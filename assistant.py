import pyaudio
import random
import os
import pyttsx3
import webbrowser
import pyautogui
import speech_recognition as sr
engine = pyttsx3.init()

def speak(text):
     engine.say(text)
     engine.runAndWait()

def listen():
     while True:
          r = sr.Recognizer()
          with sr.Microphone() as source:
               audio = r.listen(source)
                    
          try:
               return r.recognize_google(audio)
               
          except sr.UnknownValueError:
               print('Could not understand audio')
               
          except sr.RequestError as e:
               print("Could not request results;{0}".format(e))
          return ""

	
#==================================== Keyborad & Mouse ===============================

def close():
     speak("Ok sir")
     pyautogui.hotkey("alt","f4")
def back():
     speak("got it sir")
     pyautogui.hotkey("alt","left")
def font():
     speak("ok sir")
     pyautogui.hotkey("alt","right")
def font_tab():
     speak("Ok sir")
     pyautogui.hotkey("ctrl","tab")
def new_tab():
     speak("ok sir")
     pyautogui.hotkey("ctrl","t")
def fullscreen():
     speak("ok sir")
     pyautogui.hotkey("f")
def ok():
     speak("ok sir")
     pyautogui.hotkey("enter")
def com_sys():
     speak("ok sir")
     pyautogui.hotkey("winleft","pause")
def mouse():
     speak("ok sir")
     speak("what do you want to you sir")
     d = listen()
     print(d)
     if d in ['left click video one','play video one','play one','left clip video one']:
          pyautogui.click(596,262, duration=0.50)
     elif d in ['left click video to','play video to','play 2','left click play 2']:
          pyautogui.click(638,404, duration=0.50)
     elif d in ['left click video 3','play video 3','play 3','left click play 3','left clip video 3']:
          pyautogui.click(638,552, duration=0.50)
     elif d in ['left click video for','left click play 4','play 4']:
          pyautogui.click(643,708, duration=0.50)
     elif d in ['left click video 5','left click play 5','play 5','left click video five']:
          pyautogui.click(622,868, duration=0.50)
     elif d in ['left click video sex','left click video six','play 6']:
          pyautogui.click(616,1000, duration=0.50)
     elif d in ['left click home','home']:
          pyautogui.click(82,149, duration=1)
     elif d in ['left click history','history']:
          pyautogui.click(99,317, duration=1)
     elif d in ['left click youtube','youtube']:
          pyautogui.click(128,92, duration=1)
     elif d in ['left click subscriptions','subscriptions']:
          pyautogui.click(127,226, duration=1)
     elif d in ['middle click video one','mediklick video one','middle click video one']:
          pyautogui.middleClick(596,262,duration=0.50)
          pyautogui.hotkey("ctrl","tab")
     elif d in ['middle click video to','mediklick video to']:
          pyautogui.middleClick(638,404,duration=0.50)
          pyautogui.hotkey("ctrl","tab")
     elif d in ['middle click video 3','middle clip video 3','mediklick video 3']:
          pyautogui.click(638,552, duration=0.45)
          pyautogui.hotkey("ctrl","tab")
     elif d in ['middle click video for','mediklick video for','middle click video 4']:
          pyautogui.click(643,708, duration=0.45)
          pyautogui.hotkey("ctrl","tab")
     elif d in ['middle click video 5','middle click video file','middle clip video 5','middle click five']:
          pyautogui.click(622,868, duration=0.54)
          pyautogui.hotkey("ctrl","tab")
     elif d in ['middle click video six','middle click video sex','middle clip video sex']:
          pyautogui.click(616,1000, duration=0.30)
          pyautogui.hotkey("ctrl","tab")
     elif d in 'middle click home':
          pyautogui.click(82,149, duration=0.50)
          pyautogui.hotkey("ctrl","tab")
     elif d in 'middle click history':
          pyautogui.click(99,317, duration=1)
          pyautogui.hotkey("ctrl","tab")
     elif d in 'middle click youtube':
          pyautogui.click(128,92, duration=1)
          pyautogui.hotkey("ctrl","tab")
     else:
          speak('you used worng word')
          speak("try again next time")
     
#================================== Online ==========================================

def search():
     speak("yes sir")
     speak('starting all system applications')
     speak('ok sir i am go in online for you')
     speak("what do you want to search")
     new =2
     tabUrl="http://google.com/?#q=";
     term= listen()
     speak('ok sir searching' + term + 'for you')
     webbrowser.open(tabUrl+term,new = new);
def youtube():
     speak('good choice')
     speak("what do you want to search")
     new =2
     tabUrl="https://www.youtube.com/results?search_query=";
     term= listen()
     speak('ok sir going' + term + 'for you')
     webbrowser.open(tabUrl+term,new = new);

def music():
     speak('ok sir')
     speak('starting required application')
     speak('Oh sorry sir, you do not have any audio music in your system')
     speak('no problem sir, i am going in online for you')
     speak('Please wait for a moment')
     speak('oohh yes,i found a good music website for you')
     webbrowser.open("https://gaana.com")
     speak('I wish you like this website')
     
#     c =listen()
#     speak('ok sir playing' + c + 'for you')
#     os.startfile('I:/Music/'+c+'.mp3')
#     speak('Please wait for a moment')

def video():
     speak('good choice sir')
     speak('starting required application')
     speak('Ooohh sorry sir, you do not have any video music in your system')
     speak('no problem sir, i am going in online for you')
     speak('Please wait for a moment')
     speak('oohh yes,i found some good online video music website for you')
     speak('Please, what kind of video music do you want to listen to?')
     speak('1 Bangla')
     speak('2 English')
     speak('3 Hindi')
     speak('4 Do you want to search manually?')
     web = listen()
     if web in ['1', 'Bangla']:
          speak('good choice')
          webbrowser.open("http://www.bongobd.com")
          speak('I wish you like this site')

     elif web in ['2','Tu', 'English']:
          speak('good choice')
          speak('I have found two best online english video music websites')
          a = random.choice([webbrowser.open("https://www.godtube.com/music-videos/"),
                       webbrowser.open("http://www.dailymotion.com/en/channel/music")])
          print(a)
          speak('I wish you like this website')
     elif web in ['3','Hindi']:
          speak('good choice')
          speak('I have found two best online hindi video music websites')
          b = random.choice([webbrowser.open("http://www.ozee.com/music"),
                       webbrowser.open("https://www.funmaza.in")])
          print(b)
     elif web == 'manual':
          speak('ok sir')
          speak("what do you want to search")
          new = 2
          tabUrl = "http://google.com/?#q=";
          y = listen()
          speak('ok sir searching' + y + 'for you');
     else:
          speak("sorry sir,i have found some issue")
          speak("please try again")
def dnd():
     speak('please say this again ?')
     r = sr.Recognizer()
     audio = r.listen(source)
     l = r.recognize_google(audio)
     print(l)
     speak('ok sir')
     speak('if you like' +l+ 'serching for my website')
     speak('say yes')
     speak('or you like to serching google')
     speak('then say no')
     while True:
          d = listen()
          if d == 'yes':
               speak('good choice')
               os.startfile('J:/arvan/HTML/download site/website.html')
               speak('i wish you like this website')
               break
          elif d == 'no':
               speak('ok sir')
               a = l
               tabUrl="http://google.com/?#q=";
               webbrowser.open(tabUrl+a,new = new);
               speak('ok sir searching google' + a + 'for you')
               break
          #elif d == manual:
               #speak('ok sir')
               #speak("what do you want to search")
               #new = 2
               #tabUrl = "http://google.com/?#q=";
               #y = listen()
               #speak('ok sir searching' + y + 'for you');
               #break
          #elif d == back:
               #speak('got it sir')
               #break
          else:
               speak('you use some worng word')
               speak('Talk correctly')
               speak('try again')
               continue
     

#     speak('what do you want me to play for you')
#     k = listen()
#     speak('ok sir playing' + k + 'for you')
#     speak('Please wait for a moment')
#     os.startfile('g:/'+k+'.mp4')

#================================== Offline ==============================================

def python():
     speak("ok sir")
     os.system('start python.exe')

def arvan():
     speak("Arvan Bishwas founded me in 2017,9 september, while he was a collage student.")
     speak("He is a student of  Computer Science and Engineering.")
     speak("He was born in 9 February 1999")
     speak("he born from a ordinary family in bangladesh.")
def Luffy():
     speak('yes sir')
def thanks():
     speak('anything for you')
def FN():
     speak("My Founder is Arvan Bishwas.")
def hi():
     d = random.choice(['hey','good morning','hi','sub'])
     speak(d)
def tks():
     g = random.choice(['you are most walcome','you are walcome'])
     speak(g)
def do_for_me():
     speak('oohh good')
     speak('you ask me very good question')
     speak('I can make your life easier and interest.')
     speak('And i am very intelligent and friendly.')
     speak('i have solve any mathematical problem.')
     speak('In a moment.')
     
def read():
     speak("ok sir")
     speak("what do you want to read")
     d = pyautogui.hotkey("ctrl","a")
     speak(d)

#def online():
#     speak('ok sir')
#     speak('starting all system applications')
#     speak('installing all drivers')
#     os.system('k:/Python/Rainmeter.exe')
#     speak('ok sir i am go in online for you')
#     speak('every driver is insalled')
#     speak('all systems have been started')
#     speak('now i am online sir')

def shutdown():
     speak('understood sir')
     speak('connecting to command prompt')
     speak('shutting down your computer')
     os.startfile('shutdown -s')
     
#===================================== mainfunction ======================================
     
def mainfunction(source):
     r = sr.Recognizer()
     audio = r.listen(source)
     user = r.recognize_google(audio)
     print(user)

#------------------------------------ User Argument -----------------------------------------------------------------------------------------------------------------------

     a =['download','I need to download software', 'I need software', 'free software download','software','online software','online software download','offline software',
         'offline software download','worldest best software download','toppest software','top 10 software all time','top 10 software','top 10 software in 2017',
         'any software download',
          'movies download','download movies','I need to download movies','I need movies','free movies download','movies', 'online movies','online movies download',
         'offline movies', 'offline movies download','worldest best movies download','toppest movies','top 10 movies all time','top 10 movies','top 10 movies in 2017',
         'any movies download']
     b = ["open online","go online","Online","go to online"]
     c = ["YouTube","open YouTube","go to YouTube","go YouTube"]
     d = ["open mouse","mouse pad","Mouse"]
     e = ["font tab","go to font tab"]
     f = ["music","open music","go to music"]
     g = ["open video song","video music","video"]
     h = ["close tab","close the tab"]
     i = ["back","come back"]
     j = ["go to font","forward"]
     k = ["open new tab","new tab"]
     l = ["tell me about your founder","about your founder","something tell me about your founder"]
     m = "who is your founder"
     n = ["details of my computer","basic information about my pc","basic information about my computer",
		  "information about my computer","computer information","computer system","windows system"]
     o = "shutdown"
     p = ['hi','hey','whatsup','sub','good morning']
     q = 'thank you'
     u = "Luffy"
     r = "thanks"
     s = "Read"
     t = "ok"
     v = "full screen"
     w = ["what you do for me","what to do for me"]
     
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
     
     if user in a:
          dnd()
     elif user in b:
          search()
     elif user in c:
          youtube()
     elif user in d:
          mouse()
     elif user in e:
          font_tab()
     elif user in f:
          music()
     elif user in g:
          video()
     elif user in h:
          close()
     elif user in i:
          back()
     elif user in j:
          font()
     elif user in k:
          new_tab()
     elif user in l:
          arvan()
     elif user == m:
          FN()
     elif user in n:
          com_sys()
     elif user == o:
          shutdown()
     elif user in p:
          hi()
     elif user in q:
          tks()
     elif user == u:
          Luffy()
     elif user == r:
          thanks()
     elif user == s:
          read()
     elif user == t:
          ok()
     elif user == v:
          fullscreen()
     elif user in w:
          do_for_me()
     
     else:
          speak('sorry sir')
          speak('I do not have the answer')
          speak('so,i ame going online')
          new =2
          a = user
          tabUrl="http://google.com/?#q=";
          speak('ok sir searching' + a + 'for you')
          webbrowser.open(tabUrl+a,new = new);

speak('hello sir')
speak('What kind help for you')





if __name__== "__main__":
     r = sr.Recognizer()
     with sr.Microphone() as source:
          while 1:
               mainfunction(source)



