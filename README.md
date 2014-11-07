#Understanding root development, from cellular mechanisms, using Python and 3D particle based modelling 
================


### Background

The geology of the earth is incredibly diverse. Soils around the world vary in moisture, aeration, pH, and consistency (to name a few) that can creates difficult circumstances for crop plants to embed their roots into. How a plant accomplishes this task is a key interest to scientific research. 
Basic root growth processes are not well established. From the apical meristem, located at the tip of the root just behind the protective root cap, cells continuously divide to become undifferentiated root cells. Through the process of elongation the cell pushes itself into the soil whereupon they will eventually become specialised. Growth from the apical meristem is known as primary growth whereas a secondary growth increases the diameter of the root from the lateral meristem. There has been much work on building 2D models of this process yet 3D models are less common. 

The aim of my project is to generate software tools to model and visualise in three dimensions how a single root develops and pushes through soil. The model will represent individual cells moving, expanding and dividing. The program will allow visualisation of various cell types, their position and movement during growth

### Method

I will develop a program based on the programming language python. Numerical computations of cell positions and shapes will be carried out using scientific libraries such as Scipy and NumPy. Once the positions and shape of cells have been computed, the program will then provide 3D visualisation of the architecture of cells in the tissue and how these are formed as a result of cell activity.  A 3rd party module such as Pygame, PyOpenGL, PyODE or vPython will be used for 3D visualisation of cell architectures. Such libraries allows the user to create complex geometric shapes and add dynamic variables such as gravity or mathematical trajectories (using pythons inbuilt math module) upon them. By using this technique, coding cells as individual particles, allows the ability to render each cell and manipulate them through all cycles of development. 

###Pre-Project Testing 

I have tested various 3D visualisation modules and have decided to use vPython for my project because it is more adapted to fast prototyping and is designed to work with NumPy effortlessly. I am currently exploring ways to control the shape of the objects to allow better parameterisation of the cell geometry. In the future, the program will implement cell movement, cell deformation and cell division. Data from the literature, or directly measured from data available on site, will be used. Application of this work includes the simulation of entire root meristems with biological processes such as gene expression, biochemical pathways or cell wall biophysics as factors driving the changes in cell architectures. Computational techniques such as Smooth Particle Hydrodynamics could be used to model such processes. Work would likely migrate this design to a compiled programing language such as C++ to gain speed and to use techniques such as multithreading. 

### Installation

**Github Control**

### Tests

**How to run**

### Contributors

**Thanks**
