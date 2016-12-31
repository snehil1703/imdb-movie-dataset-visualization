#Importing required libraries
import sys
import csv
import matplotlib.pyplot as plt
from pylab import plot, show, savefig
import numpy as np
import datetime
import math
import os

#Function to clean data and picking required columns for visualization of LineChart
def clean(lineChartFile):
    req_columns = ['director_name','genres','title_year','imdb_score']
    
    if os.path.isfile(lineChartFile):
        input_file = open(lineChartFile,'r')
    else:
        print "File does NOT exist"
        sys.exit()

    rdr = csv.reader(input_file)
    header = rdr.next()
    columns = [header.index(i) for i in req_columns]
    input_data = [ [] , [] , [] , [] ]

    org_count = 0    
    for l in input_file:
        line = l.split(',')
        org_count += 1
        
        data = [line[i] for i in columns]
        if('' not in data and data[2].isdigit()):
            try:
                temp = float(data[3])
                if (int(data[2])<=datetime.datetime.now().year and temp<=10):
                    data[1] = data[1].split('|')
                    for i,j in zip(input_data,data):
                        i.append(j)
            except ValueError:
                pass

    file.close
    return input_data, org_count

if __name__ == "__main__":
    #Checking for required arguments
    if len(sys.argv) != 2:
        print "Invalid arguments. Requires exactly 1 argument (ie. CSV File)."
        sys.exit()
    else:
        input_file = sys.argv[1]

    #Calling 'clean' function
    input_data, org_count = clean(input_file)
    
    print "Number of entries removed after cleaning data: ", org_count - len(input_data[0])

    max_year = int(max(input_data[2]))
    min_year = int(min(input_data[2]))
    year = [i for i in range(min_year, max_year+1)]
    yearMovieCount = []
    for i in range(min_year,max_year+1):
        yearMovieCount.append(input_data[2].count(str(i)))
    
    #Plotting Linechart - Basic
    plt.clf()
    plt.plot(year, yearMovieCount)
    plt.ylabel('Number of Movie Releases')
    plt.xlabel('Release Year')
    plt.title('Line chart - Release/Year')
    savefig(os.path.dirname(os.path.abspath(__file__))+'/linechart.png')
    plt.show()

    #Calculating specific information iteratively and Plotting all respective possible linecharts
    count = 0
    for j in [4,5,10,20]:
        count += 1
        splityear_count = (max_year - min_year) / j
        year = [i for i in range(min_year, max_year+1, j)]
    
        yearClass = []
        for i in range(len(input_data[0])):
            yearClass.append(min_year + int(math.ceil((float(int(input_data[2][i])) - float(min_year))/j)) * j)
        #for i in range(len(input_data[0])):
        #    print input_data[2][i], yearClass[i]
        #print j, 'Years'
        
        yearMovieCount = []
        for i in range(min_year,max_year+1, j):
            yearMovieCount.append(yearClass.count(i))
        #print year, yearMovieCount
        #print min(yearMovieCount), max(yearMovieCount)
        
        plt.clf()
        plt.plot(year, yearMovieCount)
        plt.xticks(np.arange(min_year, max_year+1, j), rotation=90)
        plt.ylabel('Number of Movie Releases')
        plt.xlabel('TILL (Release Year)')
        plt.title('Line chart - Release/'+str(j)+' Years')
        savefig(os.path.dirname(os.path.abspath(__file__))+'/linechart'+str(count)+'.png')
        plt.show()

