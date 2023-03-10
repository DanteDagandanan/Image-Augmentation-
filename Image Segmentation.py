import numpy as np
from matplotlib import pyplot as plt
from skimage.transform import AffineTransform, warp
from skimage import io, img_as_ubyte
import random
import os
from scipy.ndimage import rotate
import cv2 as cv

import albumentations as A
images_to_generate=5000




MASK_images='C:/Users/PRO/Desktop/dante kadlfjasd/JACKFRUITS PROJECT FILES/Jackfruit Technology Project (2021-2023)/Data_Jackfruit Tech Project_21-23/training with decoy background/binary/'
RGB_images='C:/Users/PRO/Desktop/dante kadlfjasd/JACKFRUITS PROJECT FILES/Jackfruit Technology Project (2021-2023)/Data_Jackfruit Tech Project_21-23/training with decoy background/rgb/'

img_augmented_path="C:/Users/PRO/Desktop/dante kadlfjasd/JACKFRUITS PROJECT FILES/Jackfruit Technology Project (2021-2023)/Data_Jackfruit Tech Project_21-23/training with decoy background/rgb augmented/" # path to store aumented images
msk_augmented_path="C:/Users/PRO/Desktop/dante kadlfjasd/JACKFRUITS PROJECT FILES/Jackfruit Technology Project (2021-2023)/Data_Jackfruit Tech Project_21-23/training with decoy background/binary augmented/" # path to store aumented images
images=[] # to store paths of images from folder
masks=[]

for im in os.listdir(RGB_images):  # read image name from folder and append its path into "images" array     
    images.append(os.path.join(RGB_images,im))

for msk in os.listdir(MASK_images):  # read image name from folder and append its path into "images" array     
    masks.append(os.path.join(MASK_images,msk))


aug = A.Compose([
    A.VerticalFlip(p=0.3),              
    #A.RandomRotate90(p=0.5),
    A.HorizontalFlip(p=0.6),
    A.Transpose(p=1),
    #A.ElasticTransform(p=1, alpha=120, sigma=120 * 0.05, alpha_affine=120 * 0.03),
    A.GridDistortion(p=1)
    ]
)

#random.seed(42)

i=1   # variable to iterate till images_to_generate


while i<=images_to_generate: 
    number = random.randint(0, len(images)-1)  #PIck a number to select an image & mask
    image = images[number]
    mask = masks[number] 
    print(image, mask)
    #image=random.choice(images) #Randomly select an image name
    original_image = cv.imread(image)
    original_mask = cv.imread(mask)
    
    augmented = aug(image=original_image, mask=original_mask)
    transformed_image = augmented['image']
    transformed_mask = augmented['mask']

        
    new_image_path= "%s/augmented_image_%s.png" %(img_augmented_path, i)
    new_mask_path = "%s/augmented_mask_%s.png" %(msk_augmented_path, i)
    cv.imwrite(new_image_path, transformed_image)
    cv.imwrite(new_mask_path, transformed_mask)
    i =i+1
    
