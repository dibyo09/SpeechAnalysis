from flask import Flask, Response,render_template
import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import pyaudio

r= sr.Recognizer()


with sr.Microphone() as source:
    print("say Something"
          )
    r.adjust_for_ambient_noise(source,duration =1)
    #audio = r.listen(source)
    r.non_speaking_duration=0.5
    r.pause_threshold=1
    #r.energy_threshold =100
    r.dynamic_energy_threshold=True
    audio= r.listen(source)

    str = r.recognize_google(audio, language='bn-IN')

    str=str.replace('কমা',',')
    str=str.replace('দাড়ি','|')
    str=str.replace('পার্সেন্টেজ','%')
    str=str.replace('এক্সক্লামেশন','!')
    str=str.replace('বিস্ময় সূচক চিহ্ন','!')
    str=str.replace('এট দা রেট','@')
    str = str.replace('এট দা রেট', '@')
    str = str.replace('এট দি রেট', '@')
    str = str.replace('পারসেন্ট', '%')
    str=str.replace('ফাস্ট প্যাকেট খোলা','(')
    str=str.replace("ফাস্ট ব্রাকেট বন্ধ", ")")

    str=str.replace('সেকেন্ড ব্র্যাকেট খোলা','{')
    str=str.replace('সেকেন্ড ব্র্যাকেট বন্ধ','}')
    str= str.replace('অবলিক','\\')
    str=str.replace('অব্লিক','\\')
    str = str.replace('অব্লিগ', '\\')
    str=str.replace('সেমিকোলন',';')
    str=str.replace('কোলন',':')
    str = str.replace('ড্যাশ', ' - ')
    str=str.replace('আন্ডার স্কোর','_')
    str = str.replace('আন্ডারস্কোর', '_')
    str = str.replace('আন্ডারস্কোর', '_')
    str=str.replace("ইজ ইকুয়াল টু",' = ')
    str=str.replace("ইজইকুয়ালটু",' = ')
    str=str.replace("প্লাস",'+ ')
    str=str.replace("মাইনাস",' - ')
    str=str.replace("গুন",' * ')
    str=str.replace('কোট ওপেন','"')
    str = str.replace('কোট বন্ধ', '"')
    str = str.replace('কোড ওপেন', '"')
    str = str.replace('কোড বন্ধ', '"')




    #str=str.replace()
    #str.replace('কমা', ',')
    #saved_audio= r.record(source)
    language = 'bn'
    print("TEXT : - " +str);



    ##myobj = gTTS(text='আপনি কি এটা বলতে চাইছেন ' + str, lang=language, slow=False)

    ##myobj.save("welcome.mp3")

    # Playing the converted file
    ##os.system("mpg321 welcome.mp3")
    ##playsound.playsound('welcome.mp3', True)
    #os.remove("welcome.mp3")

app = Flask(__name__)


FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5


audio1 = pyaudio.PyAudio()

def genHeader(sampleRate, bitsPerSample, channels):
    datasize = 2000*10**6
    o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
    o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
    o += bytes("WAVE",'ascii')                                              # (4byte) File type
    o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
    o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
    o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
    o += (channels).to_bytes(2,'little')                                    # (2byte)
    o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
    o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
    o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
    o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
    o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
    o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
    return o

@app.route('/audio')
def audio():
    # start Recording
    def sound():

        CHUNK = 1024
        sampleRate = 44100
        bitsPerSample = 16
        channels = 2
        wav_header = genHeader(sampleRate, bitsPerSample, channels)

        stream = audio1.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,input_device_index=1,
                        frames_per_buffer=CHUNK)
        print("recording...")
        #frames = []
        first_run = True
        while True:
           if first_run:
               data = wav_header + stream.read(CHUNK)
               first_run = False
           else:
               data = stream.read(CHUNK)
               print('xxxddddddddddddddgggg')
               print(type(data))
           #yield(data)


    return Response(sound())
    #return render_template('success.html')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

#if __name__ == "__main__":
 #app.run(debug=True, port=5020)

