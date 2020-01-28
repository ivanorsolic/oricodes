+++
title = "Simulator mod: Custom RC model"
menuTitle = "Custom RC model"
draft = false
weight=2

+++

If you want to get better data for your RC, you should edit the default model that comes with the simulator. Most notably, you should edit the camera position, resolution and field of view. You can also add multiple cameras and edit the center of mass of your vehicle, as well as any other properties you think would make a difference if you wanted to use the simulator to pre-train the weights for your RC.

Let's see how we can do that.

## Editing the camera

Open up the Unity project and open the *donkey* prefab, found in Assets/Prefabs/donkey.fbx.

In the prefab hierarchy, select the ***cameraSensorBase*** and then select the ***CameraSensor***.

On the right, in the *Inspector* panel, under the **Camera** settings, you can edit a bunch of settings related to it. I'd suggest you edit the FOV value to match the FOV your real camera has, and I'd recommend disabling the Fisheye and Post Processing scripts.

You can also move the camera in different positions using the move and rotate tools ![MOve/pivot icons](/images/ai/toolicons.png) and the editor on the center of the screen, and pivot/angle it to match your real RC.

## Testing it out

You can open up any a scene, e.g. the *warehouse* scene, zoom up to the track and drag and drop your prefab onto it. After dropping it on the track, select the camera sensor to see what its output looks like:

![Camera Preview](/images/ai/cameraPreview.png)

## Adding additional parts and changing the center of mass

If you'd like, you can always create a custom 3D model of the electronics that are on your RC and insert it into the default donkey model. You can use the default *donkey.fbx* that comes with the simulator and edit it, or you can make your own from scratch.

After creating a 3D model, drag and drop it into the *Models* folder. Now open up the *donkey* prefab and drag your model wherever you'd like on the *Hierarchy* panel. I'd recommend putting it inside the *donkey* element. You can then position and resize your elements to fit them on the RC.

If you want to reorder any elements or edit them individually, but the element looks blue, like this *power bank v1* element, you can right click on it and select *unpack prefab*:

![Packed Prefab](/images/ai/packedprefab.png)

Then you'll be able to move individual parts around.

If you've made significant changes to the model, and added a lot of parts, your RC's center of mass has probably changed, and you should reflect that in the simulator by changing the defined center of mass, since you want it to realistically handle corners just as it would in real life, and if your center of mass is higher up because you've added a bunch of stuff on your RC, it could perform great in the simulator but tip over in real life.

You can find the ***centerOfMass*** element inside the *donkey* prefab, and move and pivot it around just like any other element:

![image-20200127231835076](/images/ai/centerofmass.png)

You can now build your simulator and try your model out.