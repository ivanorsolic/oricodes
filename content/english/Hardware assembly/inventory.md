+++
title = "Hardware inventory"
menuTitle = "Inventory"
draft = false
weight=10

+++

Let’s start with a list of all of the hardware I’ll be using through this tutorial, and of course, with the money shot:

![inventory](/images/hardware/inventory.jpg)

## RC Car kit

The RC Car I went with was the Tamiya TT-02, which came prebuilt and even included an receiver and a remote, [for just a bit over 100€](https://www.lindinger.at/at/fahrzeuge-und-boote/modelle/onroad-und-drift-autos/tamiya-tt-02-chassis-aufgebaut-1-10-ep-4wd-mit-2-4ghz-sender). Very lucky!

![Tamiya](/images/hardware/tamiya.png)

The reason I went with this is that it was just such a good deal for such a car. It’s 1:10 scaled, so I’ll have plenty of real estate for hooking all sorts of electronics on it, and it’s a really good car for on road driving. There’s plenty of mods available for it and plenty of extra parts, which I even got with it, such as extra wheel bases or additional mounting arms. After working with it for a couple months now, I’d highly recommend it.

{{% notice warning %}}

Be sure to pay attention to the level of pre-assembly your kit comes with. There are kits that can take days to assemble if you’re doing all by yourself, and there are kits that are completely pre-built out of the box (commonly denoted RTR - ready to run). If you’re up for a challenge, get a Tamiya kit that isn’t prebuilt. They have great instructions and it’s fun to get to know your car inside out. The difficulty of assembly also varies by car, and is often denoted on the box or in the instructions.

{{% /notice %}}

## Charger and batteries

I got a Carson Expert Charger LiPo Compact 3A set, with a Carson 3000mAh LiPo battery, [for under 30€](https://www.lindinger.at/en/batteries/chargers-und-power-supplies/chargers-230v/carson-charger-set-lipo-compact-3a-charger-2-4s-230v-lipo-7.4volt-3000mah), which is also pretty sweet!

![Charger](/images/hardware/charger.png)

{{% notice tip %}}

I’d very much recommend getting a ‘smarter’ charger, with a balancing connector so you know exactly how much your battery is charged. You’ll want to store them at around 70% of their capacity if you’re not using them.

{{% /notice %}}

I also went ahead and got an extra [Fconegy 6000 mAh](https://www.amazon.com/Fconegy-6000mAh-Battery-hardcase-Bullet/dp/B0791ZN8Z9) LiPo battery for around 25€.

![Fconegy](/images/hardware/battery.png)

And of course, per my warning on the batteries section at the RC Car primer, I got a [LiPo alarm](https://www.conrad.de/de/p/reely-lipo-checker-geeignet-fuer-zellen-2-8-1-st-1511388.html) and a [charging bag](https://www.conrad.de/de/p/reely-lipo-safety-bag-geeignet-fuer-zellen-2-1-st-1420590.html) to avoid any unnecessary explosions, housefires or general mayhem. It’s just an extra 20€ or so, but it’s very much so worth it.

![](/images/hardware/lipo.jpg?height=250px)

![](/images/hardware/lipo bag.png)



 

## Jetson Nano

Ah, the 🧠z of the project, the [Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/jetson-nano-developer-kit). It’s pretty much the way to go for 100€ or so, it packs a pretty decent GPU, 4x USB 3.0 ports, a *real* gigabit ethernet port, and you can punch a bit more power into it with a jumper and a 4A@5V power source with a barrel jack cable.

![](/images/hardware/jetson.png)

### Jetson Nano: MicroSD card

You’ll be needing a microSD card to run your Jetson Nano OS, and you should try getting a faster on (at least Class 10, preferably UHS-II or faster :)). 

I got an [Sandisk Extreme 64GB A2](https://www.amazon.de/SanDisk-Extreme-microSDXC-Speicherkarte-SD-Adapter/dp/B07FCMWCVB/ref=dp_ob_title_ce), UHS-3 card for about 25€.

![](/images/hardware/microsd.jpg?height=250px)

{{% notice tip %}}

You don’t have to get a huge (in terms of storage) microSD if you’re planning on using an external SSD with your Jetson. I’d say 32GB would be just enough, but the price difference isn’t that big, so you can go for the 64GB version just ‘cause.

{{% /notice %}}

### Jetson Nano: Noctua Fan

If you’re planning to run the Jetson at fully capacity (4A barrel jack mode), which you most definitely should, it’s gonna need some help stayin’ cool, so you should get a fan for it. 

You can pretty much get any 5V, 4-pin PWM, 40x40mm size fan, but I’d very much recommend going for a Noctua NF-A4 fan. You can choose between the 10mm or 20mm version, just be sure to get the 5V version of the fan and not the regular 12V one. 

![Noctua](/images/hardware/noctua.jpg?height=400px)

[You can get the 20mm version for about 10-15€.](https://www.amazon.de/Noctua-NF-A4x20-5V-Premium-3-polig/dp/B072Q3CMRW/ref=sr_1_6?__mk_de_DE=ÅMÅŽÕÑ&keywords=noctua+fan&qid=1564320839&s=computers&sr=1-6)

{{% notice tip %}}

You’ll also want a couple of self-tapping M3 screws or regular M2 or M2.5 screws with nuts for mounting the fan to the heatsink. I’d recommend going with the self-tapping M3 screws, it’s so much easier. Also watch out for some aluminum shavings when you mount the fan on it, you wouldn’t want them getting to the circuitry below and causing mayhem.

{{% /notice %}}

{{% notice tip %}}

Also, if you’re going with the 20mm version, get 25mm long screws. If you’re going with the 10mm version, get 15mm long screws.

{{% /notice %}}

### Wireless LAN and Bluetooth

There are two options on getting your Nano (and your car) wirelessly connected:

- An M.2 WiFi + BT card
- USB WiFi and BT adapters

I’d highly recommend going for the M.2 option. I got the Intel 8265 card for about 10€. 

![](/images/hardware/intel.jpg?height=250px)

{{% notice info %}}

If you’re getting the M.2 variant, you’ll need two antennas and an IPEX MHF4 to RP-SMA adapter cable. Pay attention to the connector types, it’s easy to get a wrong one, and vendors often misuse the labels, mixing IPEX, uFL, IPAX, IPX, MHF, and AM. Sometimes they’re right, sometimes they’re not.

{{% /notice %}}

{{% notice warning %}}

The Jetson Nano has a **M.2 key E** slot, just to keep in mind when getting a card. It also doesn’t work with NVME SSDs, if you’re wondering.

{{% /notice %}}

{{% notice warning %}}

Beware of the model of the m.2 card you’re getting. At the time of writing, the Jetson Nano SD Card Image natively supports **only the 8265**. Technically, you should be able to use any Intel card older than the 8265 since it’s supported in the 4.9 kernel, but some people had issues running even the 7265. If you’re up to it, you can build [the core14 branch](https://git.kernel.org/pub/scm/linux/kernel/git/iwlwifi/backport-iwlwifi.git/log/?h=release/LinuxCore14) on the backports git, but if you know how to do that, you probably don’t need me telling it about you. 

{{% /notice %}}