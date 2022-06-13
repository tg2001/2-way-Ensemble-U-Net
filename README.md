# 2-way Ensemble U-Net

This is the repository for the following paper: Fetal Brain Component Segmentation using with 2-way Ensemble U-Net.

This paper is for segmenting the fetal brain into its seven major components: Intracranial space and extra-axial CSF spaces, Gray matter, White matter, Ventricles, Cerebellum, Deep gray matter and the Brainstem and spinal cord.

We have used the FeTA 2.1 (Fetal Tissue Annotation) Dataset for the purpose of training and testing our models. The dataset can be downloaded from this website: [link](https://zenodo.org/record/4541606#.Yqb6HHVBw_A); after agreeing to the terms and conditions.

The repository contains the following folders:
- Dataset: Contains code for creating the dataset
- Testing: Contains code for using the model for performing segmentation and also for testing the performance of the models
- visualisation: Contains code for visualising the dataset
- Models: Contains the code for the 7 models we tested out

(Information the codes and how to use them are uploaded in the readme file of their respective folders)

We have used Google Colaboratory for all the tasks.

The input to our model should be of the shape (256x256)

The model files and saved weights are uploaded in this [google drive link](https://drive.google.com/drive/folders/1lrWgQZ1xFyEwumqrg6-jWu16GA1yCWRp?usp=sharing).

The model will output the segmentation of the shape (256x256x8), returning the probability of a pixel to be in each of the 8 classes: the seven brain components and the background; which is post-processed to return it in the required form.

We have also created a demo colab file on how to use these modules for creating a dataset, visualising it, testing the models and getting outputs from them. It is uploaded in this [link](https://colab.research.google.com/drive/15-JJQE5sdSatZ0WWOMIuICncn6Pi4Eny?usp=sharing).

A sample input and its corresponding output is of the following form:

![download](https://user-images.githubusercontent.com/89569287/173315387-8a11dc43-d041-48f2-b0c6-9b0fa12c4047.png)
![download (1)](https://user-images.githubusercontent.com/89569287/173315401-da47764e-0a79-4535-888f-a7133d5f6ee0.png)

Libraries used in this this repository:
- Numpy
- Opencv
- os
- Scikit-Learn
- Tensorflow 2
- Nibabel
- Matplotlib
- Ipywidget (required for visualization of 3D volumes; can only be used in Ipython notebooks)
