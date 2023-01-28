import random

def generate_trip():
    destinations = ["New York", "Las Vegas", "Phoenix", "Gracetown", "Salt Lake City", "Lincoln", "Orlando"]
    restaurants = ["McDonalds", "Pizza Hut", "Cheesecake Factory", "Olive Garden", "Burger King", "Sonic", "IHOP"]
    transportation = ["Train", "Uber", "Airplane", "Helicopter", "Segway", "Walk", "Horse"]
    entertainment = ["See a play", "Watch a movie", "Go bowling", "Take a walk", "Ride Horses", "Read a book", "Watch paint dry"]
    trip_aspect_list = [destinations, restaurants, transportation, entertainment]

def make_initial_plan(trip_aspect_list):
    destination = trip_aspect_list[0][random.randint(0, 6)]
    restaurant = trip_aspect_list[1][random.randint(0, 6)]
    transportation = trip_aspect_list[2][random.randint(0, 6)]
    entertainment = trip_aspect_list[3][random.randint(0, 6)]

def change_trip_aspect(trip_aspect_list, item_to_change):
    match item_to_change:
        case 1:
            destination = trip_aspect_list[0][random.randint(0, 6)]
            return destination
        case 2:
            restaurant = trip_aspect_list[1][random.randint(0, 6)]
            return restaurant
        case 3:
            transportation = trip_aspect_list[2][random.randint(0, 6)]
            return transportation
        case 4:
            entertainment = trip_aspect_list[3][random.randint(0, 6)]
            return entertainment

def print_trip(options):
    pass

# Have lists.
# Choose item from each
# Present Trip to user
# Ask if user would like to re-select "1-4", or accept "Y"
    # If reselect, randomly pick new option and reprint
    # If accept, just print