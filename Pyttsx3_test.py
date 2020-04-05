import pyttsx3

engine = pyttsx3.init()  # object creation

voices = engine.getProperty('voices')
engine.setProperty('rate', 150)         # voice rate
for voice in voices:
    engine.setProperty('volume',.9)     # volume level 0 to 1
    engine.setProperty('voice', voice.id)   # 2 type of voice male and female
    engine.say("Welcome to Voice Assistant Project")

engine.runAndWait()

engine.stop()



########################## Details #################

###### RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print ('Speaking rate: ',rate)      #printing current voice rate
engine.setProperty('rate', 130)     # setting up new voice rate

####### VOLUME
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print ('Sound level: ',volume)                          #printing current volume level
engine.setProperty('volume',.6)    # setting up volume level  between 0 and 1

###### VOICE
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()
