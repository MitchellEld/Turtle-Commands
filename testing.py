
from utils import get_commands, execute_commands

req_body = ''

while req_body != 'exit' :
    req_body = input('Turtle Command$ ')

    # Check first word in body to see if it is custom command
    commands = get_commands(req_body)
    # If custom command, run function associated with it
    # If not custom command, run the body as normal os command
    output = execute_commands(commands)

    print(output)


