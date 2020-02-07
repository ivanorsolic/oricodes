+++
title = "Adding behaviours: automated lane changing"
menuTitle = "Behaviours: Lane Changing"
draft = false
weight=13

+++

The only thing left to do, in order to test my idea with multiple specialized networks converging into a final decision layer, is to implement the behavioural specialized network.

This is what the model will look like:

![nnWithBehaviour](/images/ai/behaviourNet.png)

The behavioural part of the network can be seen just before the 100-unit dense layer.

Here it is in action: **note the lower left terminal to see when I pressed the button to change lanes**

<center><video controls src="/images/ai/changingLanes.mp4" autoplay muted loop width=100%></video></center>


Let's get to it!

### Donkey and behaviours

After a bit of research, I found that other people have already tried (and succeded) to implement behaviours such as passing using Donkey. There's even a behavioural model sitting in the `keras.py` script, which is great.

There's also some out of the box support for behaviours, but worry not, I'll walk you through it.

Also, the behavioural part of the network is pretty small, but it works! It's based off other behavioural networks I've found people used with Donkey. You can use the built-in one if you'd like to quickly get your feet wet.

### Getting behavioural data

If we want to train the network for certain behaviours, we have to give it labeled training data with said behaviours. 

We can do this many ways, we can even make the neural network trigger certain behaviours, e.g. when a classifier detects a stop sign, trigger the stop behaviour. But for this PoC, a simple button click on our controller will do.

I was going to implement a class that took in a list of possible behaviours, that would set certain behaviours to currently active on a button press, and wrote the currently set behaviour to the training data json file. And, for the I don't know-what-time now, I've found that Donkey has just such a class already implemented. And since it's there and it's really easy to understand and use, why wouldn't we.

You can find it in `donkeycar/parts/behavior.py`. It takes in a list of possible behaviors and provides methods to set the behaviours from the list iteratively and a method to explicitly set a behaviour. Beautiful.

If we set the `TRAIN_BEHAVIORS` variable in `myconfig.py` to be `True`, the `myconfig.py` script adds the behaviour part to the current vehicle, initializing it with a list of behaviours we set in the config file using the `BEHAVIOR_LIST` variable.

Say we've defined a behaviour list:

```python
behaviours = ['Left_Lane', 'Right_Lane']
```

The behaviour class will outputs the current behaviour state as an index, a one-hot array and it's label as the following key/value pairs to the dataset file:

```json
"behavior/state": 0, 
"behavior/label": "Left_Lane", 
"behavior/one_hot_state_array": [1.0, 0.0]
```

To map a controller button as a trigger for incrementing or setting the behaviours, we can use the `set_button_down_trigger` from the `controller.py` script:

```python
def set_button_down_trigger(self, button, func):
    # assign a string button descriptor to a given function call
    self.button_down_trigger_map[button] = func
```

We would pass the button we want (the name we've used in our custom mapping, e.g. 'L1') along with the method that increments or sets the behaviour from `behavior.py`.

You can also use an axis as a trigger or a button up event as a trigger.

And that's pretty much it, Donkey will just append the behavioural data to our dataset!

### Adding the behavioural subnetwork

It's actually pretty simple, the new part in the Keras model should look something like:

```python
# New input layer
behaviourInput = Input(shape=(numberOfBehaviourInputs,), name="behaviourInput")

# ConvNet parts ...

# Behavioural net
z = behaviourInput
z = Dense(numberOfBehaviourInputs * 2, activation='relu')(z)
z = Dense(numberOfBehaviourInputs * 2, activation='relu')(z)
z = Dense(numberOfBehaviourInputs * 2, activation='relu')(z)

# Concatenating the convolutional networks with the behavioural network
o = Concatenate(axis=1)([z, c])
o = Dense(100, activation='relu')(o)
o = Dense(50, activation='relu')(o)

# Output layers ...

# Update the model inputs
model = Model(inputs=[imageInput, laneInput, behaviourInput], outputs=[steering_out, throttle_out]) 
```

You just need to add the number of behaviour inputs as an input to the class constructor, and the behavioural data as an input to the model. This way we can easily train any number of behaviours we'd like.

### Training the model

After training it on a smaller dataset of around 7k records with about 20 lane changes, I got the following:

![image-20200207012336427](/images/ai/trainingBehaviour.jpg)

### Further ideas

Now that we've seen that we can actually train behaviours like this, I'm planning on creating a behaviour that uses an object tracker/classifier network to trigger certain behaviours. So let's make that network!