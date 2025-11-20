# TTS_Project
Arabic Text-To-Speech model that uses gTTS

This project demonstrates how to generate Arabic speech from text using gTTS (Google Text-to-Speech) in Python. It includes necessary installation steps, environment setup, and a complete, working example script.

Key Features
Convert Arabic text into speech.

Save the generated audio as an MP3 file (arabic_output.mp3).

Lightweight, fast, and simple implementation.

Uses the Google TTS API for excellent Arabic language support.

Prerequisites
To run this project, you will need the following tools and environment setup:

Operating System: Windows 10 / 11.

Programming Language: Python 3.10.x.

Editor: Visual Studio Code (or any preferred code editor).

Build Tools: Microsoft C++ Build Tools (required for certain Python dependencies).

Installation and Setup
Follow these steps precisely to set up your environment:

Install Python 3.10

Download from: https://www.python.org/downloads/

Crucial Step: During installation, ensure you check the box: “Add Python to PATH”.

Verify installation: Open your Command Prompt and run:

Bash

python --version
Install Microsoft C++ Build Tools

Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

Select the "Desktop development with C++" workload.

Note: Restart your computer after the installation completes.

Create a Virtual Environment

Open your Command Prompt (CMD).

Navigate to your Desktop (or project folder location):

Bash

cd Desktop
Create the environment:

Bash

python -m venv tts_env
Activate Virtual Environment

Run the activation script (must use Command Prompt, not PowerShell):

Bash

tts_env\Scripts\activate
Install gTTS

Upgrade pip and install the required library:

Bash

pip install --upgrade pip
pip install gTTS
Example Script (WieAct.py)
The following code generates the Arabic audio:

Python

from gtts import gTTS
import os

text = "مرحبا، كيف حالك اليوم؟"
print("Generating Arabic speech...")
tts = gTTS(text=text, lang='ar')
tts.save("arabic_output.mp3")
print("Audio saved as 'arabic_output.mp3'")
os.startfile("arabic_output.mp3") 
Run the Script
Ensure your virtual environment is active (step 4), then execute the script:

Bash

python WieAct.py
Key Learnings
Isolation: Virtual environments are essential for isolating project dependencies.

PATH: Proper PATH configuration is crucial for running Python commands globally.

Dependencies: Some Python packages require external tools, like the Microsoft C++ Build Tools, to compile successfully.

Library Choice: gTTS was chosen over alternatives like Coqui TTS because it is lighter, simpler, more accurate for this use case, and avoids large (4GB+) model downloads and potential build failures.

Troubleshooting Notes
Activation: The virtual environment must be activated before running pip install for packages to be installed correctly.

VS Code: Ensure your VS Code interpreter setting is configured to use the Python executable inside your newly created tts_env virtual environment.

Tools Used
Python 3.10
pip
venv (for virtual environments)
gTTS
Visual Studio Code
Command Prompt

License
This project is open-source for educational purposes.
