+++
title = "Visualization: donkey makemovie"
menuTitle = "Donkey makemovie"
draft = false
weight=4

+++

The [`makemovie`](https://docs.donkeycar.com/utility/donkey/#make-movie-from-tub) command is a great tool to visually inspect and debug your model. Here are some example uses:

- To create just a video of the training data, with an overlay that shows steering:
  `donkey makemovie --tub=pathToYour/data/ --out=outputVideo.mp4` 

  <center><video controls src="/images/ai/makemovie1.mp4" autoplay loop></video></center>

- To create a video with an overlay of your model steering and the training data steering:
  `donkey makemovie --tub=pathToYour/data/ --out=outputVideo.mp4 `
  `--model=yourModel.h5 --type=modelType` 

  <center><video controls src="/images/ai/makemovie2.mp4" autoplay loop></video></center>

- To create a video with a saliency map and both overlays:
  `donkey makemovie --tub=pathToYour/data/ --out=outputVideo.mp4 `
  `--model=yourModel.h5 --type=modelType --salient`

  <center><video controls src="/images/ai/makemovie3.mp4" autoplay loop></video></center>