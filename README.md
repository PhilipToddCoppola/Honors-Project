Utilising Python Programming to Build a 3D Particle Based Model of a Developing Root
======

### Background

The geology of the earth is incredibly diverse. Soils around the world vary in moisture, aeration, pH, and consistency (to name a few) that can creates difficult circumstances for crop plants to embed their roots into. How a plant accomplishes this task is a key interest to scientific research. 
Basic root growth processes are not well established. From the apical meristem, located at the tip of the root just behind the protective root cap, cells continuously divide to become undifferentiated root cells. Through the process of elongation the cell pushes itself into the soil whereupon they will eventually become specialised. Growth from the apical meristem is known as primary growth whereas a secondary growth increases the diameter of the root from the lateral meristem. There has been much work on building 2D models of this process yet 3D models are less common. 

The aim of my project is to generate software tools to model and visualise in three dimensions how a single root develops and pushes through soil. The model will represent individual cells moving, expanding and dividing. The program will allow visualisation of various cell types, their position and movement during growth

### Method

I will develop a program based on the programming language python. Numerical computations of cell positions and shapes will be carried out using scientific libraries such as Scipy and NumPy. Once the positions and shape of cells have been computed, the program will then provide 3D visualisation of the architecture of cells in the tissue and how these are formed as a result of cell activity.  A 3rd party module such as Pygame, PyOpenGL, PyODE or vPython will be used for 3D visualisation of cell architectures. Such libraries allows the user to create complex geometric shapes and add dynamic variables such as gravity or mathematical trajectories (using pythons inbuilt math module) upon them. By using this technique, coding cells as individual particles, allows the ability to render each cell and manipulate them through all cycles of development. 

###Pre-Project Testing 

I have tested various 3D visualisation modules and have decided to use vPython for my project because it is more adapted to fast prototyping and is designed to work with NumPy effortlessly. I am currently exploring ways to control the shape of the objects to allow better parameterisation of the cell geometry. In the future, the program will implement cell movement, cell deformation and cell division. Data from the literature, or directly measured from data available on site, will be used. Application of this work includes the simulation of entire root meristems with biological processes such as gene expression, biochemical pathways or cell wall biophysics as factors driving the changes in cell architectures. Computational techniques such as Smooth Particle Hydrodynamics could be used to model such processes. Work would likely migrate this design to a compiled programing language such as C++ to gain speed and to use techniques such as multithreading. 

Early Model Test of vPython: 
![alt text](http://i.imgur.com/Fddxb7i.png?1 "Early Model Test")

### Why Model?

The people of the world are becoming environmentally friendly. Agriculture is being urged more and more by the governments to use less damaging fertilisers and reduce the usage of water. However, this has a negative effect by reducing the output of crops and, in a world where the human population has surpassed 7 billion inhabitants, food shortage is an ever increasing likelihood. 

This catch-22 scenario has caused plant researchers to find alternative methods for plants to obtain their resource; engineering the roots to be able to hunt down all the available nutrients in the soil.
As well as hunting nutrients, the ability for the root to penetrate the soil is of great interest. With reports of increasing global temperatures and drier lands, soils will become tougher and provide further physical constraints for roots to develop but how does modelling aid the study of root development and edaphology?

Modelling assists the ability to predict how roots may overcome certain physical restrictions. One aspect of this is to the capability to look at the cellular level and understand the events occurring. How a plant has the ability to pierce harder soils can be investigated on a genotypic scale which can further research for crop yielding plants such as barley or wheat.
In essence, it allows the breeder to develop new crops that are more adapted to future climates before such events occur in the real world potentially forecasting food shortage and allowing genetic adaptions to transpire.
By using computers rather than living samples, researches can input variables into the system to generate a result in possibly seconds rather than days if it was a living plant. This can significantly reduce costs and time wasted on waiting for results but still provide the necessary data to enhance crop yield.  

Github Help
====

###Navigation

Within the ROOT directory is 3 more folders. Raw source code is found in the "Main Code" directory while older test codes can be found in the appropriately named "Old Code" directory. The "Documentation" directory contains the [Beemster & Baskin 1998](http://www.plantphysiol.org/content/116/4/1515 "Beemster et al Paper") paper where I got my data from,a logistic curve (figure 1) which is represents the velocity of my cells where they are located on the root, and finally a png image from my very early test on the vpython module.

If you wish to view all history of my code but are unsure how then please follow these steps:

1. Navigate to the ROOT directory and click the small clock image on the top right.This will bring up all the commits to that directory. ![alt text][img1]
2. Clicking on the small grey box beside the name of the commit will bring up a short description of the changes made. ![alt text][img2]
3. Clicking on the name itself will bring up a much more detailed display of what has been changed.![alt text][img3]

[img1]:http://i.imgur.com/Hnf3a3M.png
[img2]:http://i.imgur.com/aTX4XI8.png
[img3]:http://i.imgur.com/3bvTaLD.png

### Running The Script

Work is being done to implement a simple to run exe file to display the final product without the need to download and install any programs. In the meantime if you wish to run the code you will need to install [Python 2.7.x](https://www.python.org/downloads/ "Downloads Page") and the [vpython](http://vpython.org/contents/download_windows.html "vPython Download for Windows") Module

### Contributors

With thanks to Dr Lionel Dupuy for constant guidance throughout the project and to Grant Johnstone and Scott McCrimmon for keeping me sane and caffeinated from start to end. 


Licence
=======

Copyright 2014 Philip Todd Coppola

Licenced under the Apache Licence, Version 2.0 (the "Licence");
you may not use this file except in compliance with the Licence.
You may obtain a copy of the Licence at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the Licence is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the Licence for the specific language governing permissions and
limitations under the Licence.
