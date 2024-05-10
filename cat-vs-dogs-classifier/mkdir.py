import os

base_dir = './tmp/cats-v-dogs'

try:
    os.makedirs(base_dir)  # Create base directory and any missing parent directories
    os.makedirs(os.path.join(base_dir, 'training', 'cats'))
    os.makedirs(os.path.join(base_dir, 'training', 'dogs'))
    os.makedirs(os.path.join(base_dir, 'validation', 'cats'))
    os.makedirs(os.path.join(base_dir, 'validation', 'dogs'))
    os.makedirs(os.path.join(base_dir, 'test', 'cats'))
    os.makedirs(os.path.join(base_dir, 'test', 'dogs'))
except OSError as e:
    print(f"Error: {str(e)}")




CAT_DIR = 'data/train/cat'
DOG_DIR = 'data/train/dog'
TRAINING_DIR = "/tmp/cats-v-dogs/training/"
VALIDATION_DIR = "/tmp/cats-v-dogs/validation/"

TRAINING_CATS = os.path.join(TRAINING_DIR, "cats/")
VALIDATION_CATS = os.path.join(VALIDATION_DIR, "cats/")

TRAINING_DOGS = os.path.join(TRAINING_DIR, "dogs/")
VALIDATION_DOGS = os.path.join(VALIDATION_DIR, "dogs/")

# Define whether to include test split or not
INCLUDE_TEST = True



print(len(os.listdir('./tmp/cats-v-dogs/training/cats')))
print(len(os.listdir('./tmp/cats-v-dogs/training/dogs')))

print(len(os.listdir('./tmp/cats-v-dogs/validation/cats')))
print(len(os.listdir('./tmp/cats-v-dogs/validation/dogs')))

print(len(os.listdir('./tmp/cats-v-dogs/test/cats')))
print(len(os.listdir('./tmp/cats-v-dogs/test/dogs')))