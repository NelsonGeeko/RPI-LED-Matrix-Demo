# RPI-LED-Matrix-Demo

Ongoing Repo to document LED Matrix Demo, to be converted into K8s Demo for Digital Signage.

## Components needed
Single RPI - Prefer RPI 4, but my orgiginal testing of the LED Matrix was PI 3 B+ with WiFi. <br>
https://thepihut.com/products/raspberry-pi-4-model-b?variant=31994565689406

Waveshare 64x64 Matrix pannel<br>
https://www.waveshare.com/rgb-matrix-p3-64x64.htm

5v 4A Power supply - I used a bench PSU for testing, LED pannel can consume a lot of current especially if you choose to Daisy chain.<br>
https://thepihut.com/products/mean-well-5v-4a-20w-power-supply-gst25a05-p1j?variant=41611596562627&currency=GBP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=CjwKCAjwu4WoBhBkEiwAojNdXm2bPy5dsB9RV-EqaoIY3luF8vK2_lJJ9ZjYkhK2vhTdz7JpFWXgmBoCCFwQAvD_BwE

optional PI Hat - I did not use one, i used official GPIO mapping to the RPI (Mapping can be found at the bottom of this page.<br>
https://thepihut.com/products/adafruit-rgb-matrix-bonnet-for-raspberry-pi-ada3211


## Libs needed
I used the hzeller/rpi-rgb-led-matrix libary for initial testing.<br>
https://github.com/hzeller/rpi-rgb-led-matrix/tree/master

```shell
git clone https://github.com/hzeller/rpi-rgb-led-matrix.git
```

To display images, GIFs or Videos with the hzeller lib you will need to install `libgraphicsmagick++-dev` and `libweb-dev`.

## Python Scripts

As a part of the hzeller Liberary it will come with Python coomponents, these are loacted at `/bindings/python` within this dir there are samples to test and try.

To ensure that this works you will need to install python on the Pi.

```shell
sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)
```
Currently, this GH Repo has a script to run a single image, the plan is to make this configurable using env varibles, and to roll out deployments using Helm and CD.

## Note for using GPIO output without hat
If you are using the hzeller lib, commands to run some of the demos and Utils will require `--led-rows=64`, `led-cols=64` and `led-no-hardware-pulse` flags set.


### GPIO Mapping for RPI

Then for each first panel of a chain there is a set of
(R1, G1, B1, R2, G2, B2) that you have to connect to the corresponding pins.
They are marked `[1]`, `[2]` and `[3]` for chain 1, 2, and 3 below.

If you only connect one panel or have one chain, connect it to
`[1]` (:smile:); if you use parallel chains, add the other `[2]` and `[3]`.

To make things quicker to navigate visually, each chain is marked with a
separate icon:

`[1]`=:smile:, `[2]`=:boom: and `[3]`=:droplet: ; signals that go to all
chains have all icons.

|Connection                        | Pin | Pin |  Connection
|---------------------------------:|:---:|:---:|:-----------------------------
|                             -    |   1 |   2 | -
|             :droplet: **[3] G1** |   3 |   4 | -
|             :droplet: **[3] B1** |   5 |   6 | **GND** :smile::boom::droplet:
|:smile::boom::droplet: **strobe** |   7 |   8 | **[3] R1** :droplet:
|                              -   |   9 |  10 | **E**    :smile::boom::droplet: (for 64 row matrix, 1:32)
|:smile::boom::droplet: **clock**  |  11 |  12 | **OE-**  :smile::boom::droplet:
|              :smile:  **[1] G1** |  13 |  14 | -
|:smile::boom::droplet:      **A** |  15 |  16 | **B**    :smile::boom::droplet:
|                             -    |  17 |  18 | **C**    :smile::boom::droplet:
|              :smile:  **[1] B2** |  19 |  20 | -
|              :smile:  **[1] G2** |  21 |  22 | **D**    :smile::boom::droplet: (for 32 row matrix, 1:16)
|              :smile:  **[1] R1** |  23 |  24 | **[1] R2** :smile:
|                             -    |  25 |  26 | **[1] B1** :smile:
|                             -    |  27 |  28 | -
|              :boom:   **[2] G1** |  29 |  30 | -
|              :boom:   **[2] B1** |  31 |  32 | **[2] R1** :boom:
|              :boom:   **[2] G2** |  33 |  34 | -
|              :boom:   **[2] R2** |  35 |  36 | **[3] G2** :droplet:
|              :droplet:**[3] R2** |  37 |  38 | **[2] B2** :boom:
|                              -   |  39 |  40 | **[3] B2** :droplet:
