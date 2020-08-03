# Image-Augmentation for Yolo
A python based script to augment images for Yolo training. This script can be used to augment the raw labeled dataset. 

## Introduction
The script provides eleven augmentation modes. Following image manipulation types are added to a single image:

- Gaussian Blur
- Contour
- Emboss
- Find Edges
- Rank Filter
- Max Filter
- Min Filter
- Median Filter
- Mode Filter
- Watermark with a Swiss flag
- Normal

The script scales up to the highest amount of cores you have on your machine. If you don't have enough memory on your machine, dont' worrry. You can augment the dataset in batches, which are fully customizable in their size.
In the `img_aug` folder are some samples of the augmentation types.

## Prerequisites
```pip install pillow```

## Usage ##
**Step 1:** Load the labeled dataset (images and labels) in the `img_raw` folder

**Step 2:** Determine the batch size of images and labels in `augmentation.py` on line `32` and `37`

**Step 3:** I assumed your images are in `.jpg` and labels are in `.txt`, if not, then change the lines `42`, `46`, `64`, `68`

**Step 4:** run the script with `python augmentation.py`
