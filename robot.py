#robot
#(R)eally
#(O)rganized
#(B)uilder
#(O)f
#(T)asks
#dru streicher evil.little.dru@gmail.com
#gplv2

import datetime
import shutil
import os, sys

#adds help menu stuff
from optparse import OptionParser

archive = "archive/"
active = "active/"
def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-c", "--create", dest="create", help="crete a new project")
    parser.add_option("-a", "--archive", dest="archive", help="archive a completed project")
    parser.add_option("-l", "--list", action="store_true", dest="lst", help="lists all the active projects")
    (options, args) = parser.parse_args()
    if options.create:
	file = open( active + options.create + ".md", 'a')
	project = ( options.create)
	goal = raw_input("What is the desied end goal:")
        file.write( "##project: " + project + "\n" )
	file.write( "##goal: " + goal + "\n" ) 
	file.write( "##actions" + "\n" )
	while True:             
		action = raw_input('enter an action: ')
		if action == "":
			break
		file.write("- [ ]" + action + "\n")
        file.close()

    elif options.archive:
	shutil.move(active + options.archive, archive)

    elif options.idea:
	output = ("! " + options.idea)
    	file.write( output + "\n" )
    	file.close()

    elif options.event:
	output = ("@ " + options.event)
    	file.write( output + "\n" )
    	file.close()

    elif options.lst:
	dirs = os.listdir( active )
	for file in dirs:
		print file



if __name__ == "__main__":
    main()
