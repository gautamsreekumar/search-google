#!/usr/bin/python 

import sys
from subprocess import call

call("firefox https://www." + sys.argv[1] + ".com", shell = True)
# print str(sys.argv[1])
