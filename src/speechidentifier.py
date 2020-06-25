from flask import Flask, Response,render_template
import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import pyaudio

r= sr.Recognizer()


with sr.Microphone() as source:
    print("say Something"  )
    r.adjust_for_ambient_noise(source,duration =1)
    #audio = r.listen(source)
    r.non_speaking_duration=0.5
    r.pause_threshold=1
    #r.energy_threshold =100
    r.dynamic_energy_threshold=True

    print("Listening");
    audio = r.listen(source)
    str = r.recognize_google(audio, language='en-US')
    #str = r.recognize_google(audio)
    print("Listened");
    str=str.replace('কমা',',')
    str = str.replace('comma ', ',')
    str=str.replace('দাড়ি','|')
    str = str.replace('fulls stop', '.')
    str=str.replace('পার্সেন্টেজ','%')
    str = str.replace('percentage', '%')

    str=str.replace('এক্সক্লামেশন','!')
    str=str.replace('বিস্ময় সূচক চিহ্ন','!')
    str=str.replace('এট দা রেট','@')
    str = str.replace('at the rate', '@')
    str = str.replace('এট দা রেট', '@')
    str = str.replace('এট দি রেট', '@')
    str = str.replace('পারসেন্ট', '%')
    str=str.replace('ফাস্ট ব্রাকেট খোলা','(')
    str = str.replace('open first bracket', '(')
    str=str.replace("ফাস্ট ব্রাকেট বন্ধ", ")")
    str = str.replace('close first bracket', '(')
    str=str.replace('সেকেন্ড ব্র্যাকেট খোলা','{')
    str = str.replace('open second bracket', '{')
    str=str.replace('close second bracket','}')
    str = str.replace('সেকেন্ড ব্র্যাকেট বন্ধ', '}')
    str= str.replace('অবলিক','\\')
    str = str.replace('oblique', '\\')
    str=str.replace('অব্লিক','\\')
    str = str.replace('অব্লিগ', '\\')
    str=str.replace('সেমিকোলন',';')
    str = str.replace('semicolon', ';')
    str=str.replace('কোলন',':')
    str = str.replace('colon', ':')
    str = str.replace('ড্যাশ', ' - ')
    str = str.replace('dash ', ' - ')
    str=str.replace('আন্ডার স্কোর','_')
    str = str.replace('under score', '_')
    str = str.replace('আন্ডারস্কোর', '_')
    str = str.replace('আন্ডারস্কোর', '_')
    str=str.replace("ইজ ইকুয়াল টু",' = ')
    str = str.replace("is equal to", ' = ')
    str = str.replace("is equals to", ' = ')
    str = str.replace(" equals to", ' = ')
    str = str.replace(" equal to", ' = ')
    str=str.replace("ইজইকুয়ালটু",' = ')
    str=str.replace("প্লাস",'+ ')
    str = str.replace(" plus ", '+ ')
    str=str.replace("মাইনাস",' - ')
    str = str.replace(" minus ", ' - ')
    str=str.replace("গুন",' * ')
    str = str.replace(" multiplication ", ' * ')
    str = str.replace(" Asterix ", ' * ')
    str=str.replace('কোট ওপেন','"')
    str = str.replace(' Quote ', '"')
    str = str.replace('কোট বন্ধ', '"')
    str = str.replace('কোড ওপেন', '"')
    str = str.replace('কোড বন্ধ', '"')
    str = str.replace('dot', '.')




    #str=str.replace()
    #str.replace('কমা', ',')
    #saved_audio= r.record(source)
    #language = 'bn'
    languag='en'
    print("TEXT : - " +str);



    ##myobj = gTTS(text='আপনি কি এটা বলতে চাইছেন ' + str, lang=language, slow=False)

    ##myobj.save("welcome.mp3")

    # Playing the converted file
    ##os.system("mpg321 welcome.mp3")
    ##playsound.playsound('welcome.mp3', True)
    #os.remove("welcome.mp3")

app = Flask(__name__)
