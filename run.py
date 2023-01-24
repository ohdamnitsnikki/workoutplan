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

def get_age():
    """
    Get age from user to give them the right training.
    """
    print("Please enter your age in numbers.")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")
    validate_age(get_age)

def validate_age(value):
    """
    Inside the try, convert user answer to integers. Create ValueError if age isn't written in numbers.
    """
    try:
        if len(value) != 1:
            raise ValueError(
                f"Only one value is required not {len(value)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

def connect_training():
    """
    A function to connect user age to the right training program
    """
    if get_age <= 20:
        teenager = SHEET.worksheet('teenager')
        print(You got the teenager program)

    elif get_age <= 35: 
         adult = SHEET.worksheet('adult')
         print(You got the adult program)

    elif get_age <= 50:
        mid_life = SHEET.worksheet('mid_life')
        print(You got the mid_life program)

    elif get_age <= 70:
        elder = SHEET.worksheet('elder')
        print(You got the elder program)

    else:
        senior = SHEET.worksheet('senior')
        print(You got the senior program)

def get_result():
    """
    Ask user if the workout was easy to know if for tomorrow it will be increased by 10% or not.
    """
    print("Was todays workout easy? Answer Yes or No")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")
    
    if Yes:
        
def main():
    """
    Run all functions
    """
get_age()
validate_age()
connect_training()
get_result()
main()