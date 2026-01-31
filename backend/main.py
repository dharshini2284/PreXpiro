from fastapi import FastAPI
from backend.routes.inventory_routes import router as inventory_router
from backend.routes.recipe_routes import router as recipe_router
from backend.routes.image_routes import router as image_router

app = FastAPI(title="PreXpiro API")

app.include_router(inventory_router)
app.include_router(recipe_router)
app.include_router(image_router)
