from fastapi import APIRouter
from backend.inventory_db import add_item, get_inventory

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.post("/add")
def add_inventory_item(user_id: str, name: str, days_left: int):
    add_item(user_id, name, days_left)
    return {"status": "Item added"}

@router.get("/{user_id}")
def fetch_inventory(user_id: str):
    return get_inventory(user_id)
