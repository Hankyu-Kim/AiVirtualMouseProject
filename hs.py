import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
import pyautogui
import serial

py_serial = serial.Serial(
    # Window
    port='COM4',
    # 보드 레이트 (통신 속도)
    baudrate=9600,
)

def cmdreturning(cmd):
    return cmd

#########################__init__
w_Cam, h_Cam = 640, 480
ast_frame = 120
smoothening_factor = 4
customzg_distance = 4.5
customzg_camera = 0
num = [0, 0]
#########################

preTime = 0
prelocX, prelocY = 0, 0
curlocX, curlocY = 0, 0

video_capture = cv2.VideoCapture(customzg_camera)
video_capture.set(3, w_Cam)
video_capture.set(4, h_Cam)

hand_detector = htm.handDetector(maxHands=1)
w_Screen, h_Screen = autopy.screen.size()

while True:
    success, img = video_capture.read()
    img = hand_detector.findHands(img)
    lmList, bbox = hand_detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]

        if ((w_Cam / 5) > x1 > 1) & ((h_Cam / 5) < y1 < 4 * (h_Cam / 5)):
            cmd = '1'  # ld
            print(cmd)
            k = cmdreturning(cmd)
            commend = k
            py_serial.write(commend.encode())

        elif ((w_Cam / 5) > x1 > 1) & ((h_Cam / 5) > y1 > 1):
            cmd = '2'  # lu
            print(cmd)
            k = cmdreturning(cmd)
            commend = k
            py_serial.write(commend.encode())

        elif ((w_Cam / 5) < x1 < 4 * (w_Cam / 5)) & ((h_Cam / 5) > y1 > 1):
            cmd = '3'  # rd
            print(cmd)
            k = cmdreturning(cmd)
            commend = k
            py_serial.write(commend.encode())

        elif (4 * (w_Cam / 5) < x1 < 640) & ((h_Cam / 5) > y1 > 1):
            cmd = '4'  # ru
            print(cmd)
            k = cmdreturning(cmd)
            commend = k
            py_serial.write(commend.encode())

        elif (4 * (w_Cam / 5) < x1 < 640) & ((h_Cam / 5) < y1 < 4 * (h_Cam / 5)):
            cmd = '5'  # ru
            print(cmd)
            k = cmdreturning(cmd)
            commend = k
            py_serial.write(commend.encode())

        elif (4 * (w_Cam / 5) < x1 < 640) & (4 * (h_Cam / 5) < y1 < 480):
            cmd = '6'  # ru
            print(cmd)
            k = cmdreturning(cmd)
            commend = k
            py_serial.write(commend.encode())

        elif ((w_Cam / 5) < x1 < 4 * (w_Cam / 5)) & (4 * (h_Cam / 5) < y1 < 480):
            cmd = '7'  # ru
            print(cmd)
            k = cmdreturning(cmd)
            commend = k
            py_serial.write(commend.encode())

        elif ((w_Cam / 5) > x1 > 1) & (4 * (h_Cam / 5) < y1 < 480):
            cmd = '8'  # ru
            print(cmd)
            k = cmdreturning(cmd)
            commend = k
            py_serial.write(commend.encode())

    else:
        cmd = '0'
        print(cmd)
        k = cmdreturning(cmd)
        commend = k
        py_serial.write(commend.encode())

    fingers = hand_detector.fingersUp()

    # 마우스 이동
    if fingers[1] == 1:

        x3 = np.interp(x1, (ast_frame, w_Cam - ast_frame) , (0, w_Screen))
        y3 = np.interp(y1, (ast_frame, h_Cam - ast_frame) , (0, h_Screen))

        curlocX = prelocX + (x3 - prelocX) / smoothening_factor
        curlocY = prelocY + (y3 - prelocY) / smoothening_factor

        autopy.mouse.move(w_Screen - curlocX, curlocY)

        prelocX, prelocY = curlocX, curlocY

    # # 우클릭
    # if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[4] == 0 :
    #     length, img, position = hand_detector.findDistance(4, 8, img)
    #     if (position[0] - position[2]) < (16 * customzg_distance):
    #         pyautogui.click(button='right')
    #         print(pyautogui.click)
    #
    # # 좌클릭
    # if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[4] == 0 :
    #     length, img, position = hand_detector.findDistance(8, 12, img)
    #     if length < (9 * customzg_distance):
    #         autopy.mouse.click()
    # # 스크롤
    # if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[4] == 0 :
    #     length, img, position = hand_detector.findDistance(4, 8, img)
    #     if position[0] - position[2] > (12 * customzg_distance) :
    #         pyautogui.scroll(30, w_Screen - curlocX, curlocY)
    #     length, img, position = hand_detector.findDistance(8, 12, img)
    #     if length > (12 * customzg_distance):
    #         pyautogui.scroll(-30, w_Screen - curlocX, curlocY)
    #
    # # 드래그
    # if fingers    [0] == 0 and fingers[1] == 1 and fingers[2] == 0 and fingers[4] == 1 :
    #     pyautogui.mouseDown(button = 'left')
    #     if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 0 and fingers[4] == 0:
    #         pyautogui.moveTo(w_Screen - curlocX, curlocY, duration = 0.1)


    curTime = time.time()
    fps = 1/(curTime-preTime)
    preTime = curTime
    # 화면 출력
    cv2.imshow("Image", img)
    cv2.waitKey(1)