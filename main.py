import random

def main():
    generated_option_list, trip_option_list = generate_trip()
    get_user_input(generated_option_list, trip_option_list)

def generate_trip():
    destination_options = ["New York", "Las Vegas", "Phoenix", "Gracetown", "Salt Lake City", "Lincoln", "Orlando"]
    restaurant_options = ["McDonalds", "Pizza Hut", "Cheesecake Factory", "Olive Garden", "Burger King", "Sonic", "IHOP"]
    transportation_options = ["Train", "Uber", "Airplane", "Helicopter", "Segway", "Walk", "Horse"]
    entertainment_options = ["See a play", "Watch a movie", "Go bowling", "Take a walk", "Ride Horses", "Read a book", "Watch paint dry"]
    trip_option_list = [destination_options, restaurant_options, transportation_options, entertainment_options]
    #destination, restaurant, transportation, entertainment = generate_all_options(trip_option_list)
    # Scratch that. Leave as list.
    generated_option_list = generate_all_options(trip_option_list)
    return generated_option_list, trip_option_list

#Returns the four options as a list of Strings chosen from generated option lists
#This is superflous with generate_trip.
def generate_all_options(trip_option_list):
    destination = trip_option_list[0][random.randint(0, 6)]
    restaurant = trip_option_list[1][random.randint(0, 6)]
    transportation = trip_option_list[2][random.randint(0, 6)]
    entertainment = trip_option_list[3][random.randint(0, 6)]
    generated_option_list = [destination, restaurant, transportation, entertainment]
    return generated_option_list

def print_current_options(generated_option_list):
    destination, restaurant, transportation, entertainment = generated_option_list
    print()
    print(f"Your current options are:") # Could change for final options
    print(f"1 - Destination: {destination}")
    print(f"2 - Restaurant: {restaurant}")
    print(f"3 - Transportation: {transportation}")
    print(f"4 - Entertainment: {entertainment} \n")

def get_user_input(generated_option_list, trip_option_list):
    user_input = ''
    print_current_options(generated_option_list)
    while user_input != "Y":
        print (("If you would like to change something specific, press the number of that item and hit Enter."))
        print (("To change everything at once, press 5 and hit Enter."))
        user_input = input ("If you are satisfied with these options, type \"Y\" and hit Enter. ")
        generated_option_list = change_trip_option(generated_option_list, user_input, trip_option_list)
        print_current_options(generated_option_list)
        # Should check for invalid inputs to be more robust
    print ("We're glad you're satisfied.")

        
def change_trip_option(generated_option_list, item_to_change, trip_option_list):
    #Should actually make sure it doesn't return same by random chance.
    match item_to_change:
        case "1":
            destination = trip_option_list[0][random.randint(0, 6)]
            generated_option_list[0] = destination
            return generated_option_list #Find way to always do this, regardless of case.
        case "2":
            restaurant = trip_option_list[1][random.randint(0, 6)]
            generated_option_list[1] = restaurant
            return generated_option_list
        case "3":
            transportation = trip_option_list[2][random.randint(0, 6)]
            generated_option_list[2] = transportation
            return generated_option_list
        case "4":
            entertainment = trip_option_list[3][random.randint(0, 6)]
            generated_option_list[3] = entertainment
            return generated_option_list
        case "5":
            generated_option_list = generate_trip()[0] # to not get trip_option_list
            return generated_option_list 
        case "Y": # or "y"
            return generated_option_list
main()