import speech_recognition as sr
import pyttsx3
import spacy

r = sr.Recognizer()

def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

def nlp():
    i = 1
    while(i):   
        i = 0
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print("Did you say ",MyText)
                SpeakText(MyText)
                return MyText
             
        except sr.RequestError as e:
            return("")
         
        except sr.UnknownValueError:
            return("")

def key(inp):
    nlp = spacy.load("en_core_web_sm")
    text = inp
    doc = nlp(text)
    l = list(doc)
    """
    for i in range(0,len(l)+1):
        l[i] = l[i].lower()
    """
    return l

if __name__ == "__main__":
    l = []
    text = input("String: ")
    l = key(text)
    print(l)

    while len(l) > 1:
        temp = []
        t = nlp()
        if t != "":
            temp = key(t)
            print(temp)
            n = len(temp)
            while n > 1:
                if temp[0] == l[0]:
                    del_item = temp.pop(0)
                    n -= 1
                else:
                    SpeakText(l[0]) 
                del l[0]
                print(l , temp)               
    print("End")