import random

def generate_trip():
    destinations = ["New York", "Las Vegas", "Phoenix", "Gracetown", "Salt Lake City", "Lincoln", "Orlando"]
    restaurants = ["McDonalds", "Pizza Hut", "Cheesecake Factory", "Olive Garden", "Burger King", "Sonic", "IHOP"]
    transportation = ["Train", "Uber", "Airplane", "Helicopter", "Segway", "Walk", "Horse"]
    entertainment = ["See a play", "Watch a movie", "Go bowling", "Take a walk", "Ride Horses", "Read a book", "Watch paint dry"]
    trip_aspect_list = [destinations, restaurants, transportation, entertainment]
    pass

def print_trip(options):
    pass

# Have lists.
# Choose item from each
# Present Trip to user
# Ask if user would like to re-select "1-4", or accept "Y"
    # If reselect, randomly pick new option and reprint
    # If accept, just print