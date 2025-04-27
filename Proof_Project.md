Student Classifier

This Python script classifies students based on their averages and allows you to check the status of a specific student.

Functionalities
Stores names and averages of students in a dictionary.
Classifies students into three categories: approved, remedial, and failed.
Prompts the user for a student's name to check their status.
Displays the student's status (approved, remedial, or failed).
How to use
Clone this repository.
Run the main.py script.
When prompted, enter the name of the student you want to check.
Student Dictionary:

Creates a dictionary called students to store each student's name as a key and their respective average as a value. Lists for Results:

Initializes three empty lists: approved, remedial, and failed. These lists will be used to store the names of the students in each category. Student Classification:

Uses a for loop to iterate over the items (name and average) in the students dictionary. Inside the loop, check each student's average: If the average is greater than 7, the student's name is added to the approved list. If the average is between 5 (inclusive) and 7 (exclusive), the student's name is added to the recovery list. Otherwise (average less than 5), the student's name is added to the failed list. Prompting the User for a Name:

The input() function is used to ask the user to enter the name of the student he wants to check. The name entered is stored in the variable student_name. Checking the Student's Status:

A series of if, elif and else conditionals checks which of the lists (approved, recovery or failed) the student_name is in. Depending on the list the student is in, a message informing his/her status (approved, in recovery or failed) is printed on the screen. If the student's name is not found in any of the lists, a message informing that the student was not found is displayed.
