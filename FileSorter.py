import os
import shutil
import tkinter  # python -m pip install tkinter
from tkinter import filedialog


print("Select a directory you want to sort")
user_directory = tkinter.filedialog.askdirectory(initialdir="/",  title='Please select a directory')
s = os.chdir(user_directory)
current = os.getcwd()

files = os.listdir(current)

# File extensions
images = [".png", ".jpg", ".jpeg", ".gif", ".jfif", ".webp"]  # File extensions for images
videos = [".mp4", ".mov", ".webm", ".mkv", ".flv", ".avi"]  # File extensions for videos
sounds = [".mp3", ".wav", ".flac", ".ogg"]  # File extensions for sounds
text = [".txt", ".pdf", ".doc", ".docx", ".odt"]  # File extensions for text documents
applications = [".exe", ".jar"]  # File extension for applications
code = [".py", ".cpp", ".js", ".java", ".cs", ".php", ".c", ".html", ".css", ".lua"]    # File extensions for code
archives = [".rar", ".zip", ".7z", ".tar", ".gz"]  # File extensions for archives

print("Sorting your files")

# Make folders if they don't exist
if not os.path.exists('Images_Sorted'):
    os.makedirs('Images_Sorted')

if not os.path.exists('Videos_Sorted'):
    os.makedirs('Videos_Sorted')

if not os.path.exists('Sounds_Sorted'):
    os.makedirs('Sounds_Sorted')

if not os.path.exists('Texts_Sorted'):
    os.makedirs('Texts_Sorted')

if not os.path.exists('Applications_Sorted'):
    os.makedirs('Applications_Sorted')

if not os.path.exists('Code_Sorted'):
    os.makedirs('Code_Sorted')

if not os.path.exists('Archives_Sorted'):
    os.makedirs('Archives_Sorted')

# Sort files in the folders
for file in files:
    destination = ""
    for ex in images:
        if file.endswith(ex):
            destination = f'{user_directory}\Images_Sorted'
            shutil.move(file, destination)
            print(f"Moved {file} to {user_directory}\Images_Sorted")
            break

    for ex in videos:
        if file.endswith(ex):
            destination = f'{user_directory}\Videos_Sorted'
            shutil.move(file, destination)
            print(f"Moved {file} to {user_directory}\Videos_Sorted")
            break

    for ex in sounds:
        if file.endswith(ex):
            destination = f'{user_directory}\Sounds_Sorted'
            shutil.move(file, destination)
            print(f"Moved {file} to {user_directory}\Sounds_Sorted")
            break

    for ex in text:
        if file.endswith(ex):
            destination = f'{user_directory}\Texts_Sorted'
            shutil.move(file, destination)
            print(f"Moved {file} to {user_directory}\Texts_Sorted")
            break

    for ex in applications:
        if file.endswith(ex):
            destination = f'{user_directory}\Applications_Sorted'
            shutil.move(file, destination)
            print(f"Moved {file} to {user_directory}\Applications_Sorted")
            break

    for ex in code:
        if file.endswith(ex):
            destination = f'{user_directory}\Code_Sorted'
            shutil.move(file, destination)
            print(f"Moved {file} to {user_directory}\Code_Sorted")
            break

    for ex in archives:
        if file.endswith(ex):
            destination = f'{user_directory}\Archives_Sorted'
            shutil.move(file, destination)
            print(f"Moved {file} to {user_directory}\Archives_Sorted")
            break


def popupmsg(msg):
    NORM_FONT = ("Helvetica", 10)
    popup = tkinter.Tk()
    popup.wm_title("!")
    label = tkinter.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    button = tkinter.Button(popup, text="Okay", command=popup.destroy)
    button.pack()
    popup.mainloop()


popupmsg("Files sorted")
