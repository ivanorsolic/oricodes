+++
title = "Jetson Nano installation"
menuTitle = "Jetson Nano install"
draft = false
weight=10

+++

We’ll begin by preparing installing the Jetson Nano image and setting up the software neccessary to connect it to the RC Car via the PCA Servo Driver.

## Preparing the microSD

{{% notice tip %}}

The [official Jetson Nano docs](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit) are great and you can just follow them until the *Next Steps* step.

{{% /notice %}}

If you want a TL;DR version:

- [Download](https://developer.nvidia.com/jetson-nano-sd-card-image-r322) the Jetson Nano Developer Kit SD Card Image
- Format your microSD card and then flash the image on it using whatever tool you’d like. 
  - You can use [Etcher](https://www.balena.io/etcher)

- Insert the microSD into the Jetson and connect your peripherals to it: monitor, keyboard, mouse and an ethernet cable.

![Jetson](/images/jetson animation.gif)

{{% notice tip %}}

If you’re using Windows, after the flashing it’ll complain you need to [format the microSD before you use it](https://github.com/balena-io/etcher/issues/2024), since it doesn’t recognize the Linux filesystem you just flashed on it. Don’t format it, just ignore the warning.

{{% /notice %}}

## First boot

The TL;DR version would be:

- Carefully read through the NVIDIA Jetson software EULA and decide if you’ll accept it 🙃
- Select the system language, keyboard layout and time zone
- Create your user and name your Jetson
- Log in

If all went well, you should see the following screen:

![First boot](/images/first boot.png)

Congrats, you’ve set up the base OS for the Jetson. On to the fun part!

