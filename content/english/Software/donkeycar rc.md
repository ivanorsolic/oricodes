+++
title = "DonkeyCar installation: RC car"
menuTitle = "DonkeyCar: RC car"
draft = false
weight=14

+++

## Connecting to your RC via SSH

To connect and work with your RC throughout the rest of the project, you'll need two things:

- An SSH client
- The IP address of your RC

### SSH Clients:

If you're using Linux or a Mac, you're all set. They come with a SSH client pre-installed, and you just need to open up a terminal and type:

```bash
ssh username@ipAddress
```

If you're using Windows, you need to install one. I'd recommend using [MobaXTerm](https://mobaxterm.mobatek.net/):

- Download [the installer](https://download.mobatek.net/1242019111120613/MobaXterm_Installer_v12.4.zip) or [the portable version](https://download.mobatek.net/1242019111120613/MobaXterm_Portable_v12.4.zip) and install/unpack it

- To SSH to a device:

  - Open MobaXTerm

  - Press on the *Start local terminal* button

  - ```bash
    ssh username@ipAddress
    ```

### SSH via Ethernet:

If your RC is connected to your network via an ethernet cable, you should be able to find your IP address:

- Through your Router/Gateway interface, by looking at the DHCP leases;

- Or by connecting your Nano to a monitor, keyboard and mouse, opening up a terminal and writing:

  ```bash
  ip addr show
  ```

### SSH via WiFi:

I would highly recommend this approach, so you can connect your RC to a WiFi network and take it and your laptop with you and connect to it on the fly. 

To connect it to a WiFi network, you either need to first SSH into it over ethernet, or connect it to a monitor, keyboard and mouse, and do the following:

- Connect to a WiFi network:

  ```bash
  nmcli device wifi connect YOUR-SSID password YOUR-PASSWORD
  ```

- Or make the Jetson into a hotspot so you can connect your laptop to it:

  ```bash
  nmcli dev wifi hotspot ifname wlan0 ssid HOTSPOT-SSID password HOTSPOT-PASSWORD
  ```

What I like to do is connect it to both my home network, and a hotspot on my mobile phone, so I can use it anywhere and still have Internet access on both it and my laptop. 

To do so, I use the `nmcli autoconnect.priority` property, so my home network has a higher priority than my phone hotspot, in case I forget to turn it off while I'm at home, so it doesn't eat up my data plan.

You can find all of your network connections saved in `/etc/NetworkManager/system-connections/`, which you can open up with a text editor and edit the `autoconnect.priority` property for each network. The higher the integer you assign to it, the higher the priority. 

As an example, the network connection profile for my hotspot looks something like:

```bash
[connection]
id=Hotspot
uuid=random-long-string
type=wifi
autoconnect_priority=2 # The home network has a priority of 3, in my case
permissions=
```

If your Nano keeps dropping the connection for some reason, try disabling the power saving mode found in `/etc/NetworkManager/conf.d`, using a text editor.

Also, I assumed your Nano already has the `nmcli` or the `NetworkManager` utility installed, since it, at the time of writing, comes pre-installed with any Ubuntu distro. If, for some reason, you don't have it, you can install it using `sudo apt install network-manager`.

After connecting your Nano to a WiFi network you want, find out its IP Address by opening up a terminal and typing:

```bash
ip addr show
```

#### Now you can use your SSH client and SSH into the Nano, type in your username and password and you're ready to follow the rest of the tutorial.

## Dependencies

Open up a terminal on your Nano and install the following dependencies:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential python3 python3-dev python3-pip libhdf5-serial-dev hdf5-tools nano ntp
```

## Set up a Virtual Env

```bash
# Install the venv package
pip3 install virtualenv
python3 -m virtualenv -p python3 env --system-site-packages
# Activate the venv automatically at boot
echo "source env/bin/activate" >> ~/.bashrc
source ~/.bashrc
```

## Compiling and installing OpenCV

First, since OpenCV needs more than 4GB of RAM to be built from source, and our Jetson Nano just doesn't have that much RAM, we have to define some swap space to prevent it from going bonkers while compiling it:

```bash
# Allocates 4G of additional swap space at /var/swapfile
sudo fallocate -l 4G /var/swapfile
# Permissions
sudo chmod 600 /var/swapfile
# Make swap space
sudo mkswap /var/swapfile
# Turn on swap
sudo swapon /var/swapfile
# Automount swap space on reboot
sudo bash -c 'echo "/var/swapfile swap swap defaults 0 0" >> /etc/fstab'
# Reboot
sudo reboot
```

Now, we need to get all the prerequisites needed to build OpenCV from source:

```bash
# Update
sudo apt-get update
sudo apt-get upgrade
# Pre-requisites
sudo apt-get install build-essential cmake unzip pkg-config
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python3-dev
```

Okay, let's download the source code for OpenCV which we'll be building it from:

```bash
# Create a directory for opencv
mkdir -p projects/cv2
cd projects/cv2

# Download sources
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.0.zip

# Unzip
unzip opencv.zip
unzip opencv_contrib.zip

# Rename
mv opencv-4.1.0 opencv
mv opencv_contrib-4.1.0 opencv_contrib
```

Also we'll need numpy in our virtual environment for this to work:

```bash
# Install Numpy
pip install numpy
```

We also need to make sure CMake correctly generates the OpenCV bindings for our virtual environment:

```bash
# Create a build directory
cd projects/cv2/opencv
mkdir build
cd build

# Setup CMake
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    # Contrib path
    -D OPENCV_EXTRA_MODULES_PATH=~/projects/cv2/opencv_contrib/modules \
    # Your virtual environment's Python executable
    # You need to specify the result of echo $(which python)
    -D PYTHON_EXECUTABLE=~/env/bin/python \
    -D BUILD_EXAMPLES=ON ../opencv
```

The `cmake` command shows a summary of its configuration, and you should make sure that the `Interpreter` is set to the Python executable of your virtual environment, not the base OS one.

Now, to compile the code from the build folder, run the following:

```bash
make -j2
# Install OpenCV
sudo make install
sudo ldconfig
```

{{% notice warning %}}

This will take a while. And by a while, I mean: **Go grab a cup of coffee and watch a TV Show or a movie or something** while.

{{% /notice %}}

Now we just need to link it to our virtual environment:

- cd to: `/usr/local/lib/python[YOUR.VERSION]/site-packages/cv2/python[YOUR.VERSION]` and do `ls` to find out the exact name of the `.so` we built.

- It should look something like: `cv2.cpython-[YOURVERSION]m-[***]-linux-gnu.so`

- Rename it to `cv2.so`: `mv cv2.cpython-whatever-the-full-name-is.so cv2.so`

- And finally:

  - ```bash
    # Go to your virtual environments site-packages folder
    cd ~/env/lib/python[YOUR.VERSION]/site-packages/
    # Symlink the native library
    ln -s /usr/local/lib/python[YOUR.VERSION]/site-packages/cv2/python-[YOUR.VERSION]/cv2.so cv2.so
    ```

To make sure everything works as it should, run:

```python
import cv2

# Should print 4.1.0
print(cv2.__version__)
```

## Install DonkeyCar

First, go to a directory where you'd like your stuff to be:

```bash
# Probably
cd ~/projects
```

Install the latest Donkey from GitHub:

```bash
# Clone it from GitHub
git clone https://github.com/autorope/donkeycar
cd donkeycar
# Checkout the master branch
git checkout master
pip install -e .[nano]
pip install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu==1.13.1+nv19.3
```