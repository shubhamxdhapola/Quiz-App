import requests
import json
import random
import html

# Function to take the total number of questions from the user
def get_total_questions():

    attempts = 0 # Initialize the number of attempts

    while attempts < 3:  # Allow the user up to 3 attempts to enter valid input
        
        try:
            # Asking user for the total number of questions
            totalQuestions = int(input("\n>> Enter total numbers of questions : "))

            if totalQuestions > 0:

                return totalQuestions # Return the valid total number of questions
                
            else: 
                print(f">> Invalid input! Please enter a postive number ({3-(attempts+1)} attempts remaining).")

        except ValueError: 
            print(f"Invalid input! Please enter Enter a numeric value ({3-(attempts+1)} attempts remaining).")

        attempts += 1 # Increment the attempt count

    print("\n>> You are out of attempts") # Inform the user they are out of attempts
    
    
# Function to take the category ID from the user
def get_category_id():

    attempts = 0 # Initialize the number of attempts

    while attempts < 3:  # Allow the user up to 3 attempts to enter valid input

        try:
            # Asking user for the category ID
            categoryID = int(input("\n>> Select category by its ID : "))

            if categoryID in range(9,33): # Ensure the category ID is within the valid range

                return categoryID  # Return the valid category ID
                
            else:
                print(f">> Invalid Category ID. Please select a valid ID from the list ({3-(attempts+1)} attempts remaining).")
        
        except ValueError: 
            print(f"Invalid input! Please enter a numeric value ({3-(attempts+1)} attempts remaining).")

        attempts += 1 # Increment the attempt count
        
    print("\n>> You are out of attempts") # Inform the user they are out of attempts


# Function to take the difficulty level from the user
def get_difficulty_level():

    attempts = 0 # Initialize the number of attempts

    while attempts < 3:  # Allow the user up to 3 attempts to enter valid input
        
        try:
            # Asking user for the difficulty level
            difficultyLevel = input("\n>> Choose difficulty level (Easy, Medium, Hard) : ").strip().lower()

            if difficultyLevel in ['easy', 'medium', 'hard']: # Ensure the difficulty level is valid
                
                return difficultyLevel # Return the valid difficulty level
            
            else:
                print(f">> Invalid difficulty level. Please choose from 'easy', 'medium', or 'hard'. ({3-(attempts+1)} attempts remaining).")
   
        except Exception as e: 
            print(f">> An error occured : {e}")
        
        attempts += 1  # Increment the attempt count
    
    print("\n>> You are out of attempts") # Inform the user they are out of attempts


# Function to display available categories to the user
def show_available_categories():

    try:
        # Fetch categories from the API
        response = requests.get('https://opentdb.com/api_category.php')
        categories = json.loads(response.text)

        line = '-'
        print(f"\n{line*12}AVAILABLE CATEGORIES{line*12}\n")

        for category in categories['trivia_categories']:

            if category['name'].startswith(("Entertainment:","Science:")):
                print(f"-ID {category['id']} : {category['name'].split(': ')[1]}")
                
            else:
                print(f"-ID {category['id']} : {category['name']}")
        
        print(f'{line*44}')

        return True  # Return True to indicate successful retrieval of categories

    except: 
        print(f">> An error occured! Please check your internet connection or try again later")
        return False # Return False to indicate failure in retrieving categories


# Function to fetch questions from the API
def fetching_questions(totalQuestionss, categoryID, difficultyLevel):

    try:
        # Fetch questions from the API based on the provided total_questions, category_id, and difficulty_level
        response = requests.get(f'https://opentdb.com/api.php?amount={totalQuestionss}&category={categoryID}&difficulty={difficultyLevel}&type=multiple')
        quizes = json.loads(response.text)['results']

        # Ask each question to the user
        for questionNo, quiz in enumerate(quizes,1):

            question = quiz['question']
            correctAnswer = quiz['correct_answer']
            incorrectAnswers = quiz['incorrect_answers']
            options = incorrectAnswers + [correctAnswer]
            random.shuffle(options)

            asking_questions(question, options, correctAnswer, questionNo)

    except: 
        print(f">> An error occured! Please check your internet connection or try again later")


# Function to ask questions to the user
def asking_questions(question, options, correctAnswer, questionNo):

    # Unescape HTML characters in question and options
    question = html.unescape(question)
    options = [html.unescape(option) for option in options]
    correctAnswer = html.unescape(correctAnswer)

    optionMapping = {}  # Dictionary to map option numbers to their corresponding text
    
    line = '__'
    print(line*50)
    print(f"\nQuestion {questionNo}] {question}")

    # Display each option with a number
    for optionNo, option in enumerate(options,1):
        optionMapping[optionNo] = option
        print(f'Option {optionNo} : {option}')

    attempts = 0 # Initialize the number of attempts

    while attempts < 3: # Allow the user up to 3 attempts to answer the question

        try:
            # Asking user for the answer
            userAnswer = int(input("\n>> Choose the correct option number : "))

            if userAnswer in optionMapping:

                if optionMapping[userAnswer] == correctAnswer:
                    print(">> Correct Answer")

                else:
                    print(">> Wrong Answer")
                    print(f">> Correct answer is : {correctAnswer}")

                break
                
            else : print(f">> Invalid option choose the correct option ({3-(attempts+1)} attempts remaining)")
            
        except ValueError : print(f">> Invalid input! Please enter a numeric value ({3-(attempts+1)} attempts remaining)")

        attempts += 1 # Increment the attempt count
            
                
# Main function to start the quiz
def start_quiz():

    line = '-'
    print(f"\n{line*10}WELCOME TO THE QUIZ GAME{line*10}")

    totalQuestions = get_total_questions() # Get the total number of questions from the user
    
    if totalQuestions:
        categoriesFetched = show_available_categories() # Display available categories and check if successful
        
        if categoriesFetched: 
            categoryID = get_category_id()  # Get the category ID from the user

            if categoryID : 
                difficultyLevel = get_difficulty_level()  # Get the difficulty level from the user

                if difficultyLevel:
                    fetching_questions(totalQuestions, categoryID, difficultyLevel) # Fetch and ask the questions        
        
if __name__ == "__main__":

    start_quiz() # Start the quiz when the script is executed directly
