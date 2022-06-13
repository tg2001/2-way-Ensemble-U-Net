### Dataset

This folder contains the files for the preprocessing steps and the dataset creation step for training and test the models.

For creating the dataset, the function create_dataset() in this folder should be called with the following parameters:
- First one is the path to the folder containing the 3D volumes, which will form the input to the model
- Second one is the path to the folder containing the 3D volumes, which will form the corresponding segmented output
  (The 3D volumes will be used to create 2D dataset for the model)
- The third parameter 'n' will determine the number of 2D images taken from each axis of each volume. Along each axis, the 3D volume is divided into 'n' parts and 1 slice from each part is taken to create the dataset.
- The last parameter 's' will determine the test set size (in numbers or fraction), keeping the remaining for the train set. s=0 means no splitting will take place

This function will return four things if 's' is not equal to 0: train and test split for the input, followed by train and test split for the output

Otherwise, the input and output dataset will be returned as a whole.
