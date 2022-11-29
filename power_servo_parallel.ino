#include <Servo.h> 

Servo servo1; //servo1 변수 선언
Servo servo2; //servo2 변수 선언

int motor1 = 3; //motor1을 입출력 3번 핀에 연결
int motor2 = 5; //motor2을 입출력 5번 핀에 연결
int angle1 = 90; //초기 각도값 설정  
int angle2 = 90; //초기 각도값 설정

void setup() 
{ 
    servo1.attach(motor1); //servo1에 입출력 3번 핀을 지정
    servo2.attach(motor2); //servo2에 입출력 5번 핀을 지정
    Serial.begin(9600);
} 


void loop(){
  while (Serial.available()){
    char cmd = Serial.read();
    if (cmd == '0'){
      angle1=angle1;
      servo1.write(angle1);
      angle2=angle2;
      servo2.write(angle2); 
      }
    else if (cmd == '1'){
      angle2++;
      servo2.write(angle2); 
      }
    else if (cmd == '2'){
      angle1--;
      servo1.write(angle1);
      angle2++;
      servo2.write(angle2); 
      } 
    else if (cmd == '3'){
      angle1--;
      servo1.write(angle1);
      }
    else if (cmd == '4'){
      angle1--;
      servo1.write(angle1);
      angle2--;
      servo2.write(angle2); 
      } 
    else if (cmd == '5'){
      angle2--;
      servo2.write(angle2); 
      } 
    else if (cmd == '6'){
      angle1++;
      servo1.write(angle1);
      angle2--;
      servo2.write(angle2); 
      } 
    else if (cmd == '7'){
      angle1++;
      servo1.write(angle1);
      } 
    else if (cmd == '8'){
      angle1++;
      servo1.write(angle1);
      angle2++;
      servo2.write(angle2); 
      } 
    }
    }
