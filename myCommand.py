#!/usr/bin/python 

import sys # to take command line arguments
from subprocess import call # to execute bash commands using Python

search_key_for_google = '+'.join("%s" % (sys.argv[i]) for i in range(1, len(sys.argv)))
# creates a new string by joining
# the strings in the list passed as
# system argument using .join method
call("firefox https://www.google.com/search?q=" + search_key_for_google, shell = True)
# opening firefox browser using bash
