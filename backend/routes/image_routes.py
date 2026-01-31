from fastapi import APIRouter, UploadFile, File
import shutil
from backend.inventory_db import add_item
from backend.services.ocr_service import extract_text, extract_expiry_date, expiry_to_days_left
from backend.services.fruit_classifier import predict_fruit
from tensorflow.keras.preprocessing.image import ImageDataGenerator

router = APIRouter(prefix="/scan", tags=["Scan"])


# -------------------------
# PACKAGED FOOD (OCR)
# -------------------------
@router.post("/packaged")
async def scan_packaged_food(user_id: str, file: UploadFile = File(...)):
    path = f"temp_{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(path)
    expiry = extract_expiry_date(text)

    if expiry:
        days_left = expiry_to_days_left(expiry)
        if days_left is not None:
            add_item(user_id, file.filename, days_left)
            return {
                "detected_text": text,
                "expiry_found": expiry,
                "days_left": days_left
            }

    return {"message": "No expiry date detected", "detected_text": text}


# -------------------------
# FRESH PRODUCE (CNN)
# -------------------------
@router.post("/fresh")
async def scan_fresh_food(user_id: str, file: UploadFile = File(...)):
    path = f"temp_{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Load class mapping only when needed (not at startup)
    fruit_datagen = ImageDataGenerator()
    temp_gen = fruit_datagen.flow_from_directory(
        "data/fruits_dataset/train",
        target_size=(224, 224),
        batch_size=1
    )
    class_indices = temp_gen.class_indices

    fruit_name = predict_fruit(path, class_indices)

    expiry_days = {
        "banana": 3,
        "apple": 7,
        "tomato": 5,
        "potato": 10
    }

    days_left = expiry_days.get(fruit_name.lower(), 5)
    add_item(user_id, fruit_name, days_left)

    return {
        "detected_item": fruit_name,
        "estimated_days_left": days_left
    }
