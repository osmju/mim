import os
import random

#----------------------------------------------------------#
def get_subfolders(root):
    filenames = os.listdir(root)
    subfolders = []

    for filename in filenames:
        if os.path.isdir(os.path.join(os.path.abspath(root), filename)):
            subfolders.append(filename)
    
    return subfolders

#----------------------------------------------------------#
def get_files(root):
    filenames = os.listdir(root)
    files = []

    for filename in filenames:
        if os.path.isfile(os.path.join(os.path.abspath(root), filename)):
            files.append(filename)
    
    return files

#----------------------------------------------------------#
def get_contrasting_flavours(root_path):
    list_flavours = get_subfolders(root_path)
    num_flavours = len(list_flavours) - 1
    
    flavour1 = random.randint(0, num_flavours)
    flavour2 = random.randint(0, num_flavours)

    while (flavour2 == flavour1):
        flavour2 = random.randint(0, num_flavours)
    
    return [list_flavours[flavour1], list_flavours[flavour2]]

#----------------------------------------------------------#
def get_random_sound(root_path, flavour, remove_static=True):
    flavour_path = os.path.join(root_path, flavour)
    flavour_files = get_files(flavour_path)
    num_files = len(flavour_files)
    random_index = random.randint(0, num_files - 1)
    full_path = os.path.join(flavour_path, flavour_files[random_index])

    if remove_static == True:
        # remove static/ in front of path
        pos = full_path.find('/')
        full_path = full_path[pos+1:]

    return full_path

#----------------------------------------------------------#
def randomize_choices(choices):
    # randomize question 1 choices
    choices_indices = range(len(choices))
    random.shuffle(choices_indices)
    random_choices = [0] * len(choices)

    for i in range(len(choices)):
        random_choices[i] = choices[choices_indices[i]]
    
    return random_choices

#----------------------------------------------------------#



