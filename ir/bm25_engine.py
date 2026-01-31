import pandas as pd
from rank_bm25 import BM25Okapi
from ir.preprocess import preprocess_ingredients

class RecipeBM25:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.corpus = self.df["Cleaned_Ingredients"].fillna("").tolist()

        # 🔥 FIX: Proper tokenization
        self.tokenized_corpus = [
            preprocess_ingredients(text) for text in self.corpus
        ]

        self.bm25 = BM25Okapi(self.tokenized_corpus)

    def search(self, query_ingredients, top_k=5):
        tokenized_query = query_ingredients  # already clean words
        scores = self.bm25.get_scores(tokenized_query)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:top_k]

        results = []
        for idx in ranked_indices:
            results.append({
                "title": self.df.iloc[idx]["Title"],
                "score": float(round(scores[idx],2))
            })

        return results

    def search_with_expiry(self, inventory, top_k=5):
        """
        inventory = [
            {"name": "tomato", "days_left": 2},
            {"name": "onion", "days_left": 10}
        ]
        """

        ingredient_names = [item["name"] for item in inventory]
        expiry_map = {item["name"]: item["days_left"] for item in inventory}

        scores = self.bm25.get_scores(ingredient_names)

        final_scores = []

        for i, base_score in enumerate(scores):
            boost = 0
            recipe_tokens = self.tokenized_corpus[i]

            for ing in recipe_tokens:
                if ing in expiry_map:
                    boost += 2 / expiry_map[ing]   # urgency boost

            final_scores.append(base_score + boost)

        ranked_indices = sorted(
            range(len(final_scores)),
            key=lambda i: final_scores[i],
            reverse=True
        )[:top_k]

        return [
            {
                "title": self.df.iloc[i]["Title"],
                "score": float(round(final_scores[i], 2))
            }
            for i in ranked_indices
        ]

