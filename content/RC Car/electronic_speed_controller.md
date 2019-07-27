+++
title = "Electronic Speed Controller"
menuTitle = "ESC"
draft = false
weight=8
+++

![Tamiya ESC](/images/rc_car/tamiya_esc.jpg)
**The role of the ESC is to take a RC PWM control signal (pulse between 1000 and 2000 microseconds) in, and use that to control the power to the motor so the motor spins with different amounts of power in forward or reverse.** Many RC car kits come with an ESC preinstalled, in which case you should be just fine. 


Again, 1500 microseconds typically means "center" which for the motor means "dead stop." 

The battery typically connects straight to the ESC using thicker wiring than the simple control signals, because the motor draws many more amps than the control. The ESC then connects on to the motor with equally thick power wiring. 

Standard motors and ESCs have a peak current of about 12A; a 1/8th scale RC car with powerful brushless motor can have a peak draw up to 200A.

Additionally, the ESC typically contains a linear or switching voltage converter that outputs the power needed to control the steering servo; this is typically somewhere in the 4.8V to 6V range. Most BECs built into ESCs will not deliver more than about 1A of current, so it is not typically possible to power both the steering servo and the Jetson Nano from the BEC.

{{% notice info %}}
The main thing to look out for when getting an ESC on your own is to **be sure to match your motor type to your ESC type (brushed/brushless)**. 
{{% /notice %}}


>Source: [DonkeyCar docs](http://docs.donkeycar.com/roll_your_own/).