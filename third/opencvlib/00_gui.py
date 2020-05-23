def demo01():
    import cv2 as cv
    import sys
    img = cv.imread(cv.samples.findFile("../imagelib/lenna.jpg"))
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("starry_night.png", img)

# Capture Video from Camera
def demo02():
    import numpy as np
    import cv2 as cv
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()


# Playing Video from file
def demo03():
    import numpy as np
    import cv2 as cv
    cap = cv.VideoCapture('vtest.avi')
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
# Saving a Video
def demo04():
    import numpy as np
    import cv2 as cv
    cap = cv.VideoCapture(0)
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID') # http://www.fourcc.org/codecs.php
    # `cv.VideoWriter_fourcc('M','J','P','G')or cv.VideoWriter_fourcc(*'MJPG')` for MJPG.
    # FourCC是一个4字节的代码，用于指定视频编解码器。可用代码的列表可以在fourcc.org上找到。它依赖于平台。
    # In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
    # In Windows: DIVX (More to be tested and added)
    # In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv.flip(frame, 0) # 翻转
        # write the flipped frame
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()

def Drawing01():
    #  cv.line(), cv.circle() , cv.rectangle(), cv.ellipse(), cv.putText()
    import numpy as np
    import cv2 as cv
    # Create a black image
    img = np.zeros((512, 512, 3), np.uint8) # 黑色画布
    # Draw a diagonal blue line with thickness of 5 px
    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

    cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

    cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

    cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1) # 椭圆

    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(img, [pts], True, (0, 255, 255))

    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

    cv.imshow('Drawing', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 鼠标作为画笔
def Drawing02():
    import cv2 as cv
    import numpy as np
    events = [i for i in dir(cv) if 'EVENT' in i]
    print(events)

    # mouse callback function
    def draw_circle(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDBLCLK: # 双击
            cv.circle(img, (x, y), 100, (255, 0, 0), -1)

    # Create a black image, a window and bind the function to window
    img = np.zeros((512, 512, 3), np.uint8) # 黑色画布
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    while (1):
        cv.imshow('image', img)
        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()
# 鼠标作为画笔
def Drawing03():
    import cv2 as cv
    import numpy as np
    drawing = False  # true if mouse is pressed
    mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
    ix, iy = -1, -1

    # mouse callback function
    def draw_circle(event, x, y, flags, param):
        nonlocal ix, iy, drawing, mode
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv.EVENT_MOUSEMOVE:
            if drawing == True:
                if mode == True:
                    cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
                else:
                    cv.circle(img, (x, y), 5, (0, 0, 255), -1)
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)

    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    while (1):
        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break
    cv.destroyAllWindows()

# 调色板
def Trackbar01():
    import numpy as np
    import cv2 as cv
    def nothing(x):
        pass

    # Create a black image, a window
    img = np.zeros((300, 512, 3), np.uint8)
    cv.namedWindow('image')
    # create trackbars for color change # 跟踪条控件
    cv.createTrackbar('R', 'image', 0, 255, nothing)
    cv.createTrackbar('G', 'image', 0, 255, nothing)
    cv.createTrackbar('B', 'image', 0, 255, nothing)
    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv.createTrackbar(switch, 'image', 0, 1, nothing)
    while (1):
        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
        # get current positions of four trackbars
        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')
        s = cv.getTrackbarPos(switch, 'image')
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]
    cv.destroyAllWindows()


if __name__=="__main__":
    Trackbar01()

