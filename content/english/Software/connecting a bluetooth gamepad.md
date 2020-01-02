+++
title = "Using a gamepad"
menuTitle = "Using a gamepad"
draft = false
weight=17

+++

You can, and should, use a gamepad to control your RC. It's much easier to generate good training data using a gamepad, and it's much easier to drive the thing compared to the Web interface that Donkey provides. 

So how do we connect and use one?

## Compatible controllers

First, let's make sure you have one that'll actually work

[The official Donkey docs](https://docs.donkeycar.com/parts/controllers/#physical-joystick-controller) list that the following are known to work:

- [Logitech Gamepad F710](https://www.amazon.com/Logitech-940-000117-Gamepad-F710/dp/B0041RR0TW)
- Sony PS3 Dualshock OEM
- [Sony PS3 Sixaxis OEM](https://www.ebay.com/sch/i.html?&_nkw=Sony+PS3+Sixaxis+OEM) (Not compatible with Jetson Nano)
- [Sony PS4 Dualshock OEM](https://www.ebay.com/sch/i.html?&_nkw=Sony+PS4+Dualshock+OEM)
- [WiiU Pro](https://www.amazon.com/Nintendo-Wii-U-Pro-Controller-Black/dp/B00MUY0OFU)
- [XBox Controller](https://www.amazon.com/Xbox-Wireless-Controller-Blue-one/dp/B01M0F0OIY)
- [SteelSeries Nimbus](https://www.amazon.com/gp/product/B01AZC3III) (works only on TX2 jetpack 4.2+, may work on the Nano)

Depending on the controller you're going to use, open up the `myconfig.py` file and find the `# JOYSTICK` section and uncomment and fill the following (using one of the types suggested inline with the setting):

```bash
CONTROLLER_TYPE='xbox'               #(ps3|ps4|xbox|nimbus|wiiu|F710|rc3)
```

If your gamepad isn't *officially* supported, try following the rest of the tutorial and connecting it to the Nano. If it shows up as `/dev/input/js0`, you should be able to use it, since the Donkey platform just uses that OS device mount as the gamepad.

## Connecting your gamepad (via Bluetooth)

### Xbox (One) Controller

The Xbox controller doesn't like the *Enhanced Re-Transmission Mode*, so we'll disable it first.

Open up the `/etc/modprobe.d/xbox_bt.conf` file (this may actually create the file if it doesn't exist yet):

```bash
sudo nano /etc/modprobe.d/xbox_bt.conf
```

```bash
# Add this line and save the file
options bluetooth disable_ertm=1
```

```bash
# Reboot
sudo reboot
```

After rebooting, check it's actually disabled by running:

```bash
cat /sys/module/bluetooth/parameters/disable_ertm
```

It should say '**Y**'. If it does, open up bluetoothctl:

```bash
sudo bluetoothctl
```

```
# Register the default agent
agent on
# Default agent request
default-agent
# Scan for devices
scan on
```

Turn on your Xbox controller (by pressing the big **Xbox logo button**) and start the pairing mode by pressing the **sync** button on the back of the controller, next to the microUSB port.

You should see your controller show up in bluetoothctl similar to:

```bash
[NEW] Device YO:UR:MA:CA:DD:RS XBox One Wireless Controller
```

Type in:

```bash
# This may take a few tries ...
connect YOUR_MAC_ADDRESS
# If it connects but immediately disconnects, the disable_ertm setting isn't properly set up, try doing that again
# When it connects and the big Xbox logo button is solid white:
trust YOUR_MAC_ADDRESS
quit
```

Once connected, it should automatically reconnect anytime the Jetson and it are both powered on. If it doesn't, you'll have to run the steps above again.

### PS3 Controller

The Donkey docs say to follow [this guide](https://pythonhosted.org/triangula/sixaxis.html), or you can just run:

```bash
sudo apt-get install bluetooth libbluetooth3 libusb-dev
sudo systemctl enable bluetooth.service
sudo usermod -G bluetooth -a pi
sudo reboot
```

After rebooting, plug in the controller with an USB cable, press the **PS button** and:

```bash
wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb
sudo ./sixpair
```

Run bluetoothctl as a super user and pair your controller:

```bash
sudo bluetoothctl
```

```bash
# Enable the default agent
agent on
# List all found devices and get your controller's MAC address
devices
# Trust your controller
trust <MAC ADDRESS>
# Default agent request
default-agent
# Quit
quit
```

Unplug the USB cable and press the **PS button**. Your controller should be mounted at `ls /dev/input/js0`.

### PS4 Controller

Install ds4drv:

```bash
sudo pip install ds4drv
```

Grant it permissions:

```bash
sudo wget https://raw.githubusercontent.com/chrippa/ds4drv/master/udev/50-ds4drv.rules -O /etc/udev/rules.d/50-ds4drv.rules
sudo udevadm control --reload-rules
sudo udevadm trigger
sudo reboot
```

After rebooting run ds4drv:

```bash
# --led changes the light bar color, you can modify it or not use it at all
# --hidraw doesn't play well with some controllers, if you're having issues, try not using it
ds4drv --hidraw --led 00ff00
```

Start the controller in pairing mode:

- Press and hold **Share** button
- Press and hold **PS** button until the light bar starts blinking
- If it goes **green** after a few seconds, pairing is successful.

To run ds4drv on boot, open up `/etc/rc.local` and paste in the command you used to start ds4drv:

```bash
sudo nano /etc/rc.local
```

```bash
# Paste in (with or without --hidraw and --led):
/home/YOUR-USERNAME/env/bin/ds4drv --led 00ff00
```

## Creating a Button/Axis mapping:

- TODO