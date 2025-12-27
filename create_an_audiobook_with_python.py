from PyPDF2 import PdfReader
import pyttsx3

reader = PdfReader("file.pdf")

speaker = pyttsx3.init()

full_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        full_text += text
        speaker.say(text)
        speaker.runAndWait()

speaker.save_to_file(full_text, 'audio.mp3')
speaker.runAndWait()

speaker.stop()
