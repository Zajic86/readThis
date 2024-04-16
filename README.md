# readThis
Python script for reading input text using pyttsx3 and gTTS
## Install & run
``` bash
git clone https://github.com/Zajic86/readThis.git
cd readThis
pip install -r requirements.txt
python readThis.py
``` 
If you don't have any Text-To-Speech engine installed, try eSpeak for example
``` bash
sudo apt install espeak
``` 
voices in script with eSpeak (you can add your own, just uncomment list of voices):
- Čeština 
- Slovenčina 
- English 
- Deutsch 
- Polski 
- Español 
- Français 
- Magyar 
- Italiano

more voices of eSpeak - https://github.com/espeak-ng/espeak-ng/blob/master/docs/languages.md

also you can change parameters rate, pause, volume, pitch, modulation and emphasis in code