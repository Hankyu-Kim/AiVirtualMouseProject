import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
import pyautogui
import serial

py_serial = serial.Serial(
    port='COM4',
    baudrate=9600,
)

class ActiveTrack:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.ast_frame = 120
        self.smoothening_factor = 4
        self.customzg_distance = 4.5
        self.customzg_camera = 0
        self.num = [0, 0]

        self.preTime = 0
        self.prelocX = 0
        self.prelocY = 0
        self.curlocX = 0
        self.curlocY = 0

    def video_capture(self):
        V = cv2.VideoCapture(self.customzg_camera)
        V.set(3, self.width)
        V.set(4, self.height)
        return V

    def hand_dectector(self):
        hand_detector = htm.handDetector(maxHands=1)
        self.max_x, self.max_y = autopy.screen.size()

        while True:
            success, img = self.video_capture.read()
            self.img = hand_detector.findHands(img)
            lmList, bbox = hand_detector.findPosition(img)

            if success & (len(lmList) != 0):
                self.x1, self.y1 = lmList[8][1:]

                if ((self.width / 5) > self.x1 > 1) & ((self.height / 5) < self.y1 < 4 * (self.height / 5)):
                    cmd = '1'  # ld
                    py_serial.write(cmd.encode())

                elif ((self.width / 5) > self.x1 > 1) & ((self.height / 5) > self.y1 > 1):
                    cmd = '2'  # lu
                    py_serial.write(cmd.encode())

                elif ((self.width / 5) < self.x1 < 4 * (self.width / 5)) & ((self.height / 5) > self.y1 > 1):
                    cmd = '3'  # rd
                    py_serial.write(cmd.encode())

                elif (4 * (self.width / 5) < self.x1 < 640) & ((self.height / 5) > self.y1 > 1):
                    cmd = '4'  # ru
                    py_serial.write(cmd.encode())

                elif (4 * (self.width / 5) < self.x1 < 640) & ((self.height / 5) < self.y1 < 4 * (self.height / 5)):
                    cmd = '5'  # ru
                    py_serial.write(cmd.encode())

                elif (4 * (self.width / 5) < self.x1 < 640) & (4 * (self.height / 5) < self.y1 < 480):
                    cmd = '6'  # ru
                    py_serial.write(cmd.encode())

                elif ((self.width / 5) < self.x1 < 4 * (self.width / 5)) & (4 * (self.height / 5) < self.y1 < 480):
                    cmd = '7'  # ru
                    py_serial.write(cmd.encode())

                elif ((self.width / 5) > self.x1 > 1) & (4 * (self.height / 5) < self.y1 < 480):
                    cmd = '8'  # ru
                    py_serial.write(cmd.encode())

                else:
                    cmd = '0'
                    py_serial.write(cmd.encode())

                self.fingers = hand_detector.fingersUp()


    def move_curser(self):
        if self.fingers[1] == 1:

            x3 = np.interp(self.x1, (self.ast_frame, self.width - self.ast_frame) , (0, self.max_x))
            y3 = np.interp(self.y1, (self.ast_frame, self.height - self.ast_frame) , (0, self.max_y))

            curlocX = prelocX + (x3 - prelocX) / self.smoothening_factor
            curlocY = prelocY + (y3 - prelocY) / self.smoothening_factor

            autopy.mouse.move(self.max_x - curlocX, curlocY)

            prelocX, prelocY = curlocX, curlocY
            
if __name__ == '__main__':
    active_track = ActiveTrack
    try:
        active_track.video_capture()
        active_track.hand_dectector()
        active_track.move_curser()

        curTime = time.time()
        fps = 1 / (curTime - active_track.preTime)
        preTime = curTime

        cv2.imshow("Image", active_track.img)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        exit



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