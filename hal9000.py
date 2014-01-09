#! /usr/bin/env python

#this script builds the icinga configuration for MMO wah edge boxes
import os

#set variables
project_name = raw_input("Project Name: ")
project_goal = raw_input("Goal: ")
due_date = raw_input("Due Date: ")
action_step = raw_input("1st Action: ") 
filename = project_name +  ".txt"

#create file and set permissions
target = open (filename, "w")
os.chmod(filename, 0644)

#user input and writing the config
target.write("==========\n")
target.write(project_name + "\n")
target.write("==========\n")
target.write("#goal:")
target.write(project_goal + "\n")
target.write("#due_date:")
target.write(due_date + "\n")
target.write("#action steps:\n")
target.write("[ ] " + action_step + "\n")
#close the file
target.close()
