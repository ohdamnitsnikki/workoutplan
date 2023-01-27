import gspread
from google.oauth2.service_account import Credentials
import math

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('workout_plan')

user_age = 0
users_age_group = None


def start_game():
    print("\n\n============= WELCOME TO YOUR WORKOUT PLAN ===========")
    print("\nThis app is created to help you get stronger and healthier!\n")
    print("==== You will be handed a program depending on your age. ====\n")
    print("====== The older you are, the easier it will start out. ======\n")


def get_age():
    """
    Get age from user to give them the right training.
    """
    print("Please enter your age in numbers.")


def validate_age():
    """
    Inside the try, convert user answer to integers.
    Create ValueError if age isn't written in numbers.
    """

    while True:
        global user_age
        user_age = input("Your answer: \n")
        try:
            float(user_age)
            break
        except ValueError:
            print("That's not a age in numbers!")


def read_sheet(list_headers, list_numbers):
    """
    Use a while loop to read out each exercise,
    then how many times it should been done.
    """

    i = 0
    while i < len(list_headers)-1:
        print(str(list_headers[i]) + ": " + str(list_numbers[i]))
        i = i+1


def connect_training():
    """
    A function to connect user age to the right training program
    """
    parsed_age = int(user_age)
    global users_age_group
    if parsed_age <= 20:
        users_age_group = 'teenager'
        teenager = SHEET.worksheet('teenager')
        print('\nYou are in the teenager program.')
        print('This is your training for today! Do them all four times!\n')
        data = teenager.get_all_values()
        list_headers = data[0]
        list_numbers = data[-1]
        read_sheet(list_headers, list_numbers)

    elif parsed_age <= 35:
        users_age_group = 'adult'
        adult = SHEET.worksheet('adult')
        print('\nYou are in the adult program.')
        print('This is your training for today! Do them all four times!\n')
        data = adult.get_all_values()
        list_headers = data[0]
        list_numbers = data[-1]
        read_sheet(list_headers, list_numbers)

    elif parsed_age <= 50:
        users_age_group = 'mid_life'
        mid_life = SHEET.worksheet('mid_life')
        print('\nYou are in the mid_life program.')
        print('This is your training for today! Do them all four times!\n')
        data = mid_life.get_all_values()
        list_headers = data[0]
        list_numbers = data[-1]
        read_sheet(list_headers, list_numbers)

    elif parsed_age <= 70:

        users_age_group = 'elder'
        elder = SHEET.worksheet('elder')
        print('\nYou are in the elder program.')
        print('This is your training for today! Do them all four times!\n')
        data = elder.get_all_values()
        list_headers = data[0]
        list_numbers = data[-1]
        read_sheet(list_headers, list_numbers)

    else:
        users_age_group = 'senior'
        senior = SHEET.worksheet('senior')
        print('\nYou are in the senior program.')
        print('This is your training for today! Do them all four times!\n')
        data = senior.get_all_values()
        list_headers = data[0]
        list_numbers = data[-1]
        read_sheet(list_headers, list_numbers)


def validate_result():

    """
    Use a while loop to ask user to answer yes or no.
    """

    while True:
        global data_str
        data_str = input("Enter your data here: ").lower()

        try:
        
            converted_ans = data_str.lower()
            if converted_ans == "yes":
                print(f"You answered {converted_ans}\n")
                print('Your workout will be tougher tomorrow\n')
                update_worksheet()

            elif converted_ans == "no":
                print(f'You answered {converted_ans}\n')
                print('Your workout for tomorrow will be the same')
            else: 
                raise Exception("Invalid input! Answer Must Be 'Yes' or 'No'")
                   
        except Exception as e:
            print(e)
        
        else:
            break


def get_result():
    """
    Ask user if the workout was easy to know if for tomorrow
     it will be increased by 10% or not.
    """
    print("\nWas todays workout easy? If so answer Yes\n")
    validate_result()


def update_worksheet():
    """
    Update tomorrows training program to worksheet if it was easy for the user.
    """
    sheet = SHEET.worksheet(users_age_group)
    data = sheet.get_all_values()[-1]

    """
    Make list into nums to add on 10%.
    Put them back into a list and add to spreadsheet.
    """
    new_values = []

    for x in data:
        num = math.floor(int(x) * (1.1))

        new_values.append(str(num))

    sheet.append_row(new_values)
    print(new_values)


"""
Calling out functions
"""

start_game()
get_age()
validate_age()
connect_training()
get_result()
