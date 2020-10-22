  
import time
 
# Wait for 10 seconds
time.sleep(5)

import os

# python3 /home/pi/Desktop/DiscordBot/run.py &
sudoPassword = 'pi'
#command1 = 'sudo systemctl status gpio-halt.service'
command2 = 'python3 /home/pi/Desktop/DiscordBot/daBot.py'
#os.system('echo %s|sudo -S %s' % (sudoPassword, command1))
os.system('echo %s|sudo -S %s' % (sudoPassword, command2))
print('done')