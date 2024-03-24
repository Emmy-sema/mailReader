import pyttsx3
def voice(text):
    engine = pyttsx3.init()
    file = text.split(" ")[0]+'.mp3'
    engine.save_to_file(text,file)
    engine.runAndWait()
    return file

