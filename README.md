# 2-way Ensemble U-Net

This is the repository for the following paper: Fetal Brain Component Segmentation using with 2-way Ensemble U-Net.

This paper is for segmenting the fetal brain into its seven major components: Intracranial space and extra-axial CSF spaces, Gray matter, White matter, Ventricles, Cerebellum, Deep gray matter and the Brainstem and spinal cord.

We have used the FeTA 2.1 (Fetal Tissue Annotation) Dataset for the purpose of training and testing our models.

The repository contains the following folders:
- Dataset: This folder contains code for creating the dataset
- Testing: This folder contains code for using the model for performing segmentation and also for testing the performance of the models
- visualisation: This folder contains code for visualising the dataset

We have used Google Colaboratory for all the tasks.

The input to our model should be of the shape (256x256)

The model files and saved weights are uploaded in the this [link](https://drive.google.com/drive/folders/1lrWgQZ1xFyEwumqrg6-jWu16GA1yCWRp?usp=sharing)

The model will output the segmentation of the shape (256x256x8), returning the probability of a pixel to be in each of the 8 classes: the seven brain components and the background; which is post-processed to return it in the required form.

For creating the dataset, the function create_dataset(), in the Dataset folder, should be called with the following parameters:
- First one is the path to the folder containing the 3D volumes, which will form the input to the model
- Second one is the path to the folder containing the 3D volumes, which will form the corresponding segmented output

  (The 3D volumes will be used to create 2D dataset for the model)
- The third parameter 'n' will determine the number of 2D images taken from each axis of each volume. Along each axis, the 3D volume is divided into 'n' parts and 1 slice from each part is taken to create the dataset.
- The last parameter 's' will determine the test set size (in numbers or fraction), keeping the remaining for the train set. s=0 means no splitting will take place

This function will return four things if 's' is not equal to 0: train and test split for the input, followed by train and test split for the output,
otherwise, the input and output dataset will be returned as a whole.

For testing or getting output from the model, first the model should be loaded, then pred_and_eval(), in the Testing folder, should be called with the following parameters:
- The model to be used should be passed as the first input
- The input(s) to the model should be passed next
  
  (For getting output from the model, these 2 inputs are enough. In this case, the model will return a 3D array containing the segmented output to all the 2D input images)
  
  For evaluating the model's performance, the next parameters should be passed along with the above ones:
- The actual output(s), for the function to compare with
- The last parameter will decide whether to return the average value of the evaluation metrics for all the classes or to return detailed evaluation with respect to each class for all the images in the test set

Evaluation metrics used: Precision, Sensitivity, Jaccard Similarity, Dice Score, Accuracy

Accuracy wont be returned when the detailed evaluation for all the classes are returned.

For visualization purpose, there are three function in the visualization folder:
- The visualize_2d() will visualize any 2D image, for which, the 2D array should be passed as a parameter.
- The visualize_3d() will visualize any 3D volume, for which no parameters are needed, rather an input will be prompted after calling the function, where the path to the folder containing the volume(s) should be given. The volumes should be in NIfTI format (with extensions .nii or .nii.gz). This function will only work in ipython notebook (like colab), since it uses ipywidgets library.
- The brain_part_focus() will help in visualising either brain as a whole, or any one of the brain component at a time.
- 
