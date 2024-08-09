"""  
2. Double Scoop with Nested Loops
Objective: The aim of this assignment is to practice using nested loops in Python.

Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at 
three different times of the day (morning, afternoon, evening) for each day 
of the week. Use nested loops to implement this: the outer loop should iterate 
over the days, and the inner loop should iterate over the times of the day. 
For each time, randomly select a mood from a predefined list and print it. 
Use the random module again to randomly select the mood.

Example Outcome: An example would be
 "On Tuesday afternoon you were sad" "On Tuesday night you were happy"
  "On Wednesday morning you were tired"

NOTE: Ensure that all code in your file is ready to run. This means 
that if someone opens your file and clicks the run button at the top, 
all code executes as intended. For example, if there are if statements, 
print statements, or for loops, they should function correctly and display output 
in the console as expected.

The goal of this note is to ensure that all code in your Python file runs smoothly 
and that is has been tested.

"""
import random 

times_of_day = ["morning", "afternoon", "evening"]
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["happy", "sad", "tired", "energetic", "calm"]

for day in range(len(days_of_the_week)):
    for time in times_of_day:
        print(f"On {days_of_the_week[day]} {time} you were {random.choice(moods)}")
    
        