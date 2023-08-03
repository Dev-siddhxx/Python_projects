import pyttsx3
import speech_recognition as sr
import datetime
import time
import webbrowser
import wikipedia
import os
import subprocess
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Hello sir iam Jarvis2.0 . plaese tell how can i help you!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon! Hello sir iam Jarvis2.0  . plaese tell how can i help you!")
    else:
        speak("Good Evening! Hello sir iam Jarvis2.0  . plaese tell how can i help you!")
        
def takeCommand():
    r = sr.Recognizer()
   
    with sr.Microphone() as source:
        print("Listening....")
      
        
        audio = r.listen(source)
    
    try:
        print("recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")




    except Exception as e:
        #print(e)


        print("Say it again plaease.")
        return"None"
    return query


    
#main thing to run the process... the order given the user to run the file ... or any other things and can be modefied according to the  needs of the user so user is free to make changesin this software .....



    print("helllo world")
if __name__ == '__main__':
    wishMe()
    while True:
        
       query = takeCommand().lower()
       if 'wikipedia' in query:
           speak('Searching Wikipedia....')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)#number of sentensein wekepidia
           speak("According to wikipedia")
           print(results)
           speak(results)
# i can add numerus website i want...

       elif "open youtube" in query:
            speak("opening youtube wait a minute sir.")
            webbrowser.open("youtube.com")


       elif "open google" in query:
            speak("opening google wait a minute sir.")
            webbrowser.open("google.com")


       elif "open instagram" in query:
            speak("opening instagram wait a minute sir.")
            webbrowser.open("instagram.com")
        


       elif "open whatsapp" in query:
            speak("opening whatsapp wait a minute sir.")
            webbrowser.open("whatsapp.com")


       elif "open eclipse" in query:
            speak("opening eclipse please wait a minute sir")
            eclipse = 'C:\\Users\\biswa\\eclipse\\java-2022-06\\eclipse\\eclipse.exe'
            os.startfile(eclipse)


       elif "open photoshop" in query:
            speak("opening photoshop type please wait a minute sir")
            monkey = "C:\\Program Files (x86)\\Adobe\\Photoshop 7.0\\Photoshop.exe"
            os.startfile(monkey)
       elif "i want to code" in query:
            speak("opening your favourite visual studio code please wait a minute sir")
            code = "C:\\Users\\biswa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
       
       elif "lets start studying" in query:
           speak("Wait a minute analysing your studing modules...")
           webbrowser.open("www.google.com")#here i have to add my studing website to open automatically
           speak("according to me sir you are quite well in physics and according to my data analysement you need to focus in hindi, grammer, history..... sir accoring to that you can easily score good marks in Boards . if you want ican also download to pre hacked pdf for them......")
           speak("playing some nice music to concentrate in studies... ")
           webbrowser.open("www.spotify.com")
           speak("NOW CONCENTRATE IN THE STUDIE SIR..........")



       elif "who created you" in query:
           speak("I am proud to answer this question , iam jarvis 2.0 created by Sai siddhartha Maharana who is 15 years old and studies in National english School he just being promoted to class 10 and is a hacker........ ")
              


       elif "tell something about you" in query:
           
           speak("iam jarvis 2.0 an automate artifical intelligence created by sai siddhath maharana . i have many features which are being give to me by my master siddharth sir . some funtionality include , 1. auto web opening ,2. auto data analysing ,3. wifi hacking , 4. Virtual mode assistant , 5. auto app manage ment which means i can open any app you want from your device , 6. Artifical inteligent environment for studing , personal talking assistant which means one can talk with me freely.. and many more .....   ")

       elif "wait for 1 minute" in query:
           speak("Waiting for 1 minute sir")
           for pause_in_secound in [60]:
                time.sleep(pause_in_secound)
                
       elif "wait for 2 minute" in query:
           speak("Waiting for 2 minutes sir")
           for pause_in_secound in [120]:
                time.sleep(pause_in_secound) 

       elif "tell something about me" in query:
           speak("You are Sai Siddharth Maharana Son of Biswajit And Sabita Maharana and you are the person who created me, so thanks sir. Your dream in life is to become a software enginner and a multi millonare by stock time investment .... your aim in the life is to serve your parents who create you, according to your thinking parents are the one who are nothing but forms of god so it is our responsibility to serve them well in future , sir... you have only one loyal friend who is Adrija das......who studies in sent stephens high school and you call her topper ji...")
           speak("You are also Music lover. The only person you follow in this life is thomas shelby and your parents . except there is no one in this world whome you copy ...ok sir this is all about your information.......")
            

       elif "open chat gpt" in query:
            speak("Opening chat Gpt wait a minute sir.")
            webbrowser.open("https://chat.openai.com/chat")


       elif "play music" in query:
            speak("playing your music directory sir..")
            music_dir = 'C:\\Users\\biswa\\OneDrive\\Documents\\Music_jarvis'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[0]))


       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H"":""%M"":""%S")
           speak(f"Sir, the time is {strTime}")


       elif "now you can go" in query:
           speak("Thanks for choosing me sir i hope i serve you well, bye sir.")
           break

       elif "turn on wi-fi cracker" in query:

           speak("turning on wifi hacker trojan created by you please wait .......")
           print("turning on wifi hacker trojan created by you please wait .......")
           for pause_in_secound in [3]:
                time.sleep(pause_in_secound)
           
            
           speak("Checking utilities.....") 
           print("Checking utilities.....")
           for pause_in_secound in [3]:
                time.sleep(pause_in_secound)
            #sleep fun 3 sec


           speak("everything satisfied ......")
           print("everything satisfied ......")
           for pause_in_secound in [3]:
                time.sleep(pause_in_secound)

              #sleep fun 3 sec

           speak("turning on php services....")   
           print("turning on php services....")
           for pause_in_secound in [3]:
                time.sleep(pause_in_secound)
                 #sleep fun 2 sec
           speak("wait a minute cracking your nearest password.......")
           print("wait a minute cracking your nearest password.......")
           for pause_in_secound in [3]:
                time.sleep(pause_in_secound)
           data = subprocess.check_output(
           ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
           profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

           for i in profiles:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,
                                    'key=clear']).decode('utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                   print("{:<30}| {:<}".format(i, results[0]))
                except IndexError:
                    print("{:<30}| {:<}".format(i, ""))


            
          
    
       
   


