from fastapi import APIRouter
from ir.bm25_engine import RecipeBM25
from backend.inventory_db import get_inventory

router = APIRouter(prefix="/recipes", tags=["Recipes"])

bm25_engine = RecipeBM25("data/recipes.csv")

@router.get("/recommend/{user_id}")
def recommend_recipes(user_id: str):
    inventory = get_inventory(user_id)
    return bm25_engine.search_with_expiry(inventory)
