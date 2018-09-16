import os

def find(commandStrings):
    name = commandStrings[0]
    path = os.getcwd()
    return "test"
    #for root, dirs, files in os.walk(path):
        #if name in files:
            #return "test"
            #return os.path.join(root, name)
