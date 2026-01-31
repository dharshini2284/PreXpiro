from ir.bm25_engine import RecipeBM25
from backend.inventory_db import add_item, get_inventory

# -------------------------------
# 1. Initialize BM25 Engine
# -------------------------------
print("\nLoading BM25 engine...")
bm25_engine = RecipeBM25("data/recipes.csv")
print("BM25 engine ready.\n")

# -------------------------------
# 2. Basic BM25 Search (No expiry)
# -------------------------------
print("=== BASIC BM25 SEARCH ===")

query = ["tomato", "onion", "potato"]
results = bm25_engine.search(query)

for r in results:
    print(f"{r['title']} | Score: {float(r['score']):.2f}")

# -------------------------------
# 3. Add Items to MongoDB Inventory
# -------------------------------
print("\n=== ADDING ITEMS TO INVENTORY DB ===")

user_id = "user1"

add_item(user_id, "tomato", 2)   # expiring soon
add_item(user_id, "onion", 10)
add_item(user_id, "potato", 4)

print("Items added.\n")

# -------------------------------
# 4. Retrieve Inventory from DB
# -------------------------------
print("=== FETCHING INVENTORY FROM DB ===")

inventory = get_inventory(user_id)
print("Inventory:", inventory)

# -------------------------------
# 5. Expiry-Aware Recipe Ranking
# -------------------------------
print("\n=== EXPIRY-AWARE RECIPE RANKING ===")

results = bm25_engine.search_with_expiry(inventory)

for r in results:
    print(f"{r['title']} | Final Score: {r['score']}")
