import json
from cafe import Cafe
from utils import logger


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save()

    def __iter__(self):
        for cafe in self.data:
            yield Cafe(**cafe)

    @logger('app.log')
    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("Database file not found, creating a new one.")
            self.data = []
        except json.JSONDecodeError:
            print("Error reading JSON. Resetting database.")
            self.data = []

    @logger('app.log')
    def save(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            print("Failed to save database:", e)

    def add_cafe(self, cafe: Cafe):
        self.data.append(cafe.to_dict())

    def delete_cafe(self, name):
        name = name.lower()
        updated_cafes = []
        for cafe in self.data:
            cafe_name = cafe.get("name", "").lower()
            if cafe_name != name:
                updated_cafes.append(cafe)
        self.data = updated_cafes

    def search(self, keyword):
        for cafe in self.data:
            if keyword.lower() in cafe["name"].lower():
                yield Cafe(**cafe)
