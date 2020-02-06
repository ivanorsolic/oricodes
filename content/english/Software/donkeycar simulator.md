+++
title = "DonkeyCar Installation: The Simulator"
menuTitle = "DonkeyCar: Simulator"
draft = false
weight=13

+++

{{% notice tip %}}

Even if you don't have an RC car, you can start here and follow the rest of the project by just substituting the RC car with the simulator! 

{{% /notice %}}

<center><video controls src="/video/simulator_trim.mp4" autoplay loop width=100%></video></center>
This is one of the coolest parts of DonkeyCar for me, and probably one of the most useful ones. 

It's also a good way to get your feet wet with this kind of a project without building an actual RC. If it turns out you like it, you can always go back to the beginning and build an actual platform.

And if you're thinking: *boo, why use a simulator when we have a real RC car!*, remember, **[even Tesla uses a simulator](https://youtu.be/Ucp0TTmvqOE?t=7371)**. 

It is true that, **as Andrej Karpathy says:** ***there is no substitute for real data***, the simulator gives us a chance to rapidly prototype and even test multiple models at once. It also gives us an environment where we don't have to worry about the physical RC crashing into something or hurting someone. Also, if you wanted to use reinforcement learning, would you really be willing to let your RC smash into the wall for episodes and episodes until it learns basic stuff?

Also, if you've got the time, **do take a look at the [Tesla Autonomy Day stream](https://www.youtube.com/watch?v=Ucp0TTmvqOE)**, it's a goldmine of valuable insights on **how they actually do stuff that <u>actually drives on actual roads</u>** (!).

#### Let's get it up and running:

- Download and unzip the simulator for your platform from the [DonkeyCar GitHub release page](https://github.com/tawnkramer/gym-donkeycar/releases)

- Place the simulator into your projects folder (where you cloned the Donkey repo)

- Install DonkeyGym:

  ```bash
  cd ~/projects
  git clone https://github.com/tawnkramer/gym-donkeycar
  conda activate donkey
  pip install -e gym-donkeycar
  ```

- Create a new Donkey application for your simulator:

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

  - You can choose different architectures or create your own by going into the DonkeyCar parts folder (/projects/donkeycar/parts/) and opening up the ***keras.py*** script. 
  - You can define a new class that inherits the base class for models and implement your own neural network architecture, but we'll get to that further on in the project!
  - If you've created your own architecture/class, you can train the model using it by passing the flag --type=yourClassName
  - Some of the [built-in models](https://docs.donkeycar.com/parts/keras/) are: categorical, linear, rnn, 3d, latent, etc.
  - When using your custom model to drive the car, if you get some dimensions errors, you're probably forgetting to pass the --type flag with your class name while running it, it should fix it.

- Test your model by running

  ```bash
  python manage.py drive --model models/mymodel.h5
  ```

  - Open up your browser and go to: http://localhost:8887 and set the mode to Local Pilot and watch your car go!
- If you're using Linux, you can also pass the --js parameter and use your gamepad if it's mounted to /dev/js0
  
- [Download this big dataset](https://tawn-train.s3.amazonaws.com/log_donkey/lg_data.tar.gz) that contains 16 different venues with tape lined tracks on concrete and tile (some are on carpet and cobblestones)

  - Credits to Tawn from the [Donkey Slack channel](https://donkeycar.slack.com)

{{% notice warning %}} 

The dataset is **big**. And it contains a lot of **small files**, which means you should **pay attention where you're extracting the files**, since moving/copying them will take **a long while** since OS's don't like working with millions of small files. 

{{% /notice %}}

