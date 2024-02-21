# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   James Eardley, 2/21/2024, Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# Functions ------------------------------------------------------------------------------ #

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
   James Eardley,2.21.2024,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # global file
        # global students
    
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    James Eardley,2.21.2024,Created Class
    James Eardley,2.21.2024,Added menu output and input functions
    James Eardley,2.21.2024,Added a function to display the data
    James Eardley,2.21.2024,Added a function to display custom error messages
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user
    
        ChangeLog: (Who, When, What)
        James Eardley,2.21.2024,Created function
    
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')
        
        
    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user
    
        ChangeLog: (Who, When, What)
        James Eardley,2.21.2024,Created function
    
        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.
            
        
    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user
    
        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
    
        return choice
    
    
    @staticmethod
    def output_student_courses(student_data: list):
            """ This function displays the student registration data to the user
    
        ChangeLog: (Who, When, What)
        James Eardley,2.21.2024,Created function
        James Eardley,2.21.2024,Added code to toggle technical message off if no exception object is passed
    
        :return: None
        """
        # Process the data to create and display a custom message
            print()    
            print("-" * 50)
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-" * 50)
    
    
    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and GPA from the user
    
        ChangeLog: (Who, When, What)
        James Eardley,2.21.2024,Created function
    
        :return: str  
        """
        try:
             student_first_name = input("Enter the student's first name: ")
             if not student_first_name.isalpha():
                 raise ValueError("The last name should not contain numbers.")
             student_last_name = input("Enter the student's last name: ")
             if not student_last_name.isalpha():
                 raise ValueError("The last name should not contain numbers.")
             course_name = input("Please enter the name of the course: ")
             student_data = {"FirstName": student_first_name,
                             "LastName": student_last_name,
                             "CourseName": course_name}
             students.append(student_data)
             print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data
    
    
#---------  End of function definitions ---------#


#--------- Beginning of the main body of this script ------------------------ #

# When the program starts, read the file data into a list of lists (table)
students = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data=students)


# Present and Process the data
while (True):

    IO.output_menu(menu=MENU)
    
    menu_choice = IO.input_menu_choice()
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":

        IO.output_student_courses(student_data=students)            
        continue
    
    # Save the data to a file
    elif menu_choice == "3":

        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
