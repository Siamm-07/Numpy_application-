# Numpy-real-life-applicationn
#A fitness app stores the daily step count data of a user for 2 months. Performing data analysis to :
#Calculate the total and average step count.
#Identify how many days the user met the 10,000-step goal.
#Determine the most active and least active days.
import numpy as np
np.random.seed(42)  #this is to give the same data everytime (history)
steps = np.random.randint(3000,15000,60)
total_steps = np.sum(steps)
av_steps = np.mean(steps)
days_meeting_goal = np.sum(steps>=10000)
most_active_day = np.argmax(steps)
least_active_day = np.argmin(steps)
print("Steps taken in the past 60 days \n",steps)
print(f"Total steps taken in 2 months is {total_steps}")
print(f"Average amount of steps taken daily is {av_steps}")
print(f"Number of days where the goal was met : {days_meeting_goal}")
print(f"The most active day (day {most_active_day + 1}) : {steps[most_active_day]} steps") #The data is stored in an array using +1 as 
#indexing in python starts with 0 
print(f"The least active day (day {least_active_day + 1}) : {steps[least_active_day]} steps")
