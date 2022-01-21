import sys
import json
import os
import requests

from vosk import Model, KaldiRecognizer

channel = 'tv1'
date = datetime.today().strftime('%Y-%m-%d')
hour = '1700'

m3u8_url = f'https://sdma.telewebion.com/vod/_definst_/media_b2/telewebion/{channel}/{date}/{hour}/file.mp4/playlist.m3u8'


# recognizer = KaldiRecognizer(Model("model"), 16000)
# wf = open('foo.wav', "rb")
# wf.read(44)  # skip header
#
# while True:
#     data = wf.read(4000)
#     if len(data) == 0:
#         break
#     if rec.AcceptWaveform(data):
#         res = json.loads(rec.Result())
#         print(res['text'])
#
# res = json.loads(rec.FinalResult())
# print(res['text'])
