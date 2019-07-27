+++
title = "Steering servo"
menuTitle = "Servo"
draft = false
weight=7
+++

![Servo](/images/rc_car/servo.png)

**An RC servo is used for controlling the steering wheels of the car.** It almost always comes with the RC car, so you shouldn’t worry about getting one.

It typically expects around 4.8V to 6V input on the power wire (varies by car) and a PWM control signal on the signal wire. Typically, the three wires are colored black-red-white, or brown-red-yellow, where:

- the dark wire (black/brown) is ground, 
- and the center wire (red) is power, 
- and the light wire (white/yellow) is control.

The control signal is RC-style PWM, where one pulse is sent 60 times a second, and the width of this pulse controls how left/right the servo turns. When this pulse is:

- 1500 microseconds, the servo is centered; 
- 1000 microseconds, the servo is turned all the way left (or right)
- 2000 microseconds, the servo is turned all the way in the other direction. 

{{% notice warning %}}
**This is NOT the same kind of PWM that you would use to control the duty cycle of a motor, or the brightness of a LED.**
{{% /notice %}}


The power for the servo typically comes from the motor ESC, which has a BEC (Battery Eliminator Circuit) built in.

Source: [DonkeyCar docs](http://docs.donkeycar.com/roll_your_own/).