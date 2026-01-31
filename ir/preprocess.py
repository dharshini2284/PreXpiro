import ast
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_ingredient(ingredient):
    tokens = word_tokenize(ingredient.lower())
    tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token.isalpha() and token not in stop_words
    ]
    return tokens

def preprocess_ingredients(ingredient_string):
    """
    Converts string list of ingredients into cleaned tokens
    """
    try:
        ingredient_list = ast.literal_eval(ingredient_string)
    except:
        ingredient_list = []

    final_tokens = []
    for item in ingredient_list:
        final_tokens.extend(clean_ingredient(item))

    return final_tokens
