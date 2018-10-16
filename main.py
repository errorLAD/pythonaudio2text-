import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('say something')
    audio = r.listen(source)
try: print('abhishek thiks u said:\n' + r.recognize_google(audio))

except:
    pass