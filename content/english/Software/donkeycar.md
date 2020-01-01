+++
title = "DonkeyCar"
menuTitle = "DonkeyCar: Explained"
draft = false
weight=11

+++

> *Donkey is a high level self driving library written in Python. It was developed with a focus on enabling fast experimentation and easy contribution.*
>
> Source: [Official Donkey docs](http://docs.donkeycar.com/)

We'll be using Donkey® as an interface between our RC car and the neural net we'd like to drive it for us.

<img src="/images/software/donkey.png" alt="DonkeyCar diagram" style="zoom:50%;" />

As you can see above, we'd like to send the camera data from our RC to a model which would analyse it and tell the RC where to steer and how fast to go, in order to stay on the road.

Donkey will provide us with an interface to do just so, without having to worry about the details of:

- (Pre) Processing the camera data
- Converting the steering/throttle values to actual signals for the RC to understand
- Actually steering the RC and increasing/decreasing throttle

It will also enable us to:

- Collect and label training data
- Define and train custom models
- Control the car using a Web interface or a gamepad
- And even use a simulator to rapidly test and train our models

### How to get it up and running

There are two ways to go about this:

- Doing everything on your RC car/Jetson Nano, including model training
- Training and developing the model on a host PC, running and testing it on your RC

I'd very much recommend going with the second option, since you'll need the extra horsepower of a PC in order to be able to train and develop complex models, preferably with a GPU. But, if you want, you can disregard my advice and skip installing the Donkey to your host PC and just install it on your RC and do everything from there.

We'll continue our project by explaining how to:

- Install Donkey on your host PC
- Install a simulator on your host PC
- Install Donkey on your RC
- Calibrate your RC and actually control it using Donkey, via the Web interface or a gamepad
- Do a sanity check by training a very simple model to see if everything works as it should

### Further Donkey resources

Before we get to work, here are some links to Donkey resources you can check out to get familiar with it, and maybe better understand how it works:

#### [The official Donkey documentation](http://docs.donkeycar.com/) and the Slack channel

I highly recommend going through these two. The docs are great and the Slack channel has a bunch of people trying to do the same thing you are, who love helping one another solve issues and bounce ideas. I love the Donkey community and can't recommend enough going over to the channel and just saying hi.

The following videos are also an interesting watch, albeit not necessary to continue with the tutorial. One of the reasons why we're using Donkey is so we don't have to worry about all of the details it solves for us. But if you're like me, you're gonna wanna know a bit how it works before using it to piece your RC together. :) 

#### CircuitBread's overview of the Donkey platform with Ed Murphy

{{< youtube cKhrV_RYVOw >}}

#### DonkeyCar's founder, Adam Conway's video of assembling a DonkeyCar

{{< youtube OaVqWiR2rS0 >}}

#### Make magazine's video of building a Raspberry Pi DonkeyCar

{{< youtube byRLYkZkJZE >}}

#### Tawn Kramer's two part overview of the DonkeyCar framework

{{< youtube YZ4ESrtfShs >}}



{{< youtube G1JjAw_NdnE >}}

#### William Roscoe's quick get started video)

{{< youtube NGTbzfx7aL4 >}}