import csv
import os

data_input = open(os.path.dirname(os.path.abspath(__file__))+'/Dataset/movie_metadata.csv','r')

line = open('data-line.csv','wb')
hist = open('data-hist.csv','wb')

input_line = csv.writer(line, dialect = 'excel')
input_hist = csv.writer(hist, dialect = 'excel')

temp = True
data = []
for l in data_input:
	val = l.split(',')
	if temp:
		count = len(val)
		temp = False
	data.append(val[:count])

for n in data:
	n[count-1] = ''.join(n[count-1].splitlines())
	input_line.writerow(n)
	input_hist.writerow(n)

data_input.close()
line.close()
hist.close()