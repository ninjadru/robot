#! /usr/bin/env python

#this script builds checklists for building a new host
import os
from optparse import OptionParser

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-p", "--physical", action="store_true", help="build a physical machine")
    parser.add_option("-v", "--virtual", action="store_true", help="build  a virtual machine ")
    (options, args) = parser.parse_args()
    host_name = raw_input("Host Name: ")
    ip = raw_input("IP: ")
    ticket = raw_input("Ticket Number: ")
    filename = "build_" + host_name +  ".txt"
    target = open(filename, "w")
    os.chmod(filename, 0644)

    if options.physical:
	target.write("==========\n")
	target.write(host_name + "\n")
	target.write("==========\n")
	target.write("IP:" + ip + "\n")
	target.write("virt-what Physical\n")
	target.write("Ticket Number:" + ticket + "\n")
	target.write("==========\n")
	target.write("[ ] verify raid array\n")
	target.write("[ ] image via pxeboot or kickseed\n")
	target.write("[ ] apt-get updates if needed\n")
	target.write("[ ] change ip\n")
	target.write("[ ] rename host\n")
	target.write("[ ] configure switch\n")
	target.write("[ ] rack at expedient\n")
	target.write("* post-install\n")
	target.write("[ ] add to ossec\n")
	target.write("[ ] puppet\n")
	target.write("  [ ] add to radsec proxy\n")
	target.write("  [ ] run puppet agent on hlbghauth01\n")
	target.write("  [ ] create manifest\n")
	target.write("	[ ] run bootstrap\n")
	target.write("  [ ] sign puppet cert \n")
	target.write("  [ ] run puppet on new host\n")
	target.write("[ ] put in dns\n")
	target.write("[ ] monitoring\n")
	target.write("  [ ] put in cacti\n")
	target.write("  [ ] put in backuppc\n")
	target.write("  [ ] put into icinga\n")
	target.write("[ ] run nessus scan\n")
	target.write("[ ] documentation\n")
	target.write("  [ ] update wiki full host list\n")
	target.write("  [ ] update trello\n")
	target.write("  [ ] update ipam\n")
	target.write("	[ ] update rt\n")
        file.close(target)

    elif options.virtual:
        target.write("==========\n")
        target.write(host_name + "\n")
        target.write("==========\n")
        target.write("IP:" + ip + "\n")
	target.write("virt-what: Virtual\n")
	target.write("Ticket Number:" + ticket + "\n")
	target.write("==========\n")
	target.write("* install")
	target.write("[ ] create vm\n")
	target.write("[ ] image using kickseed and ubuntu archive\n")
	target.write("* post-install\n")
	target.write("[ ] add to ossec\n")
        target.write("[ ] puppet\n")
        target.write("  [ ] add to radsec proxy\n")
        target.write("  [ ] run puppet agent on hlbghauth01\n")
        target.write("  [ ] create manifest\n")
        target.write("  [ ] run bootstrap\n")
        target.write("  [ ] sign puppet cert \n")
        target.write("  [ ] run puppet on new host\n")
	target.write("[ ] put in dns\n")
        target.write("[ ] monitoring\n")
        target.write("  [ ] put in cacti\n")
        target.write("  [ ] put in backuppc\n")
        target.write("  [ ] put into icinga\n")
	target.write("[ ] run nessus scan\n")
        target.write("[ ] documentation\n")
        target.write("  [ ] update wiki full host list\n")
        target.write("  [ ] update ipam\n")
	target.write("  [ ] update rt\n")
        file.close(target)




if __name__ == "__main__":
    main()
