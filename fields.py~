import sys
from difflib import SequenceMatcher

fields=[]



class field:
    name=""
    alt_names=[]
    
    def __init__(n="",alt=[]):
        name=n
        alt_names=alt

def print_all_fields():
    s = ""
    for f in fields:
        s+=f.name+','
    print s[:-1]

def getField(input_field):
    if len(fields)<1:
        print "Error: no fields present in db"
        return ""
    closeness = []
    for f in fields:
        amp = len(f.alt_names) + 1
        temp_close = SequenceMatcher(None, f.name, input_field).ratio()*amp
        for x in f.alt_names:
            temp_close+=SequenceMatcher(None, x, input_field).ratio()
        temp_close/=((amp*2)-1) 
        closeness.append((f,temp_close))
    closeness.sort(key=lambda x:x[1], reverse=True)
    return closeness[0][0]
