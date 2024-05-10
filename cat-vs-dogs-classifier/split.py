import os
import random
from shutil import copyfile
import mkdir

def split_data(main_dir, training_dir, validation_dir, test_dir=None, include_test_split = True,  split_size=0.9):
    """
    Splits the data into train validation and test sets (optional)

    Args:
    main_dir (string):  path containing the images
    training_dir (string):  path to be used for training
    validation_dir (string):  path to be used for validation
    test_dir (string):  path to be used for test
    include_test_split (boolen):  whether to include a test split or not
    split_size (float): size of the dataset to be used for training
    """
    files = []
    for file in os.listdir(main_dir):
        if  os.path.getsize(os.path.join(main_dir, file)): # check if the file's size isn't 0
            files.append(file) # appends file name to a list

    shuffled_files = random.sample(files,  len(files)) # shuffles the data
    split = int(0.9 * len(shuffled_files)) #the training split casted into int for numeric rounding
    train = shuffled_files[:split] #training split
    split_valid_test = int(split + (len(shuffled_files)-split)/2)
   
    if include_test_split:
        validation = shuffled_files[split:split_valid_test] # validation split
        test = shuffled_files[split_valid_test:]
    else:
        validation = shuffled_files[split:]

    for element in train:
        copyfile(os.path.join(main_dir,  element), os.path.join(training_dir, element)) # copy files into training directory

    for element in validation:
        copyfile(os.path.join(main_dir,  element), os.path.join(validation_dir, element))# copy files into validation directory
        
    if include_test_split:
        for element in test:
            copyfile(os.path.join(main_dir,  element), os.path.join(test_dir, element)) # copy files into test directory
    print("Split sucessful!")



split_data(mkdir.CAT_DIR, './tmp/cats-v-dogs/training/cats', './tmp/cats-v-dogs/validation/cats', './tmp/cats-v-dogs/test/cats',mkdir.INCLUDE_TEST, 0.9)
split_data(mkdir.DOG_DIR, './tmp/cats-v-dogs/training/dogs', './tmp/cats-v-dogs/validation/dogs','./tmp/cats-v-dogs/test/dogs',mkdir.INCLUDE_TEST, 0.9)


print(len(os.listdir('./tmp/cats-v-dogs/training/cats')))
print(len(os.listdir('./tmp/cats-v-dogs/training/dogs')))

print(len(os.listdir('./tmp/cats-v-dogs/validation/cats')))
print(len(os.listdir('./tmp/cats-v-dogs/validation/dogs')))


print(len(os.listdir('./tmp/cats-v-dogs/test/cats')))
print(len(os.listdir('./tmp/cats-v-dogs/test/dogs')))