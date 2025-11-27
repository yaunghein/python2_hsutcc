import sys
import random
import webbrowser
from cafe import Cafe
from database import Database
from utils import logger


def menu():
    print("\n=== GREEN CAFE FINDER ===")
    print("1. Add Café")
    print("2. List All Cafés")
    print("3. Search Café")
    print("4. Suggest Random Café")
    print("5. Delete Café")
    print("6. Open Map")
    print("0. Exit")


@logger('app.log')
def add_cafe(database):
    name = input("Name: ")
    district = input("District: ")
    map_link = input("Map Link: ")

    cafe = Cafe(name, district, map_link)
    database.add_cafe(cafe)


@logger('app.log')
def list_all(database):
    cafes = list(database)
    if not cafes:
        print("No cafés available.")
        return []
    print("\nSelect a café to open in Google Maps:")
    for index, cafe in enumerate(cafes, start=1):
        print(f"{index}. {cafe.name} ({cafe.district})")
    return cafes


@logger('app.log')
def search_cafe(database):
    keyword = input("Search keyword: ")
    results = list(database.search(keyword))
    if not results:
        print("No café found.")
    else:
        for cafe in results:
            print(cafe)


@logger('app.log')
def random_suggestion(database):
    cafes = list(database)
    if cafes:
        print("Try:", random.choice(cafes))
    else:
        print("No cafés available.")


@logger('app.log')
def delete_cafe(database):
    name = input("Name to delete: ")
    database.delete_cafe(name)
    print("Removed if existed.")


@logger('app.log')
def open_map(cafe):
    print(f"Opening Google Maps for {cafe.name}...")
    webbrowser.open(cafe.map_link)


@logger('app.log')
def open_cafe_map(database):
    cafes = list_all(database)
    try:
        choice = int(input("Enter number: "))
        if 1 <= choice <= len(cafes):
            selected = cafes[choice - 1]
            open_map(selected)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")


with Database("cafes.json") as database:
    try:
        while True:
            menu()
            choice = input("Choose: ")

            if choice == "1":
                add_cafe(database)
            elif choice == "2":
                list_all(database)
            elif choice == "3":
                search_cafe(database)
            elif choice == "4":
                random_suggestion(database)
            elif choice == "5":
                delete_cafe(database)
            elif choice == "6":
                open_cafe_map(database)
            elif choice == "0":
                print("Adios!")
                break
            else:
                print("Invalid choice.")
    except KeyboardInterrupt:
        print("\n\nAdios!\n")
        sys.exit(0)
