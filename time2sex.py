#!/usr/bin/python

import sys

def time_to_seconds(time):
    try:
        time = [ int(i) for i in time.split(":") ]
    except ValueError:
        print "Please provide valid input"
        return "No"
    # python golf
    return sum( [ [1,60,3600][i]*j for i, j in enumerate(reversed(time[:3]))] )
   
if __name__ == "__main__":
    if len(sys.argv) == 2:
        print "=== %s seconds ===" % time_to_seconds(sys.argv[1])
    else:
        print "Please enter a command line arg"
        print "HH:MM:SS"
        print "EX:"
        print "    time2sex 1:23:45"
