+++
title = "Installing the DonkeyCar simulator"
menuTitle = "DonkeyCar: Simulator"
draft = false
weight=13

+++

# Simulator installation

- Download and unzip the simulator for your platform from the [DonkeyCar GitHub release page](https://github.com/tawnkramer/gym-donkeycar/releases)

- Place the simulator into your projects folder (where you cloned the Donkey repo)

- Install DonkeyGym:

  ```bash
  cd ~/projects
  git clone https://github.com/tawnkramer/gym-donkeycar
  conda activate donkey
  pip install -e gym-donkeycar
  ```

- Create a new donkey application for your simulator:

  ```bash
  donkey createcar --path ~/mysim
  cd ~/mysim
  ```

- Edit the myconfig.py file inside the application folder you just created (mysim):

  ```python
  # Enables the Donkey Gym simulator wrapper
  DONKEY_GYM = True
  DONKEY_SIM_PATH = "/home/wherever/your/projects/are/DonkeySimFolder/DonkeySim.exe"
  # Choose the track you want to run, you can change this later
  DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"
  ```

- [Download this test dataset](https://drive.google.com/open?id=1A5sTSddFsf494UDtnvYQBaEPYX87_LMp) that contains data of a car recovering from dropping out from the track and some standard driving data and put it in your data folder inside your application folder (/mysim/data/)

- Train your model by running

  ```bash
  python manage.py train --model models/mymodel.h5
  ```

  - You can choose different architectures or create your own by going into the donkeycar parts folder (/projects/donkeycar/parts/) and opening up the ***keras.py*** script. You can define a new class that inherits the base class for models and implement your own neural network architecture (just take a look at the other classes, you'll get it). 
  - After creating your own architecture/class, you can train the model using it by passing the flag --type=yourClassName
  - Some of the built-in models are: categorical, linear, rnn, 3d, latent, etc.
  - When using your custom model to drive the car, if you get some dimensions errors, try passing the --type flag along with your class name while running it, it should fix it.

- Test your model by running

  ```bash
  python manage.py drive --model models/mymodel.h5
  ```

  Use --type=yourCustomClass if you're trained it using a custom class and are getting some errors.

  - Open up your browser and go to: http://localhost:8887 and set the mode to Local Pilot and watch your car go!
  - If you're using Linux, you can also pass the --js parameter and use your gamepad if it's mounted to /dev/js0

- [Download this big dataset](https://tawn-train.s3.amazonaws.com/log_donkey/lg_data.tar.gz) that contains 16 different venues with tape lined tracks on concrete and tile (some are on carpet and cobblestones)

  - Credits to Tawn from the [Donkey Slack channel](https://donkeycar.slack.com)