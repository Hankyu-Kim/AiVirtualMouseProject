# AiVirtualMouseProject
AI 3D Virtual Mouse project done as capstone desing in dankook Univ.


![AiVirtualMouse Tracking Function (2)](https://user-images.githubusercontent.com/108254705/205451528-fb701f7d-bb6e-40e3-8414-f4f8886a9720.gif)
## tracking function
<br/>
<br/>
<br/>

![videoplayback](https://user-images.githubusercontent.com/108254705/205451348-fee58533-e4ae-41bb-9591-90de36146242.gif)
## (E.g. 3D Modeling)
<br/>

As a capstone design work for graduation, I designed an input device that can replace a mouse through a webcam with OpenCV and mediapipe library.
The key to coordinating this project was how to divide the team into many areas due to the character of electronic and electrical engineering, and how to divide work well with team members. We tried to meet as much as possible with cooperative SW developing partner and take a step by step with a big frame ( algorithm implementation, hardware design, motor control), etc. Our biggest mission was optimizing output data as a new input for Window cursor control with x, y coordinates and understanding there is not only bounding box as an output but also each joints position after model's feedforward. We tried to reinforce/augment data as an owner of program often.
For motor control, We planned to design only pop-up box for hardware. But after we got x,y coordinates from AI model to control mouse, we made tracking function with two servo motor that inspired from robot-arm. So when user try to get out from the display which is from webcam, motors follows hand with up-down and left-right angular control. 
After the end of the semester, we became best friends, kept in touch, and remained as a good colleagues/friends. Finally, our team won the graduation work and got the only A+ grade from the class. I found a big interest in the input device from this work and it becomes various experiences such as internship activities with recommendations from the university and other companies.
