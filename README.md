# 3D 모션컨트롤 기기
<br/>
전자공학과 전기공학과 로봇공학 전자전기공학과 졸업작품
<br/>
<br/>
준비물 : Webcam
<br/>
Power Servo motor(MR996) 2ea
<br/>
Arduino Uno
<br/>

https://www.youtube.com/watch?v=t7P1Vu8TYhk

## 데모
![videoplayback](https://user-images.githubusercontent.com/108254705/205451348-fee58533-e4ae-41bb-9591-90de36146242.gif)
## (E.g. 3D Modeling)
<br/>

As a capstone design work for graduation, I designed an input device that can replace a mouse through a webcam with OpenCV and mediapipe library.
The key to coordinating this project was how to divide the team into many areas due to the character of electronic and electrical engineering, and how to divide work well with team members. We tried to meet as much as possible with cooperative SW developing partner and take a step by step with a big frame ( algorithm implementation, hardware design, motor control), etc. Our biggest mission was optimizing output data as a new input for Window cursor control with x, y coordinates and understanding there is not only bounding box as an output but also each joints position after model's feedforward. We tried to reinforce/augment data as an owner of program often.
For motor control, We planned to design only pop-up box for hardware. But after we got x,y coordinates from AI model to control mouse, we made tracking function with two servo motor that inspired from robot-arm. So when user try to get out from the display which is from webcam, motors follows hand with up-down and left-right angular control. 
After the end of the semester, we became best friends, kept in touch, and remained as a good colleagues/friends. Finally, our team won the graduation work and got the only A+ grade from the class. I found a big interest in the input device from this work and it becomes various experiences such as internship activities with recommendations from the university and other companies.
