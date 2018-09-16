# This should just contain a dictionary of custom command names mapped to the function from the custom-commands directory
import os
import time

command_map = {
    'delay': lambda arg: time.sleep(int(arg[0])),

}

python_command_map = {
    'cd': os.chdir
}