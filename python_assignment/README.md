# python_assignment
#Time Tracker
This program helps one calculate how much is earned after a days work based on how much you earn per hour and how much time you put in your work.

#Description
When the start button is pressed it registers the time work is started, then asks user for an input which is how much he earns per hour. After work when the stop button is pressed it registers the time work was stopped and is able to tell the user how much he spent working and thus how much he will earn.
After, the information is written into a cvs file for future access.


#Our project was divided into 3 parts:
1.A window where all the information is displayed
2.A function that stores the start time
2.A function that stores the stop time,calculates the hours and amount earned and then writes the information into a cvs file

#Modules we imported to help us achieve this
from tkinter import *
from datetime import timedelta
import datetime
import decimal
import sys
import csv
import time

#using tinker to create our window
from tkinter import * # Import tkinter library in your Python Program.
Window = Tk() # Declare a window object using Tk() method.
Window.mainloop() # End the program using the mainloop() method for the window. This method holds the window active.Without this method the window does not run
window.title("TIME TRACKER") #Set the title of the window
window.geometry('370x400') # Set the width and height of the window
window.configure(bg='white') #Set the background of the window to white

#creating the start and stop button
We created the start and stop buttons using the Button class.
We then passed our functions to the buttons so that when clicked the functions run

#creating the lables
We created 8 lables
All the information displayed when the window is first run are lables
We created them using the lable class
3 of our lables don't display any information when the window is first run but information is generated there using the start and stop button
These lables are;the part that displays the start date and time, the part that displays how many hours were spent and the part that displays the amount he earns

#creating the edit window
We created this using the entry class which allows the user to enter the amount he earns


#Our functions
We created 2 functions
-calculate_date_time:when run it registers the current time on your laptop and stores it
-money_made: this function when run stores the current time on your laptop. Gets the start time from the first function and changes them both to hours. It then calculates how many hours were spent working by finding the difference, then calculates how much money he earns based on the entry for how much he earns an hour from the user. After it writes all the information to a file. Every time this function is run the file is appended with the information so that it does not overwrite any information stored in it
#The datetime module supplies classes for manipulating the dates and times.
#the datetime class helps us calculate for the day(year/month/day) and the time(hours:minutes) where;
year = %y

day = %d

hour = %H

month = %m

minutes = %M

#the now() function helps us get the current date and time when the function is run
#we then calculated thetime in seconds using the total_seconds() function and we were able to generate the hours by dividing it by 3600
#Then with the amount he earns, which is gotten from the input using the get() function, we are able to calculate for how much he will earn at the end of work

# CSV File
We create a csv file to collect al the info regarding the salaries

#with open('time_track_info.csv', mode='a') as csv_file
This command is used to create the name of the csv file and set the mode of addition to append so that it does not rewrite thw already existing information

#Fieldnames
COntains a list of the column headings for the data collected

#writer.writerow
Will update the spreadsheet with the date and time on your laptop when ever the progrm is run to calculate the working time.


Contributors
Abigail Sackey
Annie Boadu
Alfred Ametepey
