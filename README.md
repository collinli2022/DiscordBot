# DiscordBot
A personal discord bot that is intergrated with Raspberry Pi

#### Installation of Discord.py
1. python3 -m pip install -U discord.py

#### RPI setup
##### Auto-Shutdown
1. https://www.recantha.co.uk/blog/?p=13999
	- check your status by using this command ```sudo systemctl status gpio-halt.service```
##### Auto-Bot-Activate on startup
1. terminal
2. sudo crontab -e
3. at bottom bottom type ```@reboot sudo python3 <script location> &```
4. save

#### Explanation of files
dablitfam.json - custom commands for friends
helper.py - helps main file (makes code neater)
run.py - main file (run this to start bot)

#### Stuff I learned
- Why does on_message stop commands from working answered here: https://stackoverflow.com/questions/49331096/why-does-on-message-stop-commands-from-working
- How to change bot status: https://stackoverflow.com/questions/59126137/how-to-change-discord-py-bot-activity