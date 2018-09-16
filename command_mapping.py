# This should just contain a dictionary of custom command names mapped to the function from the custom-commands directory
import os
import time
from customCommands.files import find 

command_map = {
    'delay': lambda arg: time.sleep(int(arg[0])),
    'search': find,

}

python_command_map = {
    'cd': os.chdir
}
