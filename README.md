### Project Description: Quiz Game Application

#### Overview
This Quiz Game Application is a console-based program that interacts with the Open Trivia Database (OpenTDB) API to fetch and present quiz questions to the user. 
The application allows the user to specify the total number of questions, choose a category from a list of available categories, and select the difficulty level. 
The program then retrieves the questions from the API and quizzes the user, providing immediate feedback on their answers.

#### Key Features
1. **User Input Handling**:
   - **Total Number of Questions**: The user specifies how many questions they want in the quiz.
   - **Category Selection**: The user chooses a quiz category by entering its ID from a displayed list.
   - **Difficulty Level**: The user selects the difficulty level (Easy, Medium, Hard).

2. **API Interaction**:
   - Fetches available quiz categories from the OpenTDB API.
   - Retrieves quiz questions based on user-specified criteria (number of questions, category, difficulty).

3. **Question Presentation**:
   - Displays questions along with multiple-choice options.
   - Handles HTML entities in questions and options to present clean text.

4. **User Feedback**:
   - Provides immediate feedback on whether the user's answer is correct or incorrect.
   - Displays the correct answer if the user selects incorrectly.

5. **Error Handling**:
   - Handles invalid inputs with prompts for re-entry.
   - Manages network errors gracefully by informing the user to check their internet connection.

#### Detailed Function Descriptions

- **get_total_questions()**: Prompts the user to enter the total number of questions for the quiz. Allows up to 3 attempts for valid input and ensures the input is a
- positive integer.

- **get_category_id()**: Asks the user to select a category by entering its ID from the displayed list. Ensures the input is within a valid range and allows up to 3
- attempts for correct input.

- **get_difficulty_level()**: Prompts the user to choose a difficulty level (Easy, Medium, Hard). Ensures the input is one of the valid options and allows up to 3 attempts.

- **show_available_categories()**: Fetches and displays available quiz categories from the OpenTDB API. Returns a boolean indicating whether the categories were
- successfully retrieved.

- **fetching_questions(totalQuestions, categoryID, difficultyLevel)**: Fetches quiz questions based on user-specified criteria (number of questions, category ID,
- difficulty level) from the OpenTDB API and asks each question to the user.

- **asking_questions(question, options, correctAnswer, questionNo)**: Presents a single quiz question to the user with multiple-choice options. Handles user input for
- selecting an answer and provides feedback on the correctness of the chosen answer.

- **start_quiz()**: Orchestrates the quiz flow. It initiates the process by calling functions to get user inputs for the total number of questions, fetch and display
- available categories, get the selected category and difficulty level, and fetch and present the quiz questions.

#### Usage
To run the quiz application, simply execute the script. The user will be guided through the process of setting up the quiz by providing inputs for the number of questions, 
selecting a category, and choosing a difficulty level. The quiz will then proceed with the fetched questions, and the user will interactively answer each question with 
immediate feedback.

This Quiz Game Application provides a simple yet engaging way for users to test their knowledge on various topics and improve their learning in a fun and interactive manner.
