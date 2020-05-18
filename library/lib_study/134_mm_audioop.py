# mm -> Multimedia Services -> 多媒体服务

# E:\linux\emacs-26.3-x86_64\lib\python2.7\test\audiodata
import wave
import audioop

wav = wave.open("xx.wav")
print(audioop.avg(wav.readframes(wav.getnframes()), wav.getsampwidth()))
