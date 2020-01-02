+++
title = "Calibrating steering and throttle"
menuTitle = "Calibrating steering and throttle"
draft = false
weight=16

+++

{{% notice warning %}}

**Make sure your car wheels are not touching the ground.** Prop it up using a shoebox, or in my case, an eGPU dock. We will be calibrating the throttle which means your car will start accelerating very fast, without warning, so you wouldn't want it slamming into a wall at full throttle.

{{% /notice %}}

## Calibrating the throttle:

<center><video controls src="/video/throttle_calibration.mp4" autoplay loop width="500px"></video></center>

**First, you'll need to turn on your car**; the actual RC, not the Nano.

Depending on your RC, it'll probably beep because it's turned on and the controller isn't connected to it, but don't worry, it'll stop once we connect to it via the I2C bus.

Run the following:

```bash
donkey calibrate --channel YOUR_ESC\THROTTLE_CHANNEL --bus=YOUR_I2C_PCA_BUS
```

The output should look like:

```bash
using donkey v3.1.1 ...
init PCA9685 on channel 0 address 0x40 bus 0
Using PWM freq: 60

Enter a PWM setting to test ('q' for quit) (0-1500):
```

If you're using the wrong bus, you'll probably get a `OSError: [Errno 121] Remote I/O error`

Type in `370` and press enter. The ESC should stop beeping, indicating it is calibrated to the neutral throttle position.

To detect your forward values for the throttle:

- Try entering 400 and seeing if your car starts throttling forwards.
- If it's not, then try entering 330 instead.
- After finding out which *direction* forwards is:
  - Number larger than 370
  - Number smaller than 370
- Start from 370 and enter values +/- 10 and choose a value that you want your maximum forward throttle to be and write it down.

To detect your reverse values for the throttle:

- In order to go in reverse, the RC needs to get a reverse throttle value, followed by the neutral throttle value, followed by the reverse throttle value again.

- If your forward values were larger than 370:
  - Enter 330, then 370, then 330.
- If your forward values were smaller than 370:
  - Enter 400, then 370, then 330.
- After confirming how to get your car in reverse throttle, once again start from 370 and enter values +/- 10 and choose a value that you'd like your max reverse throttle to be, and write it down.

**You can now enter q to finish the throttle calibration procedure.**

## Calibrating the steering

<center><video controls src="/video/steering_calibration.mp4" autoplay loop width="500px"></video></center>

Once again, run the following:

```bash
donkey calibrate --channel YOUR_STEERING_CHANNEL --bus=YOUR_I2C_PCA_BUS
```

- Enter 360, and you should see your car slightly steering. If you don't, try 350 or 370.
- Once again, enter +/- 10 values to find out what values steer your car completely to the left and to the right and write them down.

**You can now enter q to finish the steering calibration procedure.**

## Entering the values in the config file

Open up the `myconfig.py` in the editor of your choice:

```bash
nano ~/mycar/myconfig.py
```

Find the `THROTTLE` and `STEERING` sections and enter the values you wrote down during calibration:

- STEERING_RIGHT_PWM: the value which steers your car completely to the right.
- STEERING_LEFT_PWM: the value which steers your car completely to the right.
- THROTTLE_STOPPED_PWM: the neutral throttle value.
- THROTTLE_FORWARD_PWM: the maximum forward throttle value.
- THROTTLE_REVERSE_PWM: the maximum reverse throttle value.

Save the file and exit the editor and you're done!