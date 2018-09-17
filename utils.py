import subprocess as sp
from pathlib import Path
from command_mapping import command_map, python_command_map
from messaging_wrappers.slack import responseMessage

HOME_PATH = str(Path.home())

def get_commands(commands_str):
    commands = []
    commands_str = commands_str.replace('~',HOME_PATH)
    bulk_commands = commands_str.split('; ')
    while '' in bulk_commands:
        bulk_commands.remove('')
    for bulk_command in bulk_commands:
        command = bulk_command.split(' ')
        while '' in command:
            command.remove('')
        commands.append(command)
    return commands

def execute_commands(commands, channel):
    output = ''
    for command in commands:
        try:
            if command[0] in command_map:
                output += command_map[command[0]](command[1:])
            elif command[0] in python_command_map:
                python_command_map[command[0]](' '.join(command[1:]))
            else:
                output += str(sp.check_output(command),'utf-8')+'\n'
        except Exception as e:
            output += '{} command failed\n'.format(command[0])
            #output += repr(e) + '\n'
    responseMessage(output, channel)
