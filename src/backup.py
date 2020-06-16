

'''
try:

    language = 'bn'
    print("TEXT : - "+r.recognize_google(audio , language= 'bn-IN'));
    str=r.recognize_google(audio , language= 'bn-IN')
    if str=='ডাটা সেভ করো':
        print('save data')
    myobj = gTTS(text='আপনি কি এটা বলতে চাইছেন '+str, lang=language, slow=False)

    myobj.save("welcome.mp3")

    # Playing the converted file
    os.system("mpg321 welcome.mp3")
    playsound.playsound('welcome.mp3',True)
except:
    pass;
'''