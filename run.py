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
        print('You are in the teenager program.')
        print('This is your training for today! Do them all four times!')
        data = teenager.get_all_values()
        list_headers = data[0]
        list_numbers = data[-1]
        read_sheet(list_headers, list_numbers)

    elif parsed_age <= 35:
        users_age_group = 'adult'
        adult = SHEET.worksheet('adult')
        print('You are in the adult program.')
        print('This is your training for today! Do them all four times!')
        data = adult.get_all_values()
        list_headers = data[0]
        list_numbers = data[-1]
        read_sheet(list_headers, list_numbers)

    elif parsed_age <= 50:
        users_age_group = 'mid_life'
        mid_life = SHEET.worksheet('mid_life')
        print('You are in the mid_life program.')
        print('This is your training for today! Do them all four times!')
        data = mid_life.get_all_values()
        list_headers = data[0]
        list_numbers = data[-1]
        read_sheet(list_headers, list_numbers)

    elif parsed_age <= 70:

        users_age_group = 'elder'
        elder = SHEET.worksheet('elder')
        print('You are in the elder program.')
        print('This is your training for today! Do them all four times!')
        data = elder.get_all_values()
        list_headers = data[0]
        list_numbers = data[-1]
        read_sheet(list_headers, list_numbers)

    else:
        users_age_group = 'senior'
        senior = SHEET.worksheet('senior')
        print('You are in the senior program.')
        print('This is your training for today! Do them all four times!')
        data = senior.get_all_values()
        list_headers = data[0]
        list_numbers = data[-1]
        read_sheet(list_headers, list_numbers)


def get_result():
    """
    Ask user if the workout was easy to know if for tomorrow it will be increased by 10% or not.
    """
    print("Was todays workout easy? If so answer Yes")

    data_str = input("Enter your data here: ")
    converted_ans = data_str.lower()
    if converted_ans == "yes":
        print(f'Since you answered {converted_ans}, workout will be tougher tomorrow')
        update_worksheet()

    else:
        print(f'Since you answered {converted_ans}, the workout for tomorrow will be the same')


def update_worksheet():
    """
    Update tomorrows training program to worksheet if it was easy for the user.
    """
    sheet = SHEET.worksheet(users_age_group)
    data = sheet.get_all_values()[-1]

    new_values = []

    for x in data:
        num = math.floor(int(x) * (1.1))

        new_values.append(str(num)) 

    sheet.append_row(new_values)


get_age()
validate_age()
connect_training()
get_result()
