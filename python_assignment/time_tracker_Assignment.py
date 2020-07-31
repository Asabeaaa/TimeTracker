from tkinter import *
from datetime import timedelta
import datetime
import decimal
import sys
import csv
import time




window = Tk()
window.title("TIME TRACKER")
window.geometry('370x400')
window.configure(bg='white')



lb2= Label(window, text=" Click Start and begin work", font=("Arial Bold", 20),background='white')
lb2.grid(column=0, row=1)

lb4 = Label(window, font=("Arial", 10),background='white')
lb4.grid(column=0, row=3)

#fuction that stores the time and date after the button is clicked
def calculate_date_time():
    now = datetime.datetime.now()
    date_time=now.strftime("Date:%Y-%m-%d  Start time:%H:%M")
    global only_date
    global datee
    only_date=now.strftime("%H:%M")
    datee=now.strftime("%Y-%m-%d")
    lb4.configure (text=date_time)
    print(datee)
   
    
#Start button
btn = Button(window, text="START",command=calculate_date_time,background='white')
btn.grid(column=0, row=2)

lbl3 = Label(window, text="Enter amount then click Stop", font=("Arial Bold", 10),background='white')
lbl3.grid(column=0, row=4)

lbl5 = Label(window, text="Amount per hour:", font=("Arial", 10),background='white')
lbl5.grid(column=0, row=5)

#variable that holds how much he earns
earn_per_hour = Entry(window,width=10)
earn_per_hour.grid(column=0, row=6)
earn_per_hour.focus()

lbl9 = Label(window, text="Hours spent:", font=("Arial", 20),background='white')
lbl9.grid(column=0,row=7)

lbl6 = Label(window, text="You have earned ($):", font=("Arial", 20),background='white')
lbl6.grid(column=0,row=9)

lbl7 = Label(window, font=("Arial", 10),background='white')
lbl7.grid(column=0,row=10)

#function that stores your stop time and takes your start time and calculates your earnings
#also writes all information into a file
def money_made():
    #getting time for stop work
    now2 = datetime.datetime.now()
    date_time2=now2.strftime("%H:%M")
    
    #changes the start time into hours
    h=only_date
    delta = timedelta(hours=int(h.split(':')[0]), minutes=int(h.split(':')[1]))
    hour1 = delta.total_seconds()/3600
    
    #changes the stop time into hours
    h2=date_time2
    delta2 = timedelta(hours=int(h2.split(':')[0]), minutes=int(h2.split(':')[1]))
    hour2 = delta2.total_seconds()/3600
   
    
    #amount he earns
    amount_earned=float(earn_per_hour.get())
    
    #calculates for the difference in time(hours)
    total_hours=round(hour2-hour1,1)

    #calcultes how much is earned
    total_amount= total_hours*amount_earned
    
    #displays the hours spent working
    lbl8.configure(text=total_hours)

    #diisplays the amount earned
    lbl7.configure(text=total_amount)
    
    #passes all information to a cvs file
    with open('time_track_info.csv', mode='a') as csv_file:
        fieldnames = ['Date','Time Started', 'Time Ended ', 'Number of hours spent','Amount per hour','Total money earned $']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)    
        writer.writeheader()
        writer.writerow({'Date':datee,'Time Started':only_date, 'Time Ended ':date_time2 , 'Number of hours spent': total_hours,'Amount per hour':amount_earned, 'Total money earned $': total_amount})
        
lbl8 = Label(window, font=("Arial", 10),background='white')
lbl8.grid(column=0,row=8)  


   
 #stop button 
btn2 = Button(window, text="STOP",command=money_made,background='white')
btn2.grid(column=0, row=11)


#used to run the window
window.mainloop()


        
