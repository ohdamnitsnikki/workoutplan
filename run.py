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
        print('You are in the teenager program')

    elif get_age <= 35: 
         adult = SHEET.worksheet('adult')
         print('You are in the adult program')

    elif get_age <= 50:
        mid_life = SHEET.worksheet('mid_life')
        print('You are in the mid_life program')

    elif get_age <= 70:
        elder = SHEET.worksheet('elder')
        print('You are in the elder program')

    else:
        senior = SHEET.worksheet('senior')
        print('You are in the senior program')

def get_result():
    """
    Ask user if the workout was easy to know if for tomorrow it will be increased by 10% or not.
    """
    print("Was todays workout easy? Answer Yes or No")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")
    
    if data_str != Yes:
        print(f'Since you answered {}, workout will be tougher tomorrow')
        #Write code for specific age to get added by 10%

        else:
            print(f'Since you answered {}, the workout for tomorrow will be the same')

def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


# def main():
#     """
#     Run all functions
#     """
# get_age()
# validate_age()
# connect_training()
# get_result()
# main()