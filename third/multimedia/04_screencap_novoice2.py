import time,threading
from datetime import datetime
from PIL import ImageGrab
from cv2 import *
import numpy as np
from pynput import keyboard
def video_record():   # 录入视频
  global name
  name = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # 当前的时间（当文件名）
  screen = ImageGrab.grab() # 获取当前屏幕
  width, high = screen.size # 获取当前屏幕的大小
  fourcc = VideoWriter_fourcc('X', 'V', 'I', 'D') # MPEG-4编码,文件后缀可为.avi .asf .mov等
  video = VideoWriter('%s.avi' % name, fourcc, 15, (width, high)) # （文件名，编码器，帧率，视频宽高）
  #print('3秒后开始录制----')  # 可选
  #time.sleep(3)
  print('开始录制!')
  global start_time
  start_time = time.time()
  while True:
    if flag:
      print("录制结束！")
      global final_time
      final_time = time.time()
      video.release() #释放
      break
    im = ImageGrab.grab()  # 图片为RGB模式
    imm = cvtColor(np.array(im), COLOR_RGB2BGR) # 转为opencv的BGR模式
    video.write(imm)  #写入
    # time.sleep(5) # 等待5秒再次循环
def on_press(key):   # 监听按键
  global flag
  if key == keyboard.Key.home:
    flag = True # 改变
    return False # 返回False，键盘监听结束！
def video_info():   # 视频信息
  video = VideoCapture('%s.avi' % name)  # 记得文件名加格式不要错！
  fps = video.get(CAP_PROP_FPS)
  Count = video.get(CAP_PROP_FRAME_COUNT)
  size = (int(video.get(CAP_PROP_FRAME_WIDTH)), int(video.get(CAP_PROP_FRAME_HEIGHT)))
  print('帧率=%.1f'%fps)
  print('帧数=%.1f'%Count)
  print('分辨率',size)
  print('视频时间=%.3f秒'%(int(Count)/fps))
  print('录制时间=%.3f秒'%(final_time-start_time))
  print('推荐帧率=%.2f'%(fps*((int(Count)/fps)/(final_time-start_time))))
if __name__ == '__main__':
  flag = False
  th = threading.Thread(target=video_record)
  th.start()
  with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
  time.sleep(1)  # 等待视频释放过后
  video_info()
