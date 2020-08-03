import os
import shutil
import glob
import pathlib
import shutil
import concurrent.futures
import random
from datetime import datetime
from PIL import Image, ImageFilter
from PIL.ImageFilter import (RankFilter, MedianFilter, MinFilter, MaxFilter)
from pathlib import Path


# # # SETTINGS # # #
# start timer for measurement
start_time = datetime.now()

# import folder for Images
# feel free to choose an other source folder
list_of_files = "img_raw"

# export folder for images
# feel free to choose an other processing folder
middle_process_folder = "img_processed"

# relative path for export folder, images and labels will be exported in the same folder
# feel free to choose an other destination folder
export_folder = "img_aug"

# set amount of max images per augmentation batch
# max_batch_amount_images can be as high as possible, only restriction is the result from all images in img_raw divided by max_batch_amount_images must be an integer
# the program will break if (amount of images in img_raw)/max_batch_amount_images is not an integer
max_batch_amount_images = 1

# set amount of max labels per renaming batch
# max_batch_amount_labels can be as high as possible, only restriction is the result from all labels in img_raw divided by max_batch_amount_labels must be an integer
# the program will break if (amount of images in img_raw)/max_batch_amount_labels is not an integer
max_batch_amount_labels = 1

# File extension for augmented images
# can be adjusted, depends on the source filetype
image_extension = ".jpg"

# File extension for renamed labels
# can be adjusted, depends on the label format
label_extension = ".txt"

# # # CONSTANS # # #
# counter for batch runs
# this value shold not be changed!
i = 0

# # # FUNCTIONS # # #
# image loading
def loadImages(path = middle_process_folder):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(image_extension)]

# label loading
def loadLabels(path = middle_process_folder):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(label_extension)]

# image counting function
def count_images(dir):
    return len(glob.glob1(dir,"*" + image_extension))

# label counting function
def count_labels(dir):
    return len(glob.glob1(dir,"*" + label_extension))

# add normal image to augmented images
def process_image_normal(img_name):
    img = Image.open(pathlib.Path(img_name))
    img.save(export_folder + "/Normal_" + format(Path(img_name).stem) + image_extension)
    print("Normal Image added successfully")

# add gaussian blur to an image
def process_image_gaussblur(img_name):
    img = Image.open(pathlib.Path(img_name))
    img = img.filter(ImageFilter.GaussianBlur(radius=3))
    #filename = (Path(img_name).stem)
    img.save(export_folder + "/GaussBlur_" + format(Path(img_name).stem) + image_extension)
    print("Gauss Filter added successfully")

# add contour filter to an image
def process_image_contour(img_name):
    img = Image.open(pathlib.Path(img_name))
    img = img.filter(ImageFilter.CONTOUR())
    img.save(export_folder + "/Contour_" + format(Path(img_name).stem) + image_extension)
    print("Contour Filter added successfully")

# add emboss filter to an image
def process_image_emboss(img_name):
    img = Image.open(pathlib.Path(img_name))
    img = img.filter(ImageFilter.EMBOSS())
    img.save(export_folder + "/Emboss_" + format(Path(img_name).stem) + image_extension)
    print("Emboss Filter added successfully")

# add find edges filter to an image
def process_image_findedges(img_name):
    img = Image.open(pathlib.Path(img_name))
    img = img.filter(ImageFilter.FIND_EDGES())
    img.save(export_folder + "/FindEdges_" + format(Path(img_name).stem) + image_extension)
    print("FindEdges Filter added successfully")

# add RankFilter to an image
def process_image_rankfilter(img_name):
    img = Image.open(pathlib.Path(img_name))
    img = img.filter(ImageFilter.RankFilter(size=9, rank=2))
    img.save(export_folder + "/RankFilter_" + format(Path(img_name).stem) + image_extension)
    print("RankFilter added successfully")

# add MaxFilter to an image
def process_image_maxfilter(img_name):
    img = Image.open(pathlib.Path(img_name))
    img = img.filter(ImageFilter.MaxFilter(size=9))
    img.save(export_folder + "/MaxFilter_" + format(Path(img_name).stem) + image_extension)
    print("MaxFilter added successfully")

# add MinFilter to an image
def process_image_minfilter(img_name):
    img = Image.open(pathlib.Path(img_name))
    img = img.filter(ImageFilter.MinFilter(size=9))
    img.save(export_folder + "/MinFilter_" + format(Path(img_name).stem) + image_extension)
    print("MinFilter added successfully")

# add MedianFilter to an image
def process_image_medianfilter(img_name):
    img = Image.open(pathlib.Path(img_name))
    img = img.filter(ImageFilter.MedianFilter(size=9))
    img.save(export_folder + "/MedianFilter_" + format(Path(img_name).stem) + image_extension)
    print("MedianFilter added successfully")

# add ModeFilter to an image
def process_image_modefilter(img_name):
    img = Image.open(pathlib.Path(img_name))
    img = img.filter(ImageFilter.ModeFilter(size=3))
    img.save(export_folder + "/ModeFilter_" + format(Path(img_name).stem) + image_extension)
    print("ModeFilter added successfully")

# add an image as watermark to an image
def process_image_watermark(img_name):
    img = Image.open(pathlib.Path(img_name))
    watermark_img = Image.open("swissflag.png")
    positionwatermarkx = random.randint(0, 700)
    positionwatermarky = random.randint(0, 400)
    img.paste(watermark_img, (positionwatermarkx, positionwatermarky), watermark_img)
    img.save(export_folder + "/Watermark_" + format(Path(img_name).stem) + image_extension)
    print("Watermark added successfully")

# rename source label to normal label
def process_label_normal(label_name):
    old_label = label_name
    renamed_label = export_folder + "/Normal_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Normal Label renamed successfully")

# rename source label to gaussblur label
def process_label_gaussblur(label_name):
    old_label = label_name
    renamed_label = export_folder + "/GaussBlur_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Gauss Label renamed successfully")

# rename source label to contour label
def process_label_contour(label_name):
    old_label = label_name
    renamed_label = export_folder + "/Contour_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Contour Label renamed successfully")

# rename source label to emboss label
def process_label_emboss(label_name):
    old_label = label_name
    renamed_label = export_folder + "/Emboss_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Emboss Label renamed successfully")

# rename source label to findedges label
def process_label_findedges(label_name):
    old_label = label_name
    renamed_label = export_folder + "/FindEdges_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Find Edges Label renamed successfully")

# rename source label to rankfilter label
def process_label_rankfilter(label_name):
    old_label = label_name
    renamed_label = export_folder + "/RankFilter_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Rank Filter Label renamed successfully")

# rename source label to maxfilter label
def process_label_maxfilter(label_name):
    old_label = label_name
    renamed_label = export_folder + "/MaxFilter_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Max Filter Label renamed successfully")

# rename source label to minfilter label
def process_label_minfilter(label_name):
    old_label = label_name
    renamed_label = export_folder + "/MinFilter_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Min Filter Label renamed successfully")

# rename source label to medianfilter label
def process_label_medianfilter(label_name):
    old_label = label_name
    renamed_label = export_folder + "/MedianFilter_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Median Filter Label renamed successfully")

# rename source label to modefilter label
def process_label_modefilter(label_name):
    old_label = label_name
    renamed_label = export_folder + "/ModeFilter_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Mode Filter Label renamed successfully")

# rename source label to watermark label
def process_label_watermark(label_name):
    old_label = label_name
    renamed_label = export_folder + "/Watermark_" + format(Path(label_name).stem) + label_extension
    shutil.copy(old_label, renamed_label)
    print("Watermark Label renamed successfully")

# # # Main Code # # #
if __name__ == '__main__':

    # the result from img_raw divided by max_batch must be an integer! 
    if count_images(list_of_files) % max_batch_amount_images == 0:
        # loop over all files in directory
        for files in os.listdir(list_of_files):
            if count_images(list_of_files) > 0:
                if files.endswith(image_extension):
                    # move only an amount of batch size of images to the process folder
                    
                    while i < (max_batch_amount_images):
                        all_latest_files = glob.glob(list_of_files + "/*" + image_extension)
                        youngest_file = all_latest_files[0]
                        shutil.move(os.path.join(youngest_file), middle_process_folder)
                        i += 1
                    
                    # empty list for temp images in img_processed
                    img_names = []
                    # load images into list
                    filenames_image = loadImages()
                    for file_images in filenames_image:
                        img_names.append(file_images)

                    # start the multithreading augmentation process
                    with concurrent.futures.ProcessPoolExecutor() as executor:
                        executor.map(process_image_normal, img_names)
                        executor.map(process_image_gaussblur, img_names)
                        executor.map(process_image_contour, img_names)
                        executor.map(process_image_emboss, img_names)
                        executor.map(process_image_findedges, img_names)
                        executor.map(process_image_rankfilter, img_names)
                        executor.map(process_image_maxfilter, img_names)
                        executor.map(process_image_minfilter, img_names)
                        executor.map(process_image_medianfilter, img_names)
                        executor.map(process_image_modefilter, img_names)
                        executor.map(process_image_watermark, img_names)

                    removeable_files = glob.glob(middle_process_folder + "/*")
                    for f in removeable_files:
                        os.remove(f)

                    i = 0

    else:
        print("[ERROR]  Please choose another value for max_batch_amount")
        print("[ERROR]  Division result from img_raw/max_batch_amount must be evenly")
        print("[INFO]   Please recalculate the correct max_batch_amount and edit line 32")



    if count_labels(list_of_files) % max_batch_amount_labels == 0:

        # loop over all files in directory
        for files in os.listdir(list_of_files):
            if count_labels(list_of_files) > 0:
                if files.endswith(label_extension):

                    # move only an amount of batch size of labels to the process folder
                    
                    while i < (max_batch_amount_labels):
                        all_latest_files = glob.glob(list_of_files + "/*" + label_extension)
                        youngest_file = all_latest_files[0]
                        shutil.move(os.path.join(youngest_file), middle_process_folder)
                        i += 1
                    
                    # empty list for temp labels in img_processed
                    label_names = []
                    # load images into list
                    filenames_label = loadLabels()
                    for file_labels in filenames_label:
                        label_names.append(file_labels)

                    # start the multithreading renaming process
                    with concurrent.futures.ProcessPoolExecutor() as executor:
                        executor.map(process_label_normal, label_names)
                        executor.map(process_label_gaussblur, label_names)
                        executor.map(process_label_contour, label_names)
                        executor.map(process_label_emboss, label_names)
                        executor.map(process_label_findedges, label_names)
                        executor.map(process_label_rankfilter, label_names)
                        executor.map(process_label_maxfilter, label_names)
                        executor.map(process_label_minfilter, label_names)
                        executor.map(process_label_medianfilter, label_names)
                        executor.map(process_label_modefilter, label_names)
                        executor.map(process_label_watermark, label_names)

                    removeable_files = glob.glob(middle_process_folder + "/*")
                    for f in removeable_files:
                        os.remove(f)

                    i = 0

    else:
        print("[ERROR]  Please choose another value for max_batch_amount_labels")
        print("[ERROR]  Division result from img_raw/max_batch_amount_labels must be evenly")
        print("[INFO]   Please recalculate the correct max_batch_amount_labels and edit line 37")


    time_elapsed = datetime.now() - start_time
    print("Die Augmentation dauerte (h:mm:ss.ms) {}".format(time_elapsed))
