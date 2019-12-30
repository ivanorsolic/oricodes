+++
title = "Assembling the Jetson Nano"
menuTitle = "Assembling the Jetson Nano"
draft = false
weight=15

+++
Now we can finish up our Nano by connecting the WLAN card, microSD and the fan to it.

## Plugging in the microSD

{{% notice tip %}}

I actually already did a lot of assembly some time ago, and I'm writing this in retrospect, so don't be worried if my Nano has a lot of stuff already hooked up to it and if it looks a bit different than yours, just focus on the stuff we're going through and disregard the rest.

{{% /notice %}}

First, we have to take out the Nano module from the breakout board we got it with. We begin by unscrewing these two Phillips screws, highlighted in yellow:

<img src="/images/hardware/jetson1.png" alt="Two Phillips screws to unscrew" style="zoom:50%;" />

After unscrewing them, pull these two levers outwards (highlighted in yellow)  and your Nano module will pop out:

<img src="/images/hardware/jetson2.png" alt="Levers that hold the Nano card in place" style="zoom:50%;" />

The Nano should pop out like this:

<img src="/images/hardware/jetson3.png" alt="Nano pops out" style="zoom:50%;" />

And after pulling it out, you can plug in your microSD on the bottom side:

<img src="/images/hardware/jetson4.png" alt="microSD slot" style="zoom:50%;" />

## Connecting the Noctua fan to the Nano

On the other side of the module, you can find the heatsink with four screw holes into which, if you haven't done so already, you can screw in the fan you bought for your Nano:

<img src="/images/hardware/jetson5.png" alt="Noctua fan" style="zoom:50%;" />

You also need to plug in the 3-pin (or 4-pin) fan connector to the Jetson board right below the ethernet port:

<img src="/images/hardware/jetson6.png" alt="Fan connector" style="zoom:50%;" />

## Plugging in the WLAN+BT card

The only thing left is the wireless card, which is plugged into the slot at the middle of the breakout board. You just need to unscrew one Phillips screw, insert the card, put the screw back in and connect your antennae connectors to the WLAN card. The antennae are the same, so don't worry where to plug which one, it doesn't matter.

<img src="/images/hardware/jetson7.png" alt="WLAN+BT Card" style="zoom:50%;" />

#### And that's it for the Nano board! 

After putting it all back together, and connecting the antennae, it looks something like this:

<img src="/images/hardware/jetson8.png" alt="Finished Jetson Nano" style="zoom:50%;" />
