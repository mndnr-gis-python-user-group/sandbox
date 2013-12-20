#-------------------------------------------------------------------------------
# Name:        sample_template.py
#
# Purpose:     Testing GitHub as well as to show how to manage arguments to
#              a script
#
# Author:      Hal Watson (hal.watson@state.mn.us)
#
# Created:     12/20/2013
#
# Requires:    Python 2.7
#
#
#-------------------------------------------------------------------------------

def main():

    import sys
    #import os
    #import arcpy

    # ---------- Incoming Arguments/Parameters ----------

    # If no arguments were passed from command line, print the usage and exit
    if len(sys.argv[1:]) < 1:
        print "python_script.py <arg1>"
        exit(1)

    # Get the incoming argument(s)  argv[0] is the script name by default
    #                               argv[1] is first real argument/parameter
    arg1 = sys.argv[1]

    # ---------------------------------------------



if __name__ == '__main__':
    main()
