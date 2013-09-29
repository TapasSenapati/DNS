#!/usr/bin/python
import trie

symbtoip = trie.Trie()			#trie to store symbolic address to ip mapping
iptomac = trie.Trie()			#trie to store ip to mac address mapping

def addtotrie(filename):
    f = open(filename , "r")
    data = f.readlines()
    for line in data:
        key, value1, value2 = line.split(";")
        #print "key: ",key,"value:",value
        symbtoip.add(key, value1)
        iptomac.add(value1, value2)
    f.close()
    
def looktrie1(symbolic_name):
    print symbtoip.lookup(symbolic_name)

def looktrie2(symbolic_name):
    print iptomac.lookup(symbolic_name)


def main():
    
    while True:
        userinput = raw_input('Please enter the command.Type quit to quit..\n')
        if userinput == "quit":
            break
        else:
            command, param = userinput.split(" ")
            if command == "ARPinput":
                addtotrie(param)
            elif command == "GetIPAddress":
                looktrie1(param)
            elif command == "GetARPAddress":
                looktrie2(param)
        
main()
