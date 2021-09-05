import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia 
import smtplib 
import webbrowser as wb 
engine = pyttsx3.init()
'''voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current Time is")
    speak(Time)
#time()

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The current Date is")
    speak(date)
    speak(month)
    speak(year)
#date()

def wishme():
    speak("welcome back!")
   
    hour=datetime.datetime.now().hour

    if hour>= 6 and hour< 12:
        speak("Good morning")
    elif hour>= 12 and hour< 18:
        speak("Good afternoon")
    elif hour>= 18 and hour<= 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Ramu at your service. How can i help you?")
#wishme()

def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language ="en-in")
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say That again please.....")
        return "None"

    return query
#takeCommand()

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("jnishita.nj@gmail.com", "1395dnishita")
    server.sendmail("en19cs301227@medicaps.ac.in",to,content)
    server.close()

if __name__ == "__main__":

    wishme()

    while True:
          query = takeCommand().lower()
          print(query)

          if "time" in query:
              time()
          elif "date" in query:
              date()
          elif "offline"  in query:
              quit()  
          elif "wikipedia" in query:
              speak("Searching..")   
              query = query.replace("wikipedia","")
              result = wikipedia.summary(query,sentences = 2)
              speak(result)
         # elif  "send email"  in query:
              #try:
                  #speak("What should I say?")
                  #content = takeCommand()
                  #to ="en19cs301227@medicaps.ac.in"
                  #sendmail(to,content)
                  #speak("Email sent successfully")
              #except Exception as e:
                  #speak(e)   
                  #speak("Unable to send the message")
          elif "search in chrome" in query:
               speak ("What should I search?")    
               chromepath = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
               search = takeCommand().lower()
               wb.get(chromepath).open_new_tab(search + ".com")
         #elif 'open youtube' in query:
              #wb.open("youtube.com")

