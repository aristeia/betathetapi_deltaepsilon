import sys
from difflib import SequenceMatcher

class field:
    name=""
    alt_names=[]
    
    def __init__(self,name="",alt=[]):
        self.name=name
        self.alt_names=alt

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
        closeness.append((f,max([SequenceMatcher(None,x,input_field).ratio() for x in f.alt_names+[f.name]])))
    closeness.sort(key=lambda x:x[1], reverse=True)
    return closeness[0][0].name


fields=[]

with open("fields.txt") as field_file:
    fields=map((lambda x: field(name=str(x[0])) if len(x)==1 else field(name=str(x[0]),alt=map(lambda y:y.strip(),x[1:]))),map(lambda x:x.strip().split(','), field_file.readlines()))

