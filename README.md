# GSoC_Ideas
My ideas and proposal for the GSoC 2018 project: Native Python and Processing (p5py)

This repository contains the following projects and programs:
1. An image modifier made using Processing-Java (Image_Modifier.pde)
2. A program made using pyOpenGL, to display cubes of various sizes and colours appearing at random places in 3D space. The camera moves through the 3D space and you can navigate up, down, left and right using the arrow keys. (infinite_cubes.py)  

I have made a few changes to my GitHub repo [p5](https://github.com/AliabbasMerchant/p5) and have added a Prototype for `PShape` and the code for `TimeDate`.  

* The file [`TimeDate.py`](https://github.com/AliabbasMerchant/p5/blob/master/p5/sketch/TimeDate.py) contains p5py equivalents of all the Processing (Java) Date and Time functions.
* The file [`PShape.py`](https://github.com/AliabbasMerchant/p5/blob/master/p5/core/PShape.py) is a prototype of the PShape module to be made during the coding period in GSoc 2018. The prototype currently supports dynamic shape creation and dynamically editing the vertices of a shape.

The working example of PShape and TimeDate can be found here: [link] (https://github.com/AliabbasMerchant/p5/blob/master/PShape_Demo.py)  
Also, I have created a Processing (Java) example to demonstrate the similarities: [link] (https://github.com/AliabbasMerchant/p5/tree/master/PShape_Demo)

The demo videos for PShape can be found here: [link](https://drive.google.com/drive/folders/15PyKUEQSN6_HJeLRgawOSQtcdFkzzb84?usp=sharing)  
The videos in the Google Drive folder are:  
1. [PShapeMouse](https://drive.google.com/open?id=18tj6YxRCF_0vsteMJ6TBIt_ey6V0VDCL): A vertex of the PShape is dynamically edited, to follow the mouse movements.
2. [PShapeRandom](https://drive.google.com/open?id=1Eo6Yv5BtSjba89UeEiHl6fg8S7VLSyUy): A vertex of the PShape is dynamically edited, and assigned random co-ordinates
3. [PShapeTimeVarying](https://drive.google.com/open?id=1ge9v334IsC0xuAsClwXHxKCfQP-_UiGC): A vertex of the PShape is dynamically edited, to move linearly with time (Also, this uses the `millis()` function of the `TimeDate` module).  
All of the above videos contain two programs each, one made in p5py (using the code in my repo [p5](https://github.com/AliabbasMerchant/p5)) (the window named p5) and the other made in Processing-Java (the window named PShape_Demo), so as to demonstrate the similarities between the two.
