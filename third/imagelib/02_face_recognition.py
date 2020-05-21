# only Linux
# pip3 install face_recognition
# pip3 install face_recognition -i  http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
# https://github.com/ageitgey/face_recognition

import face_recognition

# 识别出人脸的位置
image = face_recognition.load_image_file("lenna.jpg")
face_locations = face_recognition.face_locations(image)
print(face_locations)

# 识别是不是同一个人
import face_recognition
known_image = face_recognition.load_image_file("lenna.jpg")
unknown_image = face_recognition.load_image_file("lenna.jpg") # "wallhaven-nmekwy.jpg"

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

print(results)


# 面部特征
image = face_recognition.load_image_file("lenna.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks_list)