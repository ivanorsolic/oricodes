+++
title = "DonkeyCar configuration: RC car"
menuTitle = "DonkeyCar configuration: RC car"
draft = false
weight=15

+++

{{% notice info %}}

From now until the end of this chapter, I'll assume you're working on your car via SSH.

{{% /notice %}}

## Creating a DonkeyCar application

First, we'll run the [`createcar`](https://docs.donkeycar.com/utility/donkey/#create-car) command, which will create a new directory with all of the files needed to run and train our RC.

[Command usage](https://docs.donkeycar.com/utility/donkey/#create-car) from the docs:

```bash
donkey createcar --path <dir> [--overwrite] [--template <donkey2>]
```

Run the following command to create a new donkeycar application:

```bash
donkey createcar --path ~/mycar
```

Open the newly created directory:

```bash
cd ~/mycar
```

## Configuring the DonkeyCar application

We can find a bunch of settings for the application we just created in a file called `myconfig.py`. We'll have to edit this file to make our RC work as intended.

Open up the `myconfig.py` file in a text editor:

```bash
nano myconfig.py
```

**Note**: Some settings are commented out by default (read: have a `#` at the beginning of the line). **Whenever we're filling in a value of some setting, you should uncomment it first**/remove the `#` at the beginning.

### Camera settings:

If you're using Nano as your text editor, you can press `CTRL+W` and type in `CAMERA` and press enter to jump to the camera settings.

If you're using Vim, you probably don't need me to tell you how to search for stuff, but I'll do it anyways: type in `/CAMERA` to search forward for the camera settings, and use `n` and `N` to go back and forth between matches.

Here are the settings:

```bash
# #CAMERA
CAMERA_TYPE = "CVCAM"   # (PICAM|WEBCAM|CVCAM|CSIC|V4L|MOCK)
IMAGE_W = 1280
IMAGE_H = 720
IMAGE_DEPTH = 3
```

The different types of camera are:

- PICAM: the standard OV5647 Raspberry Pi camera
- CSIC: the Sony IMX219 Raspberry Pi camera v2+
- CVCAM: a USB camera connected to the Nano, I'm using this for my GoPro clone
- WEBCAM: also for USB cameras, but this requires further setup since it uses pygame
- V4L: Video4Linux
- MOCK: A fake camera that outputs a static frame.

If your image is flipped, or you want to mount your camera in a rotated position, use:

- CSIC_CAM_GSTREAMER_FLIP_PARM: for flipping your camera output
- Example: to flip your image vertically, use CSIC_CAM_GSTREAMER_FLIP_PARM = 3

Also, you can specify your resolution/image depth here:

- IMAGE_W: image width in pixels
- IMAGE_H: image height in pixels
- IMAGE_DEPTH: number of channels, 3 for RGB/BGR

### PCA9685 settings:

We also need to specify which bus we've connected our PCA9685 to. 

[See this to refresh your memory:](/hardware/connecting-the-car-to-the-nano/#connecting-the-pca9865-to-the-nano)

- If you used pins 3 and 5 on your Nano, then you're connected to Bus 1. 
- If you used pins 27 and 28, you're connected to Bus 0.

We'll also need the I2C address our PCA is connected to, for which we'll need to:

```bash
# Add our user to the i2c group
sudo usermod -aG i2c YOUR-USERNAME
# Reboot so it takes effect
sudo reboot
```

After rebooting, type:

```bash
# i2c-tools should come preinstalled with your Nano, but in case they aren't:
# sudo apt install i2c-tools

# For Bus 0: use 0
# For Bus 1: use 1
sudo i2cdetect -r -y 1
```

If your PCA is wired/connected correctly to the Nano, you should get something like:

```bash
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: 70 -- -- -- -- -- -- --
```

The results explained:

- 40 and 70: The addresses of our device. We'll be using the first one, 40, to address it.

- --: the address was probed, no chip was found
- UU: probing was skipped because the address is currently in use

If you're getting jibberish or all of the addresses are filled, check your connections, you probably swapped SDA and SCL or plugged them into the wrong pins.

Finally, in the `myconfig.py` file, find and fill the following:

```bash
PCA9685_I2C_ADDR = 0x40
PCA9685_I2C_BUSNUM = 1 
```

- PCA9685_I2C_ADDR: the I2C address of our PCA, in hex format (0xNumber)
- PCA9685_I2C_BUSNUM: the I2C bus our PCA is connected to

### Steering and throttle channels:

We also need to specify to which PCA channels our steering servo and our ESC are connected to. 

[See this to refresh your memory](/hardware/connecting-the-car-to-the-nano/#enter-the-pca9685) or just look at the numbers on the PCA, above the places you've connected your servo and esc connectors to, they correspond to their respective channel numbers.

In the settings, find and fill out the steering:

```bash
# #STEERING
STEERING_CHANNEL = 1            #channel on the 9685 pwm board 0-15
```

And the throttle channel values:

```bash
# #THROTTLE
THROTTLE_CHANNEL = 0            #channel on the 9685 pwm board 0-15
```

In my case, the throttle/ESC is the zeroth channel and the steering/servo is the first channel.

We will also need to fill out the following values for steering:

```bash
STEERING_LEFT_PWM = 295         #pwm value for full left steering
STEERING_RIGHT_PWM = 395        #pwm value for full right steering
```

And throttle:

```bash
THROTTLE_FORWARD_PWM = 310      #pwm value for max forward throttle
THROTTLE_STOPPED_PWM = 370      #pwm value for no movement
THROTTLE_REVERSE_PWM = 390      #pwm value for max reverse throttle
```

To do so, we'll need to calibrate our steering and throttle first, and then come back with the values we've found and fill them in.

Feel free to save the changes you've made to the `myconfig.py` file so far:

- Nano: `CTRL+O` and `Enter/Return` to save, `CTRL+X` to close the editor
- Vim: `:wq!` :) 