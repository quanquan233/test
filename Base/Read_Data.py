import os

import yaml

def return_yaml(filename):
    file_dir = '.\\'+'Data\\'+filename
    with open(file_dir,'r',encoding='utf-8') as f:
        file_obj = yaml.load(f)
        return file_obj

