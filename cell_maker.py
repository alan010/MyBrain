#! /usr/bin/python

import sys, os, random

TEMP='/root/MyBrain/cell_temp.py'
BASIC_DIR='/MyBrain'

def open_temp(cell_temp): 
    return open(cell_temp).read().splitlines() 

def gen_axon(): 
    while True:
        path = '/'.join([BASIC_DIR, str(random.randint(0,255)), str(random.randint(0,255)), str(random.randint(0,255))])
        cell_name = 'cell_' +  str(random.randint(0,65535))
        axon = path + '/' + cell_name
        if not os.path.isfile(axon):
            break
    return axon
    

def set_cell(opened_temp, axon, dendrons, data):
    index_axon = opened_temp.index('axon')
    print index_axon
    index_dendrons = opened_temp.index('dendrons')
    print index_dendrons
    index_data = opened_temp.index('data')
    print index_data

    opened_temp[index_axon] = "axon = '" + axon + "'" 
    opened_temp[index_dendrons] = 'dendrons = ' + dendrons
    opened_temp[index_data] = 'data = ' + data

def make_cell(axon, temp): 
    os.system('mkdir -p ' + os.path.dirname(axon))
    tmp_axon=open(axon,'w')
    for line in temp:
        tmp_axon.write(line + '\n')
    tmp_axon.close()


#----------- main --------------
opened_cell_temp = open_temp(TEMP)
new_cell_axon = gen_axon()
print new_cell_axon
set_cell(opened_cell_temp, new_cell_axon,  sys.argv[1],  sys.argv[2])
make_cell(new_cell_axon, opened_cell_temp)
