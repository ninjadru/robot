#!/usr/bin/python -O
#robot
#an attempt to make a digital clone of the bullet journal
#also an attempt to learn python
#dru streicher evil.little.dru@gmail.com
#gplv2
import datetime
from optparse import OptionParser
def main():
    file = open('ana.log', 'a')
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-t", "--todo", dest="todo", help="adds an entry for a todo")
    parser.add_option("-i", "--idea", dest="idea", help="adds an entry for an idea")
    parser.add_option("-e", "--event", dest="event", help="adds an entry for an event")
    parser.add_option("-l", "--list", action="store_true", dest="lst", help="list all entries")
    (options, args) = parser.parse_args()
    if options.todo:
	output = ("* " + options.todo)
	date = datetime.datetime.now()
    	datestamp = date.strftime('%m|%d|%Y ')
    	file.write( datestamp + output + "\n" )
    	file.close()

    elif options.idea:
	output = ("! " + options.idea)
	date = datetime.datetime.now()
    	datestamp = date.strftime('%m|%d|%Y ')
    	file.write( datestamp + output + "\n" )
    	file.close()

    elif options.event:
	output = ("@ " + options.event)
	date = datetime.datetime.now()
    	datestamp = date.strftime('%m|%d|%Y ')
    	file.write( datestamp + output + "\n" )
    	file.close()

    elif options.lst:
        file = open("ana.log", "r")
	lines= file.readlines() # Note that the content of line changes 
	print ''.join(lines)
	file.close()



if __name__ == "__main__":
    main()



