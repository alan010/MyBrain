#! /usr/bin/python

import sys,os

#---------- basic cell structure ----------

#Once been set, cannot be changed then.
axon

#always can be changed.
dendrons

#Once been set, cannot be changed then.
data

#---------- basic cell fucntions ----------
def cell_self_destroyed():
    os.system('rm -f %s' % (sys.argv[0],))

def cell_health_check():
    if axon == '' or  data == ():
        cell_self_destroyed()
    
def print_data():
    print "===> cell_axon: %s:" % (axon,)
    for i in data:
        print i

#---------- cell work ----------

print_data
