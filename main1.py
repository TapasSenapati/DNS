#!/usr/bin/python
import trie
import sys
import trie

symbtoip = trie.Trie()			#trie to store symbolic address to ip mapping

def addtotrie(filename):
    f = open(filename , "r")
    data = f.readlines()
    for line in data:
        key, value = line.split(";")
        #print "key: ",key,"value:",value
        symbtoip.add(key, value)
    f.close()
    
def looktrie(symbolic_name):
    #print "inside looktrie: ", symbolic_name
    print symbtoip.lookup(symbolic_name)

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
