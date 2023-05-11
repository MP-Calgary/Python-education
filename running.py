# the purpose of this program to record running times 
# and the graph them to achieve a running goal

# import math plot libary

import matplotlib.pyplot as plt, csv
import datetime
import time

from datetime import date, datetime  

# get running info from today
def main():

    mile_run = input("Do you have a mile time to record?(yes/no) ")

    if mile_run.upper() == "YES":

        mile_date = input("What day did you run? (YYYY-MM-DD)? ")
        # print(f"This is what I recorded the date as {mile_date}. ")

        mile_time = input("How long did it take you to run the mile?(m:ss) ")
        # print(f"This is what I recorded the time as {mile_time}. ")

        # running_file = str("running_times.csv")
        running_file = str("/Users/michaelparker/Dropbox (Personal)/MP_Python/running_times.csv")

        # open file to write data to end (cursor is at end)
        with open(running_file, "a+") as runData:
            # combine data to be written to a line
            data_to_write = mile_date + "," + mile_time

            # write new data to end of file
            runData.write(data_to_write + "\n")
            #because this is in a with loop, it automatically closes file

        # Open running file again, this time in read mode, cursor at beginning
        filename_running_times = open(running_file, "r")
          
        run_date = [];
        run_time = [];
        
        for lines in filename_running_times:
            # read in the line, and split it into parts based on comman, store in file_line array
            file_line = lines.split(",")
            run_date.append(file_line[0].strip())
            run_time.append(file_line[1].strip())

        # y axis values 
        # y = ["5:52","5:58","4:00"]

        # correspodning x axis values 
        # x = ["2021-07-11", "2022-12-13", "2023-09-12"]

        # plt.plot(x,y)
        plt.plot(run_date,run_time)

        #name the x-axis
        plt.ylabel("time(mins)")

        #name the y-axis 
        plt.xlabel("date")

        #name the graph
        plt.title("Sadie's Runs")

        #rotate lables 45 degrees
        plt.xticks(rotation=45)

        #show the graph
        plt.show()
        
        # Close open file
        filename_running_times.close()
        
    else:
        print("You can do it next time! Try again tomorrow.")
main() 
