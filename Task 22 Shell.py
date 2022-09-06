'''
Task 22 Level 3 

This is a big one! Stay calm though here's some guidelines to work through and help you get past this monster of a task!
There are about 5 parts to this task that we can break down (4 Functions and then main function):
                            - Reading CSV files (Pretty easy and straightforward)
                            - Calculating Eucledian Distance (Not too difficult, but not easy either)
                            - Initializing Clusters (Will struggle on this bit)
                            - Implementing the K-Means Algorithim (Can either be really easy or rather difficult, 
                                                                   depending on how well you Google)
                            - Finally putting it all together in the main function 
Keep in mind that Rome was not built in a day! This task will take time, up to about 10 days, depending on how much
        time you put into this task on a day-to-day basis.

Remember to stick to a plan, draw out some pseudo code, break the task down into coherrent steps.
        Even make some flow charts, read up on how Machine Learning works and its basics to keep yourself sharp.
        
Part 0 : We need imports! We know we are going to be plotting data and doing some advanced maths for this task as well as
        reading a csv file. So we need those necessary imports. 
'''
# Numpy allows us to do the math to the data
import numpy as np
 
# csv does a similar function compared to pandas
import csv

# Matplotlib allows us to plot the graphs when it is time to plot nearer to the end of this task
import matplotlib as plt

# And Finally random, because we use random to find and initialize the clusters that we need to calculate the distance to
import random 

'''
Part I : We know that there are 3 datasets we need to be able to read when the user decides. So first we should create
        a function that allows us to read any of the three csv files (Keep in mind that Birthrate is x and Life Expectancy
                                                                      is y)
'''

# Define function with one argument since we will be using a csv file to be able to... Well, y'know. Read the file.
# The read file should also be returned as a list for use within our calculations. This can also be done outside this function
def readCSV(file):
    
    with open(file, 'r') as csvfile:
        read = csv.reader(csvfile, delimiter = ',')
        
'''
We are now able to read whichever file the user chooses. Now we get into the mathematical part of things. (No worries,
    numpy makes this easy for us)

Part II : Finding the Euclidean distance between any two points. This is one of the math parts of the task
            The PDF contains what the Eucliedian distance calculation it is. It's up to you for how the calculation is done
                in Python, HINT : np.sqrt allows you to calculate the square root of a value.
                    Also keep in mind that you can use nested loops to separate x1 and x2 and y1 and y2
'''

# Define a function that will be called when we need the Eucledian Distance between two points
# Remember that np.sqrt is the numpy version in python to calculate the square root of a value 
# And since we know that the Euclidean calculation is done with two x and y values, that tells us we need a 2d list in order to complete the calculation.
def euclideanDistCalc():
   np.sqrt()
   
   
'''
Part III : Initalizing the Clusters. This part is determined by the amount of clusters the user wants in their analysis. 
        This can be done easily by creating two empty lists and appending (using a for loop) the data from the actual dataset (we can refer to this in 
	our function as strList) then we append this data to our empty X and Y lists and use .random to take a random sample for our cluster initialization.
'''
def initClusters(strList, numClusters):
    
    x = []
    y = []
    
    
'''
Part IV : And finally for our last bit, we'll be implementing the kMeans algorithm. This can be really easy (with proper research) or you can be 
	extra and create a function yourself! 

'''
def kMeansAlg():
    cmaps = [" ", "Blue", "Green", "Purple", "Pink", "Red", "Orange", "Brown", "Black", "Yellow", "Grey"] 
    # If you're feeling tough
    
    
'''
Part V : And now, we put all these functions to use to get the desired outcome we need. Start by asking the user what dataset they'd like to use

'''

dataSet1 = readCSV(input('''Plese enter the file name you want to use: 
                    data1953.csv
                    data2008.csv
                    dataBoth.csv \n''' ))               
                                                                                        
# Initalising cluster points
cluster_amount = int(input("Input cluster amount:"))                     
x, y = initClusters(dataSet1, cluster_amount)
