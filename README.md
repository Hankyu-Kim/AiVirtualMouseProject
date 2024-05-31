# AiVirtualMouseProject
AI 3D Virtual Mouse project done as capstone desing in dankook Univ.


<p align="center" width="100%">
  <img src="https://github.com/Hankyu-kim/AiVirtualMouseProject/assets/108254705/00cf0811-d0a9-41da-81a5-301f0e917498" align="center" width="49%">
  <img src="https://user-images.githubusercontent.com/108254705/205451348-fee58533-e4ae-41bb-9591-90de36146242.gif" align="center" width="49%">
</p>



fig.1 active track | fig.2 control mousr cursor using hand gesture

## (E.g. 3D Modeling)
<br/>

As a capstone design work for graduation, I designed an input device that can replace a mouse through a webcam with OpenCV and mediapipe library.
The key to coordinating this project was how to divide the team into many areas due to the character of electronic and electrical engineering, and how to divide work well with team members. We tried to meet as much as possible with cooperative SW developing partner and take a step by step with a big frame ( algorithm implementation, hardware design, motor control), etc. Our biggest mission was optimizing output data as a new input for Window cursor control with x, y coordinates and understanding there is not only bounding box as an output but also each joints position after model's feedforward. We tried to reinforce/augment data as an owner of program often.
For motor control, We planned to design only pop-up box for hardware. But after we got x,y coordinates from AI model to control mouse, we made tracking function with two servo motor that inspired from robot-arm. So when user try to get out from the display which is from webcam, motors follows hand with up-down and left-right angular control. 
After the end of the semester, we became best friends, kept in touch, and remained as a good colleagues/friends. Finally, our team won the graduation work and got the only A+ grade from the class. I found a big interest in the input device from this work and it becomes various experiences such as internship activities with recommendations from the university and other companies.
