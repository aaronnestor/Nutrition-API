# Nutrition Analysis API with edamam.com

import requests
import json

class NutritionAnalysis:
    def __init__(self, api_id, api_key):
        self.api_id = api_id
        self.api_key = api_key
    def analyze(self, ingredients):
        url = "https://api.edamam.com/api/nutrition-details"
        querystring = {"app_id": self.api_id, "app_key": self.api_key}
        payload = json.dumps({"title":"Nutrition Analysis", "ingr": ingredients})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=payload, headers=headers, params=querystring)
        return response.json()

if __name__ == "__main__":
    with open ('api_keys.json') as f:
        data = json.load(f)
        api_id = data['api_id']
        api_key = data['api_key']
    ingredients = ["1 cup of milk", "1 cup of sugar", "1 cup of flour"]
    nutrition_analysis = NutritionAnalysis(api_id, api_key)
    print(nutrition_analysis.analyze(ingredients))