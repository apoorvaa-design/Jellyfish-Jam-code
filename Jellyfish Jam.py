#Coding for the band drummer and guitarist
from machine import Pin, PWM
import time

# --- Servo Setup ---
servo_motor = PWM(Pin(15))  # For head or single servo
servo_motor.freq(50)

servo1 = PWM(Pin(14))  # Right arm
servo2 = PWM(Pin(26))  # Left arm
servo1.freq(50)
servo2.freq(50)

# --- Switch Setup ---
switch = Pin(13, Pin.IN, Pin.PULL_UP)

# --- Main Loop ---
while True:
    # Check limit switch
    if switch.value() == 0:  # Button pressed
        servo_motor.duty(77)  # Head servo to 90°
        print("Pressed - Pos2")
    else:
        servo_motor.duty(26)  # Head servo to 0°
        print("Released - Pos1")

    # Animate arms
    servo1.duty(77)  # Arms down (hit)
    servo2.duty(77)
    print("Hit!")
    time.sleep(0.75)

    servo1.duty(26)  # Arms up (rest)
    servo2.duty(26)
    print("Rest")
    time.sleep(0.75)


#Code for dancer-stepper motor

from machine import Pin
import time

coilA = Pin(12, Pin.OUT)

coilB = Pin(13, Pin.OUT)

coilC = Pin(14, Pin.OUT)

coilD = Pin(15, Pin.OUT)

sequence = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
coils = [coilA, coilB, coilC, coilD]

while True:
    for step in sequence:
        for i in range(len(coils)):
            coils[i].value(step[i])
            time.sleep(0.001)







#Code jelly fish pattern Background projections- Done on P5
#LINK-  https://editor.p5js.org/286asmidhaker/sketches/Uew-EIS2N
//let num = 300;
//let rez = 1;
//let angle = 0;
//let amp = 100;
//let speed = 1;

let slider;

let angle = 0;

let rotX;
let rotY;
let num;
let rez;
let amp;
let speed;

function setup() {
  createCanvas(800,600, WEBGL);
  angleMode(DEGREES);
  rotX = new Slider("RotX:", 0, 360, 15, 10, 10);

  rotY = new Slider("RotY:", 0, 360, 45, 10, 30);

  num = new Slider("Num:", 1, 400, 300, 10, 50);

  rez = new Slider("Rez:", 1, 15, 10, 10, 70);

  amp = new Slider("Amp:", 10, 200, 100, 10, 90);

  speed = new Slider("Speed:", 1, 10, 1, 10, 110);

  loadFont("Roboto-VariableFont_wdth,wght.ttf", drawText);
}

function drawText(font) {
  textFont(font, 11);
  fill(255);
}

function draw() {
  background(0, 0, 100);
  //let x = map(mouseX, 0, width, 0,360);

  //slider.display();

  rotX.display();
  rotY.display();
  num.display();
  rez.display();
  amp.display();
  speed.display();

  rotateX(rotX.val);
  rotateY(rotY.val);

  for (let a = 0; a < 10; a++) {
    for (let b = 0; b < 10; b++) {
      for (let i = 0; i < num.val; i += rez.val) {
        push();
        noFill();
        stroke(255, (i / num.val) * random(0,255), (i / num.val) * random(0,255), (i / num.val) * 255);
        let depth = amp.val * sin(angle + i);
        translate(400 * a -400, -400*b +400, depth);
        ellipse(0, 0, i, i);
        pop();
      }
    }
  }

  angle += speed.val;
}








