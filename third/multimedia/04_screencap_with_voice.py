import wave
from pyaudio import PyAudio,paInt16
from PIL import ImageGrab
import numpy as np
import cv2
from moviepy.editor import *
from moviepy.audio.fx import all
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
audio_record_flag = True
def callback(in_data, frame_count, time_info, status):
    wf.writeframes(in_data)
    if audio_record_flag:
        return (in_data, pyaudio.paContinue)
    else:
        return (in_data, pyaudio.paComplete)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                input=True,
                stream_callback=callback)
image = ImageGrab.grab()#获得当前屏幕
width = image.size[0]
height = image.size[1]
print("width:", width, "height:", height)
print("image mode:",image.mode)
k=np.zeros((width,height),np.uint8)

fourcc = cv2.VideoWriter_fourcc(*'XVID')#编码格式
video = cv2.VideoWriter('test.mp4', fourcc, 9.5, (width, height))
#经实际测试，单线程下最高帧率为10帧/秒，且会变动，因此选择9.5帧/秒
#若设置帧率与实际帧率不一致，会导致视频时间与音频时间不一致

print("video recording!!!!!")
stream.start_stream()
print("audio recording!!!!!")
record_count = 0
while True:
    img_rgb = ImageGrab.grab()
    img_bgr=cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
    video.write(img_bgr)
    record_count += 1
    if(record_count > 200):
        break
    print(record_count, time.time())

audio_record_flag = False
while stream.is_active():
    time.sleep(1)

stream.stop_stream()
stream.close()
wf.close()
p.terminate()
print("audio recording done!!!!!")

video.release()
cv2.destroyAllWindows()
print("video recording done!!!!!")

print("video audio merge!!!!!")
audioclip = AudioFileClip("output.wav")
videoclip = VideoFileClip("test.mp4")
videoclip2 = videoclip.set_audio(audioclip)
video = CompositeVideoClip([videoclip2])
video.write_videofile("test2.mp4",codec='mpeg4')
