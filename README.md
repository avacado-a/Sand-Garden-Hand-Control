# Sand-Garden-Hand-Control
1. Go to the Crunchlabs Sand Garden Hack Pack IDE
2. Set the level to level 3 on the IDE
3. Copy the code from the *HandControlArduinoCode.ino* file here on GitHub, and paste it into the IDE
4. Make sure your sand garden is plugged into your computer, and is plugged into power. If your confused, look at the image below:
<img width="1435" height="1075" alt="Screenshot_2025-02-14_201744" src="https://github.com/user-attachments/assets/30efc803-2a76-411a-8356-d9beb3ad7bd0" /> 
5. Upload the code from the IDE to the Sand Garden
6. Download all of the python files to your computer.
7. Go into your terminal
8. Run the command: 
```bash
cd Downloads
python liveDrawDir.py
```
9. You should see a window pop up that looks just like the one in the video on Discord
10. Follow what I do in the video and it should all work

Note on Windows
On Windows, it may not work due to interference with the crunchlabs-arduino-create-agent. In order to disable this you should:
1. Before doing step 8, open Task Manager.
2. In the search bar, search for 'crunchlabs'
3. If you see crunchlabs-arduino-create-agent (or something similar), click on it
4. Then click end task on the top right corner of Task Manager
5. Now, you can proceed with steps 8-10
6. If it still doesn't work, ask on Discord for help

After running this hack, you will want to run crunchlabs-arduino-create-agent again. 
Follow the instructions <a href="https://ide.crunchlabs.com/assets/downloads/windows/crunchlabs-arduino-create-agent-Setup-1.0.1.exe">here</a> to re-enable it
