# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 00:57:37 2019

@author: sefa
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)