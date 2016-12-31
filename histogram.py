#Importing required libraries
import sys
import csv
import matplotlib.pyplot as plt
from pylab import plot, show, savefig
import datetime
import os

#Function to clean data and picking required columns for visualization of LineChart 
def clean(histChartFile):
    req_columns = ['title_year','num_critic_for_reviews','num_user_for_reviews','director_facebook_likes']                                                     
    
    if os.path.isfile(histChartFile):
        input_file = open(histChartFile,'r')
    else:
        print "File does NOT exist"
        sys.exit()
    
    rdr = csv.reader(input_file)
    header = rdr.next()
    columns = [header.index(i) for i in req_columns]
    input_data = [ [] , [] , [] , [] , [], []]

    org_count = 0    
    for l in input_file:
        line = l.split(',')
        org_count += 1
        data = [line[i] for i in columns]
        if('' not in data and data[0].isdigit() and data[1].isdigit() and data[2].isdigit() and data[3].isdigit()):
            if (int(data[0])<=datetime.datetime.now().year and int(data[1])>=0 and int(data[2])>=0 and int(data[3])>=0):
                for i,j in zip(input_data,data):
                    i.append(int(j))
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

    #Plotting Histogram
    plt.clf()
    plt.hist(input_data[1],50, color = 'red', alpha = 0.5, histtype = "bar")
    plt.xlabel('Number of Critic Reviews')
    plt.ylabel('Frequency')
    plt.title('Histogram - Critic Reviews')
    savefig('histogram.png')
    plt.show()

    plt.clf()
    plt.hist(input_data[2],50, color = 'green', alpha = 0.5, histtype = "bar")
    plt.xlabel('Number of User Reviews')
    plt.ylabel('Frequency')
    plt.title('Histogram - User Reviews')
    savefig('histogram1.png')
    plt.show()

    plt.clf()
    plt.hist(input_data[3],50, color = 'blue', alpha = 0.5, histtype = "bar")
    plt.xlabel('Number of Director Facebook Likes')
    plt.ylabel('Frequency')
    plt.title('Histogram - Facebook Likes')
    savefig('histogram2.png')
    plt.show()
    