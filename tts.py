import pyttsx3 as tts

engine = tts.init()
print("gib die Geschwindigkeit der stimme  ein")
a = input()
engine.setProperty('rate', a)

print("gib deinen text ein")

x = input()

print("gib den Namen ein")
y = input()


def speak(xt):
    engine.say(xt)
    engine.save_to_file(x,y)
    engine.runAndWait()


speak(x)
