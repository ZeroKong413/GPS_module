import zmq
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from time import sleep

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://0.0.0.0:12345")

img_str = socket.recv(copy=False)
img =cv2.imdecode(np.frombuffer(img_str, dtype=np.uint8), cv2.IMREAD_COLOR)

# 이미지를 저장하는 것
cv2.imwrite("test123.jpg", img)


# # 이미지를 보여주는 것 (프로젝트에서는 필요 없을 듯)
# cv2.imshow("Image", img)
# cv2.waitKey(0)

sleep(5)


# 저장된 모델 불러오기
loaded_model = load_model('c:/my_model20.h5')
# 새로운 사진 분류
new_image_path = 'test123.jpg'
new_image = cv2.imread(new_image_path)
# new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
new_image = new_image.reshape((1,) + new_image.shape)
new_image = new_image.astype('float32') / 255.0

prediction = loaded_model.predict(new_image)
print(prediction[0][0])

if prediction[0][0] > 0.9:
    print("이 물건은 학습시킨 물건입니다.")
    # 라즈베리파이에 보내주기?
    # 다시 zmq를 또 써야될 듯

    # zmq 컨텍스트 생성
    context = zmq.Context()

    # 소켓 생성
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.219.146:54321")
    socket.send_string('yes')
else:
    print("이 물건은 학습시킨 물건이 아닙니다.")
    # zmq 컨텍스트 생성
    context = zmq.Context()

    # 소켓 생성
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.219.146:54321")
    socket.send_string('no')
