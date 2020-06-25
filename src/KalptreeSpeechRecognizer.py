#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from flask import Flask
from flask import request ,session
from flask import render_template
import os
import speech_recognition as sr
import playsound
from gtts import gTTS
import os
#import pyaudio
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from flask import jsonify

#nltk.download('all')
from requests import Session

app = Flask(__name__)
app.secret_key=("DG123") ## unique identifier for cookies will be identified by the Flask
text_tag_arr=[]
def speech_analysis(text):
    tokenized_word = word_tokenize(text)
    print(tokenized_word)

    fdist = FreqDist(tokenized_word)
    print(fdist)
    print(fdist.most_common(6))

    stop_words = set(stopwords.words("english"))

    meaningful_words = [w for w in tokenized_word if not w in stop_words]

    more_exclusion= {' I ',' i ','me ','myself ','us ','our ','you ', 'yourselves ' , 'yourself ','your ','he' ,'himself ','her ','herself ' , 'problem'
                     ,' they','themselves ', 'mine ', 'thier' ,'there '}

    more_meaningful_words = [w for w in meaningful_words if not w.lower() in more_exclusion]

    filtered_sent = []
    for w in tokenized_word:
        if (w not in stop_words) & (w.lower() not in more_exclusion)& (w!='I'):
            filtered_sent.append(w)
    print("Tokenized Sentence:", tokenized_word)
    print("Filterd Sentence:", filtered_sent)

    print("meaningful_words:", more_meaningful_words)

    unique_filtered_sent = []
    for x in filtered_sent:
        if x not in unique_filtered_sent:
            unique_filtered_sent.append(x)
    print('unique_filtered_sent: ',unique_filtered_sent)

    ps = PorterStemmer()

    stemmed_words = []
    for w in filtered_sent:
        stemmed_words.append(ps.stem(w))

    print("Filtered Sentence:", filtered_sent)
    print("Stemmed Sentence:", stemmed_words)


    lem = WordNetLemmatizer()


    lematized_words = []
    for w in filtered_sent:
        lem.lemmatize(w, "v")
    print("lematized_words:", lematized_words)

    return unique_filtered_sent

def speech_analyze(filename):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.record(source)
    audio_text = r.recognize_google(audio, language='en-US')
    print('audio_text:-  ',audio_text)

    text_tag_arr=speech_analysis(audio_text)
    print('text_tag_arr',text_tag_arr)
    session['tags'] =text_tag_arr
    final_tags=''
    for tag in  text_tag_arr:
        final_tags=final_tags+" and "+tag

    print('final tags - > ',final_tags)
    language = 'en-US'
    myobj = gTTS(text='Your problem mainly concerns with '+final_tags , lang=language, slow=False)

    myobj.save("welcome.mp3")

    # Playing the converted file
    os.system("mpg321 welcome.mp3")
    playsound.playsound('welcome.mp3', True)
    os.remove("welcome.mp3")

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        #language_chosen=request.files['language']
        #print(' xxdg language',language_chosen)
        print(' request.files ',request)
        target = os.path.join(os.getcwd(), "templates")
        destination = os.path.join(target, 'Kalptree_problem.wav')
           # destination = os.path.join(target, audio.name)'')
        with open(destination, 'wb') as audio:


            destination = os.path.join(target, audio.name)
            f.save(destination)

        speech_analyze(destination)
        print('file uploaded successfully')
        #os.remove("Kalptree_problem.wav")
        return render_template("index.html", results=session['tags'])
    else:
        return render_template("index.html")
@app.route('/Problem_result')
def Problem_result():
    print(" in results",session['tags'])
    return jsonify(session['tags'])
    #return session['tags']
    #return render_template("Problem_result.html", results=session['tags'])
if __name__ == "__main__":
    app.run(debug=True,port=5020)
    #app.run(host="0.0.0.0",port=5002)