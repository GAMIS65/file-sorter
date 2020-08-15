import os
import shutil
import tkinter  # python -m pip install tkinter
import uuid
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()     # This hides the blank tkinter window

def get_directory():
    global user_directory 
    global files
    
    print("Select a directory you want to sort")
    
    user_directory = tkinter.filedialog.askdirectory(initialdir="/",  title='Please select a directory')
    s = os.chdir(user_directory)
    current = os.getcwd()
    files = os.listdir(current)

    return user_directory, files


# File extensions
images = [".png", ".jpg", ".jpeg", ".gif", ".jfif", ".webp"]  # File extensions for images
videos = [".mp4", ".mov", ".webm", ".mkv", ".flv", ".avi"]  # File extensions for videos
sounds = [".mp3", ".wav", ".flac", ".ogg"]  # File extensions for sounds
text = [".txt", ".pdf", ".doc", ".docx", ".odt", ".ppt", ".pptx", ".pptm"]  # File extensions for text documents
applications = [".exe", ".jar"]  # File extension for applications
code = [".py", ".cpp", ".js", ".java", ".cs", ".php", ".c", ".html", ".css", ".lua"]    # File extensions for code
archives = [".rar", ".zip", ".7z", ".tar", ".gz"]  # File extensions for archives


def make_folders(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def sort_files(files, file_formats, folder_name, user_directory): 
    try:    
        for file in files:
            destination = ""
            for file_format in file_formats:
                if file.endswith(file_format):
                    destination = f'{user_directory}\\{folder_name}'
                    shutil.move(file, destination)
                    print(f"Moved {file} to {user_directory}/{folder_name}")
                    break

    except Exception as err:   # Rename the file if a file with that name already exists
        extension = os.path.splitext(file)[1]   
        xx = str(uuid.uuid4()) + extension  
        os.rename(file, file[1] + xx)
        s = os.chdir(user_directory)
        current = os.getcwd()
        files = os.listdir(current)
        sort_files(files, file_formats, folder_name, user_directory)

def main():
    get_directory()
    
    make_folders("Images_Sorted")
    make_folders("Videos_Sorted")
    make_folders("Sounds_Sorted")
    make_folders("Archives_Sorted")
    make_folders("Texts_Sorted")
    make_folders("Code_Sorted")
    make_folders("Applications_Sorted")

    sort_files(files, images, "Images_Sorted", user_directory)
    sort_files(files, videos, "Videos_Sorted", user_directory)
    sort_files(files, sounds, "Sounds_Sorted", user_directory)
    sort_files(files, archives, "Archives_Sorted", user_directory)
    sort_files(files, text, "Texts_Sorted", user_directory)
    sort_files(files, code, "Code_Sorted", user_directory)
    sort_files(files, applications, "Applications_Sorted", user_directory)

    input("Files sorted. Press any key to exit")

if __name__ == "__main__":
    main()
