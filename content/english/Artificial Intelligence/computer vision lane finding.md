+++
title = "Computer Vision: Lane Finding"
menuTitle = "Computer Vision: Lane Finding"
draft = false
weight=6

+++

Remember we've showed before that our CNN is taking the horizon as the input feature, and that we'll be addressing it after making a simulator mod that'll allow us to take high res images. Well, the time has come!

We'll be using some computer vision tricks to help it find the lane lines easier.

## Quick overview of what we'll be doing

Here's what it will look like. We'll be going through a detailed explanation and implementation further on, this is just a motivational example.

{{% notice note %}}

This is just a quick motivational overview, worry not, we'll get through a very detailed explanation for each step and implement everything in code.

{{% /notice %}}

Let's take this input image for an example:

![](/images/ai/preview1.jpg)

We'll begin by transforming its perspective to a birds-eye view like this:

![](/images/ai/preview2.jpg)

We'll apply some color space transformations and filters to extract only the lane lines:

![](/images/ai/preview3.jpg)

We can then fit two polynomials for the left and right lane which allow us to map the entire lane like this:

![](/images/ai/preview4.jpg)

We'll then revert the perspective to the normal car view:

![](/images/ai/preview5.jpg)

And make an overlay to visualize how the detected lane looks like:

![](/images/ai/preview6.jpg)

{{% notice tip %}}

This uses absolutely no machine learning! We'll use some form of the detected lane as an input to our neural net, which should work even better!

{{% /notice %}}

This is what it looks like on video:

<center><video controls src="/images/ai/lanefinding.mp4" autoplay loop width=100%></video></center>

# Will publish the rest today or tommorow!

