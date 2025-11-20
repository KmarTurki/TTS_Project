from gtts import gTTS
import os

# Arabic text to convert to speech
text = "مرحبا، كيف حالك اليوم؟"

# Generate speech
print("Generating Arabic speech...")
tts = gTTS(text=text, lang='ar')

# Save to file
tts.save("arabic_output.mp3")
print("Audio saved as 'arabic_output.mp3'")

# Play the audio file
os.startfile("arabic_output.mp3")