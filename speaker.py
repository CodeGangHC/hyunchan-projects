import time
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

import requests
from bs4 import BeautifulSoup
from datetime import datetime

current_time = datetime.now()
# url lists:
weather_url = "https://weather.com/weather/today/l/de8c78996a73470bbe53d7ea51b93a733ee74f0744de3cf7660665e506a33862"

# weather soup
res_weather = requests.get(weather_url)
res_weather.raise_for_status()
weather_soup = BeautifulSoup(res_weather.text, "lxml")


location = weather_soup.find("h1", attrs={"class": "CurrentConditions--location--1YWj_"}).get_text()
weather = weather_soup.find("div", attrs={"class": "CurrentConditions--phraseValue--mZC_p"}).get_text()
curr_temp = weather_soup.find("span", attrs={"class": "CurrentConditions--tempValue--MHmYY"}).get_text()
high_low = weather_soup.find("div", attrs={"class": "CurrentConditions--tempHiLoValue--3T1DG"}).get_text()


# recognizing voice (listening)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='en-US')
        print('[User] ' + text)
        answer(text)
    except sr.UnknownValueError:
        print('Voice recognition failed')
    except sr.RequestError as e:
        print('Request failed : {0}'.format(e))


# answer
def answer(input_text):
    answer_text = ''
    if 'hi' in input_text:
        answer_text = 'How are you doing today?'
    elif 'weather' in input_text:
        answer_text = 'Weather for today at ' + location + ' is ' + weather + ' and ' + curr_temp + ' with ' + high_low
    elif 'thank you' in input_text:
        answer_text = 'You\'re welcome'
    elif 'bye' in input_text:
        answer_text = 'See you next time'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = 'Sorry, I don\'t understand'
    speak(answer_text)


# read out loud (TTS)
def speak(text):
    print('[AI] ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):  # remove voice.mp3 file everytime
        os.remove(file_name)


r = sr.Recognizer()
m = sr.Microphone()

speak('How may I help you?')
stop_listening = r.listen_in_background(m, listen)
# stop_listening(wait_for_stop=False) # stop listening

while True:
    time.sleep(0.1)
