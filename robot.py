#!/usr/bin/python -O
#robot
#(R)eally
#(O)rganized
#(B)uilder
#(O)f
#(T)asks
#dru streicher evil.little.dru@gmail.com
#gplv2

#imports
import time
import shutil
import os, sys

#adds help menu stuff
from optparse import OptionParser

analog = ("analog.md")

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-b", "--begin", action="store_true", help="begin the day")
    parser.add_option("-e", "--event", dest="event", help="add a new event")
    parser.add_option("-t", "--task", dest="task", help="add a new task")
    parser.add_option("-n", "--note", dest="note", help="add a new note")
    parser.add_option("-l", "--list", action="store_true", dest="lst", help="lists all the active projects")
    (options, args) = parser.parse_args()
	
# begin the day
    if options.begin:
	file = open( analog, 'r')
	old_text = file.read()
	file.close()
	file = open( analog, 'w')
	# create date stamp
	date = (time.strftime("%m|%d|%y %A"))
	file.write( "#" + date + "\n")
	# add events
	file.write( "##events \n" )
	while True:
		event = raw_input("Enter Todays Events: ")
		if event == "":
			break
		file.write("- [ ] " +event + "\n")
	# add tasks
	file.write( "##tasks \n")
	count = 0
	while ( count < 3):
		mit = raw_input("What are the most important tasks today: ")
		file.write( "- [ ] !" + mit + "\n" )
		count = count +1
	# add notes
	file.write( "##notes \n\n" )
	file.write( old_text )
        file.close()
	print "Have a Great Day!"

#    elif options.archive:
#	shutil.move(active + options.archive, archive)

# add a new event
    elif options.event:
        file = open( analog,'r')
        filedata = file.read()
        new_event = ( "##events \n- [ ] " + options.event )
        file.close()

        newdata = filedata.replace("##events",new_event)

        file = open(analog,'w')
        file.write(newdata)
        file.close()

# add a new task
    elif options.task:
        file = open( analog,'r')
        filedata = file.read()
        new_task = ( "##tasks \n- [ ] " + options.task )
        file.close()

        newdata = filedata.replace("##tasks",new_task)

        file = open(analog,'w')
        file.write(newdata)
        file.close()
# add a new task
    elif options.task:
	file = open( analog,'r')
	filedata = file.read()
	new_task = ( "##tasks \n- [ ] " + options.task )
	file.close()

	newdata = filedata.replace("##tasks",new_task)

	file = open(analog,'w')
	file.write(newdata)
	file.close()	

# add a new note
    elif options.note:
        file = open( analog,'r')
        filedata = file.read()
        new_note = ( "##notes \n- " + options.note )
        file.close()

        newdata = filedata.replace("##notes",new_note)

        file = open(analog,'w')
        file.write(newdata)
        file.close() 

    elif options.lst:
	dirs = os.listdir( active )
	for file in dirs:
		print file



if __name__ == "__main__":
    main()
