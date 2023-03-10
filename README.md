# Image-Augmentation-

This is a Python script for augmenting images and their corresponding binary masks using the Albumentations library. It reads images and masks from their respective directories, randomly selects one of each, applies a series of random transformations using Albumentations, and saves the resulting augmented images and masks to their respective output directories.

The script uses the following libraries:

numpy
matplotlib
skimage
random
os
scipy
cv2 (OpenCV)
albumentations
It starts by defining the paths to the input (RGB and binary mask) and output directories. It then uses os.listdir to get a list of the image and mask filenames in the input directories.

The script defines a set of image augmentations using Albumentations, including vertical and horizontal flips, transpose, and grid distortion. It then enters a while loop that iterates until the desired number of augmented images (images_to_generate) has been created.

Inside the loop, the script randomly selects an image and mask from their respective lists, reads them using OpenCV, and applies the Albumentations transforms to both the image and mask. The resulting transformed image and mask are saved to the output directories using cv2.imwrite.

Finally, the loop increments the image counter (i) and the script moves on to the next iteration.
