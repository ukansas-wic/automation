Step 0
You should have the "automation" folder opened in your terminal by now. If not, look at the slide on the board for instructions on how to do that.

Step 1
Open up the file "file_renamer"

Step 2
Let's start coding! Please walk through each line of code and read the comments!

```python
import os #This is telling Python to use the os module so we can talk to the operating system to look inside folders and rename files.

folder = "files_to_be_renamed" #You're telling Python where the files that need to be renamed are.

#Make a list of what you want to rename the files (you can choose any names you want, I just chose these for fun!)
version_names = [
    "v1",
    "v1_final",
    "v1_final_FINAL",
    "v1_final_FINAL_for_real_THIS_time",
    "v1_final_FINAL_for_real_THIS_time_LAST_EDIT",
]

files = os.listdir(folder) #This grabs all the file names from the folder and stores them in a list called files

#Loop through each file in the folder. i is the file number and filename is the name of the file
for i, filename in enumerate(files):
    base, ext = os.path.splitext(filename) #This splits the filename into 2 parts: base (the name of the file without extension), ext (the extension like .jpg, .png, .txt, etc)
    try:
        new_base = f"project_{version_names[i]}" #Try to use a name from the list
    except IndexError:
        new_base = f"project_backup_{i+1}" #If we run out of version names, we can fall back to something like project_backup_6, project_backup_7

    #This builds the full file paths for before and after renaming. We need these to tell the computer where to look and where to rename.
    old_path = os.path.join(folder, filename)
    new_filename = f"{new_base}{ext}"
    new_path = os.path.join(folder, new_filename)

    os.rename(old_path, new_path) #This does the actual renaming!
    print(f"Renamed '{filename}' → '{new_filename}'") #Print out what just happened.
```
Final Step
Run your file, and watch what happens!
    
