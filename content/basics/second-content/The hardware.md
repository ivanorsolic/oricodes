---
title: "The Hardware"
date: 2019-07-27T15:46:14+02:00
draft: false

---

# The hardware

This is the first post in the series of guides on how to make a RC car. 

It will explain what hardware parts and tools are needed, how to put them all together and how to setup the base software needed for it to run. 

The end result should be something that looks like this, and runs a custom Linux kernel:

<video controls autoplay>
    <source src="C:\Users\ori\Desktop\3D Models\car 2.mp4" type="video/mp4">
</video>

## Parts list

You'll want to have:

- A RC car (with some batteries)
- A PWM/Servo Driver (I2C + some jumper cables)
- A Jetson Nano
- A powerbank (+ some usb cables)
- A microSD card (and optionally an external SSD)
- A WiFi/BT m.2 card (key E) or some USB equivalent
- Some tools and materials for building the chassis (and optionally access to a 3D printer)
- An Xbox/PS/PC gamepad

Let's go through each of the parts.

# RC Car

You can basically get any RC car, as long as it has an ESC controller, or you can hook up one to it. But not to get ahead of ourselves, let's first look at some of the things that are important to consider in a RC car if you want to make it drive itself:

- Scale
- Body type
- Electric motor
- Servo
- ESC
- Receiver
- Batteries

### The scale

Most RC cars are scaled down versions of their real-life equivalent, so they're expressed in ratios, the most common ones being (real-life size : RC model size):

- 1:18
- 1:16
- 1:10
- 1:8
- there are also all sorts of scales in between those (and above/below)

**Of course, the question is: why do we care, and what's better for a self-driving RC car?**

It's pretty simple, **a bigger RC car equals more real estate and more power** to carry all of our gadgets on top of it, without damaging the motors while struggling with all of the weight. **The down side of a bigger car is the need for a bigger race track** and road size we want to drive it on. 

![Image result for rc car scales](https://i.pinimg.com/originals/ef/7d/20/ef7d206abe733c9faf0218cf2afd179f.jpg)

## The body type

The best body type for on road self-driving purposes would be the standard race body type. But to be thorough, we could roughly group all of the RC cars in 4 distinct categories:

### **RACE/STREET**

![1564143558801](C:\Users\ori\AppData\Roaming\Typora\typora-user-images\1564143558801.png)

Probably the first thing that comes to mind when thinking of an RC car, a standard race car. 
This body type is the fastest and the best on paved, flat surfaces and is meant for on road use only.

There is also a specialized group of RC cars of this body type that are meant for drifting on racing tracks. The main difference are the tires, which are much slicker than regular ones.

### **BUGGY**

![1564143548752](C:\Users\ori\AppData\Roaming\Typora\typora-user-images\1564143548752.png)

Buggies are the golden middle between an off-road and on road RC car. They are the second best thing on the road but the slowest off-road. That being said, they *can* go off-road, unlike a regular racing car, so that makes them the best bet for people that aren't sure if they want to go off-road or on road.



## TRUGGY

![1564143975179](C:\Users\ori\AppData\Roaming\Typora\typora-user-images\1564143975179.png)

Truggies are also an in-between body type, but they lean more to the off-road role, as opposed to the buggies. Consider them a buggy with monster truck tires. They're the second fastest body type off-road, and the third fastest on road.

### TRUCKS

![1564143801923](C:\Users\ori\AppData\Roaming\Typora\typora-user-images\1564143801923.png)

Truck are your regular monster trucks, the best for going off-road but the slowest for going on road. For a self-driving application, they'd be pretty bad, since they tend to flip over while making on road turns, so it's best to stick with them only if you're planning to go off road in the woods, grass or dirt. 

## Electric motors

The main question concerning electric motors is: **brushed or brushless?**

![Related image](https://www.portable-electric.com/wp-content/uploads/brushed-brushless.jpg)

**Brushed pros:** cheaper, simpler, better for off-road. 
**Brushed cons:** heavier, bigger, worse power efficiency (75-80%), they wear out in time.

**Brushless pros:** long lifespan, much better speed and handling, better power efficiency (85-90%).
**Brushless cons:** much more expensive, worse for off-road.

So what should we get? It depends on your budget, but brushed motors work just fine, and besides, for self-driving purposes, you don’t need a RC car that drives 100 KPH. It’s also always possible to swap out a brushed motor for a brushless later on.

## Servo

![1564145380411](C:\Users\ori\AppData\Roaming\Typora\typora-user-images\1564145380411.png)

**An RC servo is used for controlling the steering wheels of the car.** It almost always comes with the RC car, so you shouldn’t worry about getting one.

It typically expects around 4.8V to 6V input on the power wire (varies by car) and a PWM control signal on the signal wire. Typically, the three wires are colored black-red-white, or brown-red-yellow, where:

- the dark wire (black/brown) is ground, 
- and the center wire (red) is power, 
- and the light wire (white/yellow) is control.

The control signal is RC-style PWM, where one pulse is sent 60 times a second, and the width of this pulse controls how left/right the servo turns. When this pulse is:

- 1500 microseconds, the servo is centered; 
- 1000 microseconds, the servo is turned all the way left (or right)
- 2000 microseconds, the servo is turned all the way in the other direction. 

**This is NOT the same kind of PWM that you would use to control the duty cycle of a motor, or the brightness of a LED.**

The power for the servo typically comes from the motor ESC, which has a BEC (Battery Eliminator Circuit) built in.

Source: [DonkeyCar docs](http://docs.donkeycar.com/roll_your_own/).

## Electronic Speed Controller (ESC)

**The role of the ESC is to take a RC PWM control signal (pulse between 1000 and 2000 microseconds) in, and use that to control the power to the motor so the motor spins with different amounts of power in forward or reverse.** Many RC car kits come with an ESC preinstalled, in which case you should be just fine. 

Again, 1500 microseconds typically means "center" which for the motor means "dead stop." 

The battery typically connects straight to the ESC using thicker wiring than the simple control signals, because the motor draws many more amps than the control. The ESC then connects on to the motor with equally thick power wiring. 

Standard motors and ESCs have a peak current of about 12A; a 1/8th scale RC car with powerful brushless motor can have a peak draw up to 200A.

Additionally, the ESC typically contains a linear or switching voltage converter that outputs the power needed to control the steering servo; this is typically somewhere in the 4.8V to 6V range. Most BECs built into ESCs will not deliver more than about 1A of current, so it is not typically possible to power both the steering servo and the Jetson Nano from the BEC.

The main thing to look out for when getting an ESC on your own is to **be sure to match your motor type to your ESC type (brushed/brushless)**. 

Source: [DonkeyCar docs](http://docs.donkeycar.com/roll_your_own/).

## Receiver

![1564146948251](C:\Users\ori\AppData\Roaming\Typora\typora-user-images\1564146948251.png)

**If you buy a "kit car" that is listed as "needs a receiver," then you don't need to buy a receiver.** 

The Jetson Nano and the PWM/Servo driver will replace the receiver, outputting control signals to the car. If you’re buying a kit with a steering servo, motor, and ESC, **you should actually try to** **not get a receiver**, since the RC car could be specifically designed for that receivers PWM signals, and you’ll be taking it apart anyways. 

## Batteries

![Related image](https://images.amain.com/images/large/tra/tra2993.jpg)

**There are two types of batteries used for RC cars: Nickel Metal Hydride batteries (NiMH) and Lithium Polymer batteries (LiPo).**

**TL;DR: LiPo batteries are much better, but also more expensive.**

Lithium Polymer batteries generally have higher current capacity (the amount of Amps the battery can deliver at one point while driving) as well as energy storage (the number of Amp Hours the battery stores when fully charged) so it may also last longer.

**The amount of charge a battery can hold (how long it runs) is measured in Ampere-hours**. 
**The amount of current a battery can instantaneously deliver while driving is measured simply in Amperes.** 

Amperes are often re-calculated in terms of multiples of the energy content, divided by one hour which is often called "C." Thus, a LiPo rated for 10C and 2000 mAh, can deliver 20 Amperes of current while driving. A NiHM rated for 5C and 1100 mAh can deliver 5.5 Amperes of current while driving. 

Batteries can deliver more than the C rating for very short amounts of time, but will heat up or build up internal resistance so you shouldn’t count on that as being their standard capability.

**For your custom car, be aware of the voltages needed for the ESC and the motor of the car, and make sure to get a battery that matches them in voltage.** 

Smaller RC cars will come with NiMH for affordability, or 2S LiPo for power. Larger RC cars will use 3S (11.1V) or 4S (14.8V) or even 6S (22.2V) Lithium batteries, and thus need to have ESC and motor combinations to match.

**Be sure to get a charger that matches your battery.** 

If you have a LiPo battery:

- get a good Lithium battery charger, with a balancing plug,
- **never discharge a Lithium battery below 3.2V per cell**

**If you discharge a LiPo battery completely, it won’t ever be charged up to its normal voltage again, and trying to do so will overheat the battery and set it on fire.**

To prevent this, get a battery alarm and a LiPo charging bag:

![Related image](https://cdn.shopify.com/s/files/1/0790/0655/products/batterymonitorscreen_1024x1024.jpg?v=1465472962)



![Image result for lipo charging bag](https://rcgearlab.com/wp-content/uploads/2019/02/lipo-bag-feature.jpg)

#### Tamiya TT-01/TT-02