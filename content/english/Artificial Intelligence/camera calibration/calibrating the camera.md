+++
title = "Camera calibration: Calibrating the camera and undistorting images"
menuTitle = "Calibrating your camera and undistorting images"
draft = false
weight=3

+++
Finally, we can actually calibrate our camera and undistort our images! 

We'll start with the real camera on our RC and then we'll also calibrate our simulator camera!

{{% notice note %}}

Once calibrated on the calibration images, you can use the same undistortion matrix for any other image that the same camera takes (given the focal length hasn't changed)!

{{% /notice %}}

## Calibrating your real camera

I'll be using my RC camera, the EleCam Explorer 4K, which has an advertised 170 degree FOV.

![My Camera](/images/ai/cam.jpg)

First, we need to print a checkerboard pattern so we can take some calibration rig photos.

There's a pretty cool [checkerboard collection](https://markhedleyjones.com/projects/calibration-checkerboard-collection) by Mark Hedley Jones which you can use to generate a checkerboard/chessboard pattern you like. I'll be using [this one](https://markhedleyjones.com/storage/checkerboards/Checkerboard-A4-25mm-10x7.pdf):

![img](/images/ai/checkerboard.jpg)

{{% notice info %}}

If you use another pattern, make sure to update the number of inner corners for the rows and columns in the `getObjectAndImagePoints` function we made earlier.

{{% /notice %}}

After printing it out on an A4 paper, you should take at least 10 photos of it in different angles, e.g.:

![image-20200128205334523](/images/ai/calibrationImage2.jpg)

![image-20200128205426724](/images/ai/calibrationImage1.jpg)

Also, most action cams with a FOV as large as this one (170°) will have some built-in distortion correction, probably named something like *fisheye correction* or *adjust*:

![Fisheye adjust](/images/ai/fisheye adjust.png)

I've intentionally left mine off, to show how distorted the images are by default at such a big FOV, and to show that they can be undistorted even for those whose camera doesn't have a built-in option to do so.

After copying the images to my `calibration_images` folder and calling the `getObjectAndImagePoints` script, here's what the detected image points look like:

![image3](/images/ai/calibration2.jpg)

![image7](/images/ai/calibration1.jpg)

After getting the image points, we can call the ***calibrateCamera*** function once, and then ***undistortImage*** to undistort our images for as many new images as we want, here's what the previous two image look like undistorted:

![testUndistort](/images/ai/testUndistort2.jpg)



![testUndistort](/images/ai/testUndistort.jpg)

And that's it! You can undistort every image like this before you input it to the neural network. Here's what the code could look like:

```python
# At the beginning of run
getObjectAndImagePoints()

calibrateCamera(inputImage.shape[1::-1])
undistortedImage = undistortImage(inputImage)
# Pass it along to the NN
```

## Calibrating the simulator camera

First, we need to put a checkerboard object into the simulator so we can take photos of it.

# TODO