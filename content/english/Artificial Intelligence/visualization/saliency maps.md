+++
title = "Visualization: Saliency Maps"
menuTitle = "Saliency Maps"
draft = false
weight=3

+++

Another useful visual tool to see how your network works is a saliency map. They were proposed back in 1998 by Itti, Koch and Niebur, a group of neuroscientists working on feature extraction in images, in a paper titled *[A Model of Saliency-based Visaul Attention for Rapid Scene Analysis](http://www.lira.dist.unige.it/teaching/SINA_08-09/papers/itti98model.pdf)*.

In the context of Deep Learning and convolutional neural networks, they were first mentioned by the Visual Geometry Group at the University of Oxford, in a paper called *[Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps](https://arxiv.org/pdf/1312.6034.pdf)*

I won't go into excessive detail on how it works, but in our case, a saliency map will show us which pixels on the input image make the most impact on the output inferred by the network. We will make a heat map that shows us which visual features the car uses the most, in order to steer and throttle correctly. Hopefully, it should be the lane lines.

<center><video controls src="/images/ai/saliency.mp4" autoplay loop width=50%></video></center>

Now, just a day after I've implemented a script that generates a video with a saliency map, given a trained model and some input data, I've noticed that Tawn Kramer (of Donkey) has already implemented a saliency map visualization, which you can generate using the `donkey makemovie` command. But since I've already made my implementation, we'll walk through it.

As a starting point, I've used this [Jupyter Notebook](https://github.com/ermolenkodev/keras-salient-object-visualisation/blob/fix_tf1.8/keras-salient-object-visualisation.ipynb) made by [ermolenkodev](https://github.com/ermolenkodev/keras-salient-object-visualisation/blob/fix_tf1.8).

I'll be using the Nvidia model we made earlier throughout the implementation. Feel free to use your own stuff in here.

## Implementing the Saliency Map vizualization

First off, we need to import all the Keras stuff we use in our model:

```python
from donkeycar.parts.keras import KerasPilot
from tensorflow.python.keras.layers import Input, Dense
from tensorflow.python.keras.models import Model, Sequential
from tensorflow.python.keras.layers import Convolution2D, Convolution2D, MaxPooling2D, Reshape, BatchNormalization
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Cropping2D, Lambda
```

Then we can copy the function that implements our model:

```python
# The ROI crop helper function
def adjust_input_shape(input_shape, roi_crop):
    height = input_shape[0]
    new_height = height - roi_crop[0] - roi_crop[1]
    return (new_height, input_shape[1], input_shape[2])

# The definition of our model
# Also, be sure to name every convolutional layer you have as "convx" (x ∈ ℕ)
def customModel(num_outputs=2, input_shape=(160,120,3), roi_crop=(0,0)):

    input_shape = adjust_input_shape(input_shape, roi_crop)
    img_in = Input(shape=input_shape, name='img_in')
    x = img_in
    
    # Dropout rate
    keep_prob = 0.5
    rate = 1 - keep_prob
    
    # Convolutional Layer 1
    x = Convolution2D(filters=12, kernel_size=5, strides=(2, 2), activation='relu', name="conv1")(x)
    x = Dropout(rate)(x)

    # Convolutional Layer 2
    x = Convolution2D(filters=24, kernel_size=5, strides=(2, 2), activation='relu', name="conv2")(x)
    x = Dropout(rate)(x)

    # Convolutional Layer 3
    x = Convolution2D(filters=48, kernel_size=5, strides=(2, 2), activation='relu', name="conv3")(x)
    x = Dropout(rate)(x)

    # Convolutional Layer 4
    x = Convolution2D(filters=64, kernel_size=3, strides=(1, 1), activation='relu', name="conv4")(x)
    x = Dropout(rate)(x)

    # Convolutional Layer 5
    x = Convolution2D(filters=64, kernel_size=3, strides=(1, 1), activation='relu', name="conv5")(x)
    x = Dropout(rate)(x)

    # Flatten Layers
    x = Flatten()(x)

    # Fully Connected Layer 1
    x = Dense(100, activation='relu')(x)

    # Fully Connected Layer 2
    x = Dense(50, activation='relu')(x)

    # Fully Connected Layer 3
    x = Dense(25, activation='relu')(x)
    x = Dense(10, activation='relu')(x)
    x = Dense(5, activation='relu')(x)
    outputs = []
    
    for i in range(num_outputs):
        outputs.append(Dense(1, activation='linear', name='n_outputs' + str(i))(x))
        
    model = Model(inputs=[img_in], outputs=outputs)
    
    return model
```

We can then initialize the model and pass the weights we previously trained to it:

```
model = customModel()
# Pass the path to your trained .h5 file here
model.load_weights('nvidia.h5')
```

Now we can define just the convolutional layers we're interested in visualizing:

```python
img_in = Input(shape=(160,120,3), name='img_in')

x = img_in
x = Convolution2D(filters=12, kernel_size=5, strides=(2, 2), activation='relu', name="conv1")(x)
x = Convolution2D(filters=24, kernel_size=5, strides=(2, 2), activation='relu', name="conv2")(x)
x = Convolution2D(filters=48, kernel_size=5, strides=(2, 2), activation='relu', name="conv3")(x)
x = Convolution2D(filters=64, kernel_size=3, strides=(1, 1), activation='relu', name="conv4")(x)
lastConvLayer = Convolution2D(filters=64, kernel_size=3, strides=(1, 1), activation='relu', name="conv5")(x)  

convolution_part = Model(inputs=[img_in], outputs=[lastConvLayer])
```

We can now set the weights of the convolutional layers we just created to the actual weights our model contains:

```python
# If you have more than 5 layers, or less than 5 layers, edit the number here
numberOfConvLayers = 5
for layer_num in range(1, numberOfConvLayers):
    convolution_part.get_layer('conv' + str(layer_num)).set_weights(model.get_layer('conv' + str(layer_num)).get_weights())
```

To get the activation values from each layer, we need to define functors for them:

```python
from tensorflow.python.keras import backend as K

inp = convolution_part.input  # input placeholder
outputs = [layer.output for layer in convolution_part.layers[1:]] # all layer outputs
functors = K.function([inp], outputs)
```

We'll also define some helper variables that we'll use for the strides, padding and the kernels while computing the visualization masks:

```python
import tensorflow as tf
import numpy as np
import pdb

# 3x3 kernel with all ones
kernel_3x3 = tf.constant(np.array([
        [[[1]], [[1]], [[1]]], 
        [[[1]], [[1]], [[1]]], 
        [[[1]], [[1]], [[1]]]
]), tf.float32)

# 5x5 kernel with all ones
kernel_5x5 = tf.constant(np.array([
        [[[1]], [[1]], [[1]], [[1]], [[1]]], 
        [[[1]], [[1]], [[1]], [[1]], [[1]]], 
        [[[1]], [[1]], [[1]], [[1]], [[1]]],
        [[[1]], [[1]], [[1]], [[1]], [[1]]],
        [[[1]], [[1]], [[1]], [[1]], [[1]]]
]), tf.float32)

# Based on the layers in your model, you should assign the kernel sizes you're using at each layer here.
# E.g. I'm using a 3x3 kernel in my last two layers, and a 3x3 in my first three layers
layers_kernels = {5: kernel_3x3, 4: kernel_3x3, 3: kernel_5x5, 2: kernel_5x5, 1: kernel_5x5}

# Same goes here for the strides you're using in your layers
layers_strides = {5: [1, 1, 1, 1], 4: [1, 1, 1, 1], 3: [1, 2, 2, 1], 2: [1, 2, 2, 1], 1: [1, 2, 2, 1]}
```

And we can finally compute the visualization masks using  [ermolenkodev's](https://github.com/ermolenkodev/keras-salient-object-visualisation/blob/fix_tf1.8) function:

```python
def compute_visualisation_mask(input_image):
    activations = functors([np.array([input_image])])
    activations = [np.reshape(input_image, (1, input_image.shape[0], input_image.shape[1], input_image.shape[2]))] + activations
    upscaled_activation = np.ones((53, 73))
    for layer in [5, 4, 3, 2, 1]: # Edit if you have a different # of layers 
        averaged_activation = np.mean(activations[layer], axis=3).squeeze(axis=0) * upscaled_activation
        output_shape = (activations[layer - 1].shape[1], activations[layer - 1].shape[2])
        x = tf.constant(
            np.reshape(averaged_activation, (1,averaged_activation.shape[0],averaged_activation.shape[1],1)),
            tf.float32
        )
        conv = tf.nn.conv2d_transpose(
        	x, layers_kernels[layer],
            output_shape=(1,output_shape[0],output_shape[1], 1), 
            strides=layers_strides[layer], 
            padding='VALID'
        )
        with tf.Session() as session:
            result = session.run(conv)
        upscaled_activation = np.reshape(result, output_shape)
    final_visualisation_mask = upscaled_activation
    return (final_visualisation_mask - np.min(final_visualisation_mask))/(np.max(final_visualisation_mask) - np.min(final_visualisation_mask))
```

And the only thing we need to implement is the code to animate the results and save them as a video:

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import display, HTML

def save_movie_mp4(image_array, filename='output.gif', fps=30):
    dpi = 72.0
    xpixels, ypixels = image_array[0].shape[0], image_array[0].shape[1]
    fig = plt.figure(figsize=(ypixels/dpi, xpixels/dpi), dpi=dpi)
    im = plt.figimage(image_array[0])

    def animate(i):
        im.set_array(image_array[i])
        return (im,)
    
    writer = animation.PillowWriter(fps=fps)
    anim = animation.FuncAnimation(fig, animate, frames=len(image_array))
    anim.save(filename, writer=writer)
```

We can now finally pass our model and our input data to the program and let it create the Saliency Map video for us:

```python
import glob, re, time, datetime
# The path to your dataset
pathToData = 'data/tub/'

# Output video name
output = "saliency.gif"

# Output FPS
fps = 60

# Number of frames you want to use
numberOfFrames = 600

def sort_human(l):
    convert = lambda text: float(text) if text.isdigit() else text
    alphanum = lambda key: [convert(c) for c in re.split('([-+]?[0-9]*\.?[0-9]*)', key)]
    l.sort(key=alphanum)
    return l

inputImages = []
alpha = 0.004
beta = 1.0 - alpha
counter = 0
print("Generating %ds of video." % (numberOfFrames/fps))
accumulatedTime = 0
start = time.time()
for path in sort_human(glob.glob(pathToData + '*.jpg')):
    inputImage = cv2.imread(path)
    salient_mask = compute_visualisation_mask(inputImage)
    salient_mask_stacked = np.dstack((salient_mask,salient_mask))
    salient_mask_stacked = np.dstack((salient_mask_stacked,salient_mask))
    blend = cv2.addWeighted(inputImage.astype('float32'), alpha, salient_mask_stacked, beta, 0.0)
    inputImages.append(blend)
    counter += 1

    if counter >= numberOfFrames:
        break

    elif counter % 100 == 0:
        end = time.time()
        accumulatedTime += end - start
        remainingSeconds = (accumulatedTime/counter)*(numberOfFrames-counter)
        print("Generated %d/%d frames." % (counter, numberOfFrames))
        print("Estimated time left: %dm:%ds." % divmod(remainingSeconds, 60))
        print("Runtime so far: %dm:%ds." % divmod(accumulatedTime, 60))
        start = time.time()
```

And save the gif:

```python
save_movie_mp4(inputImages, output, fps)
```

{{%attachments style="grey" title="You can download the above code as an ipynb here." pattern=".*ipynb" /%}}

## The results

The output video I got using the Nvidia model we made earlier and the dataset we downloaded:

<center><video controls src="/images/ai/saliency.mp4" autoplay loop width=50%></video></center>

We can see that the car indeed uses the lane lines, but it also uses the horizon as a feature a lot. That's quite interesting. We can get rid of that problem using a ROI crop or by implementing some computer vision feature extraction/engineering, which we'll do right after we make a high res version of the simulator. :)

We can also see that it's far more interested in the right line, than the middle (left) one. That's because, in general, the car tends to go to the right, since we're driving around the circuit clockwise. We need to do some data augmentation to solve this issue, which we'll also do a bit later.