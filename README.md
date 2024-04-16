# readThis
Python script for reading input text using TTS (Text-to-speech pyttsx3) library and eSpeak opensource voice synth.
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
voices in script with eSpeak (you can add your own):
- Čeština 
- Slovenčina 
- English 
- Deutsch 
- Polski 
- Español 
- Français 
- Magyar 
- Italiano

also you can change parameters rate, pause, volume, pitch, modulation and emphasis in code