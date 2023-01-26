import gspread
from google.oauth2.service_account import Credentials

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

   # data_str = input("Enter your data here: ")
   # print(f"The data provided is {data_str}")
    validate_age()

def validate_age():
    """
    Inside the try, convert user answer to integers. Create ValueError if age isn't written in numbers.
    """

    while True:
      global user_age
      user_age = input("\nYour answer: ")
      try:
        val = float(user_age)
        break
      except ValueError:
        print("That's not a age in numbers!")

def connect_training():
    """
    A function to connect user age to the right training program
    """
    parsed_age = int(user_age)
    if parsed_age <= 20:
        global users_age_group
        users_age_group = 'teenager'
        teenager = SHEET.worksheet('teenager')
        print('You are in the teenager program')
        data = teenager.get_all_values()
        print(data)

    elif parsed_age <= 35: 
        users_age_group = 'adult'
        adult = SHEET.worksheet('adult')
        print('You are in the adult program')
        data = adult.get_all_values()
        print(data)

    elif parsed_age <= 50:
        users_age_group = 'mid_life'
        mid_life = SHEET.worksheet('mid_life')
        print('You are in the mid_life program')
        data = mid_life.get_all_values()
        print(data)

    elif parsed_age <= 70:
        
        users_age_group = 'elder'
        elder = SHEET.worksheet('elder')
        print('You are in the elder program')
        data = elder.get_all_values()
        print(data)

    else:
        users_age_group = 'senior'
        senior = SHEET.worksheet('senior')
        print('You are in the senior program')
        data = senior.get_all_values()
        print(data)

def get_result():
    """
    Ask user if the workout was easy to know if for tomorrow it will be increased by 10% or not.
    """
    print("Was todays workout easy? If so answer Yes")
   

    data_str = input("Enter your data here: ")
    converted_ans = data_str.lower()
    if converted_ans == "yes":
        print(f'Since you answered {converted_ans}, workout will be tougher tomorrow')
       
    
    else:
        print(f'Since you answered {converted_ans}, the workout for tomorrow will be the same')



def update_worksheet():
    """
    Update tomorrows training program to the worksheet.
    """

    print(users_age_group)
    SHEET.worksheet(users_age_group)

    # print(worksheet)
    # print(f"Updating {worksheet} tomorrows training program...\n")
    # worksheet_to_update = SHEET.worksheet(worksheet)
    # worksheet_to_update.append_row(data)
    # print(f"{worksheet} worksheet updated successfully\n")


get_age()
connect_training()
get_result()
update_worksheet()
