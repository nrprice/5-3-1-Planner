from five_three_one_planner import create_exercise_objects_with_input, create_workout_spreadsheet, ask_for_spreadsheet
from five_three_one_tools import call_weight_plate
from first_window import Ui_First_Window
from PyQt5 import QtWidgets
import sys

welcome_message = '\nWelcome to the 5/3/1 Workout Creation Program!\n'
print('*' * len(welcome_message) + welcome_message + '*' * len(welcome_message))

def five_three_one_creator():
    print("Please choose how you would like to create your workout:\n1. With a GUI\n2. With text input\n3. Just use our handy plate calculator tool")
    answer = input('Please enter 1, 2 or 3:\n')
    # Starts creation via GUI
    if answer == '1':
        app = QtWidgets.QApplication(sys.argv)
        First_Window = QtWidgets.QMainWindow()
        ui = Ui_First_Window()
        ui.setupUi(First_Window)
        First_Window.show()
        sys.exit(app.exec_())
    # Starts creation via text input
    elif answer == '2':
        # Creates exercise objects using the function from five_three_one_planner.py
        squat, deadlift, bench, ohp = create_exercise_objects_with_input()
        # Checks if ask_for_spreadsheet returns true. Function is in five_three_one_planner.py
        if ask_for_spreadsheet():
            # Creates a spreadsheet containing the workouts using the function from five_three_one_planner.py
            create_workout_spreadsheet([squat, deadlift, bench, ohp])
            output = 'Thanks for using 5/3/1 planner! Happy training!'
            print (output)
        else:
            output = '\nOk! No sweat!\n'
            lines = '-' * len(output)
            print(lines + output + lines) \

    elif answer == '3':
        call_weight_plate()

    else:
        output = "\nWe're sorry, that was not an appropriate answer. Please try again.\n"
        print('-' * len(output) + output + '-' * len(output))

    print ('Need anything else?')
    answer = input('Enter Y or N: \n')
    if answer.lower() == 'y':
        five_three_one_creator()
    else:
        message = '\nOk bye!\n'
        stars = '*' * len(message)
        print (stars + message + stars)
        sys.exit()

    # Any incorrect entry will result in an error message, and will restart the program.

    # Calls a function to check if the user would like to calculate a target weight

if __name__ == "__main__":
    five_three_one_creator()