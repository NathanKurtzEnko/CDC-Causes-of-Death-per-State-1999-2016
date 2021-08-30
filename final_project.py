#import necessary files and packages
import csv
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QLabel


class deathData: #create a class
    #initialize class to have a bunch of attributes that are lists 
    #which were derived from an array which uses an argument 
    #AllLines which is data that has been read into a large list.
    def __init__(self, allLines): 
        self.data = np.array(allLines)
        self.year = []
        for year in self.data[1:, 0]:
            self.year.append(year)
        self.intent = []
        for intent in self.data[1:, 1]:
            self.intent.append(intent)
        self.cause = []
        for cause in self.data[1:, 2]:
            self.cause.append(cause)
        self.state = []
        for state in self.data[1:, 3]:
            self.state.append(state)
        self.age = []
        for age in self.data[1:, 5]:
            self.age.append(age)
        self.deaths = []
        for deaths in self.data[1:, 4]:
            self.deaths.append(int(deaths))
                 
    def gather(self, column): 
        #function that returns a list of information that corresponds to 
        #a specified column of the data set
        if column == "year":
            return self.year
        if column == "intent":
            return self.intent
        if column == "cause":
            return self.cause
        if column == "state":
            return self.state
        if column == "age":
            return self.age
        if column == "deaths":
            return self.deaths    
    
    def totStateCause(self, state):
        #function that returns a dictionary of the total number
        #of deaths that occur in a specified state
        mydict = {}
        for index, st in enumerate(self.state):
            cause = self.cause[index]
            deaths = self.deaths[index]
            if st == state and cause != "All causes": 
                #Does not consider ALL causes because that inflates 
                #total numbers as it is a sum of all deaths for all causes
                mydict[cause] = mydict.get(cause, 0) + deaths
        return mydict
    
    def totDeathCauseYearState(self, cause, year, state):
        #similar to totStateCause, just also takes into account year
        for info in self.data:
            if info[0] == year and info[2] == cause and info[3] == state:
                tot = int(info[4]) #this is the total deaths in a state for a particular cause, in a particular year
        return tot
    
    def makeEverything(self):
        a = self.gather("cause")
        b = [] 
        for i in a:
            if i != "All causes":
                b.append(i) #for loop removes all instances of 'All causes'
        causes = list(set(b)) #compiles list of unique causes
        years = list(range(1999,2017)) #compiles all the unique years covered in the data set
        for index, i in enumerate(years):
            years[index] = str(i) #converts all values in year list to strings
        more = True
        while more:
            state = input("What state would you like to examine?\nExample, -->Kansas\nEnter 'done' to stop.\n-->")
            #^user input to examine a state
            if state == "done": #if they want to end then end it
                more = False
                break
            #plot one
            plt.figure(1)
            tot = self.totStateCause(state) #finds the total deaths for each cause in a particular state
            for key, value in tot.items():
                plt.barh(key, value) #plots the a horizontal bar for each cause that is of length equal to the number of deaths
            plt.title("All deaths for {0}".format(state))
            plt.pause(.05) #need this to render plot in a while loop
            for cause in causes:
                #adds to list the number of deaths for a cause for each year, then resets list to empty and does the same for a new cause
                dataList = []
                for year in years:
                    dataList.append(self.totDeathCauseYearState(cause, year, state))
                plt.plot(years, dataList, label = cause) #plots what is curently in the data list with deaths on y axis, year on x axis, and color of line being the cause
                # this will create a bunch of lines in one plot frome
            plt.xticks(rotation = 45)            
            plt.title("All deaths by cause for {0}".format(state))
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            plt.pause(.05)
          
                
def readFile(path):
    #functon that reads in a file with given file path, file must be a csv and separated by commas
    allLines = []
    with open(filePath, "r") as csvStream:
        namesReader = csv.reader(csvStream, delimiter = ",")
        for line in namesReader:
            allLines.append(line)
    return allLines
     

filePath = "C:/Users/nathan/Desktop/final project/NCHS_-_Leading_Causes_of_Death__United_States.csv"
allLines = readFile(filePath)
data = deathData(allLines)


data.makeEverything()


print("As we examine many states across the USA, many causes of death remain unchanged in number from 1999-2016.\nHowever, there seems to be a trend in CLRD, cancer, and Alzheimer's of increased deaths per year over the past few years.\nTo increase the general public's health, it may be important to focus research on these areas and keep people informed about these diseases.")
print("Research can be further focused by geograhical region as well in order to address health issues more efficiently.\nThe leading causes of death nationally are still cancer and heart disease and further work should be done in these areas still.")