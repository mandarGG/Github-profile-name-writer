#1/usr/bin/python
import datetime
import random
import time
from finalIndexing import *
##########
# If you want to generate some different patterns then the ones which are already present here
# then the folder components is for you. :D
###########

allowedChar = [' '] #More to add
user = raw_input("Enter the github username:- ")
email = raw_input("Enter the registered github email id:- ")
print "Now you need to enter the date from which you want to start writing your name"
time.sleep(1)
print "For more details or to know how to find date, refer README.md"
time.sleep(1)
year = int(raw_input("Enter the year:- "))
mon = int(raw_input("Enter the month:- "))
day = int(raw_input("Enter the day:- "))
name=raw_input("Enter the name (only alphabets, numbers and space supported for now):- ")
num = int(raw_input("How many commits do you want per day (more commits, darker color)..:- "))
startingDate = datetime.datetime(year, mon, day)

for word in name:
	if word.isalnum() == False and word not in allowedChar:
		print "The character " + str(word) + " is not yet released"
	elif word != ' ':
		text = "arr" + word.upper()
		increment = eval('increment' + word.upper())
		print word
		myArray = eval(text)
		for i in myArray:
			first = 'echo ' + str(random.random()) + str(random.random()) + ' > testFile'
			second = 'git add .'
			third = 'git commit -m "blah blah" --amend --author="' + user + ' <' +email + '> " --date="' + (startingDate + datetime.timedelta(days=i)).strftime("%A %B %d %Y") + '"'

			final = first + '; ' + second + '; ' + third + '; git push origin master --force'
			with open('runThis.sh', 'a') as f:
				f.write('for i in `seq 1 ' + str(num) + '`;do ' +  final+ '; done' + '\n')
		startingDate = startingDate + datetime.timedelta(days=increment*7)
	else:
		print ""
		startingDate = startingDate + datetime.timedelta(days=7)
print "Go and execute the file runThis.sh in your repository"