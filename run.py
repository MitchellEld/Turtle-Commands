import subprocess
import os
from setup.config import FLASK_PORT

try:
    subprocess.run(['pip','install','-r','requirements.txt'])
    d = dict(os.environ)
    d['FLASK_APP'] = 'server.py'
    subprocess.Popen(['flask', 'run','--port={}'.format(FLASK_PORT)], env=d)
    subprocess.run(['python3', 'messaging_wrappers/slack.py'])
    # The following will normally not do anything. If the flask server for some reason does not close, this will close it
    # pid = subprocess.check_output(['lsof', '-i', ':5000', '|', 'awk', '{if (NR==2) {print $2}}'])
    # subprocess.run(['kill',pid])
except:
    print('Servers stopped')