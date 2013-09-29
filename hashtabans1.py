#!/usr/bin/python

symbtoip = {}			#hash table or dictionary to store symbolic address to ip mapping

def addtotrie(filename):
    f = open(filename , "r")
    data = f.readlines()
    for line in data:
        key, value = line.split(";")
        #print "key: ",key,"value:",value
        symbtoip[key] = value
    f.close()
    
def looktrie(symbolic_name):
    #print "inside looktrie: ", symbolic_name
    print symbtoip[symbolic_name]

def main():
    
    while True:
        userinput = raw_input('Please enter the command.Type quit to quit..\n')
        if userinput == "quit":
            break
        else:
            command, param = userinput.split(" ")
            if command == "Dnsinput":
                addtotrie(param)
            elif command == "GetIPAddress":
                looktrie(param)
        
main()
