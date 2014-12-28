#!/usr/bin/python
import sys
import fields

def usage():
    print "Usage: python compilation.py args\nargs can be the names of one or more csv files, seperated by spaces\nthe first file must contain all the entries found in succeeding files\nOutput: one csv file compiled by field name"

if len(sys.argv) < 2:
    print "Error; no arguments given."
    usage()
    
else:
    input = []
    for arg in sys.argv[1:]:
        with open(arg) as temp_file:
            input.append(map(lambda x: x.strip().split(','),temp_file.readlines()))
    output = []
    field_list = []
    for file in input:
        for field in map(fields.getField,file[0]):
            if field not in field_list:
                field_list.append(field)
    for file in input:
        temp_fields = map(field_list.index,map(fields.getField,file[0]))
        rolls=map(lambda x:x[0], output)
        for entry in file[1:]:
            temp_entry=['' for _ in field_list] if entry[0] not in rolls else output[rolls.index(entry[0])]
            for val_nbr in range(len(entry)):
                if str(entry[val_nbr])!='':
                    temp_entry[temp_fields[val_nbr]]=str(entry[val_nbr])
            if entry[0] not in rolls:
                output.append(temp_entry)
    output.sort(key=lambda x:x[0])
    for x in [field_list]+output:
        s=''
        for y in x:
            s+=str(y)+","
        print s[:-1]
