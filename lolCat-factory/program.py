import os
import subprocess
import platform


import cat_service

def print_heaer():
    print('---------------------------------------')
    print('             Cat Factory')
    print('---------------------------------------')
    print()

def get_or_create_ouput_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)
    # print(full_path)
    return full_path

def download_cats(folder):
    print('contacting server to download cats ...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)
    print('Done')

def display_cats(folder):
    # open folder
    print('Displaying cats in OS window')

    if platform.system() == 'Darwin':
       subprocess.call(['open', folder])  #open file finder
    elif platform.system() == 'Windows':
       #subprocess.call(['start', folder], shell=True)  #open explorer
       subprocess.call(['explorer', folder])  #open explorer
    elif platform.system() == 'Linux':
       subprocess.call(['xdg-open', folder])  # linux
    else:
        print("We don't support your os:" + platform.system())

def main():
    print_heaer()
    folder = get_or_create_ouput_folder()
    download_cats(folder)
    display_cats(folder)

if __name__ == '__main__':
    main()