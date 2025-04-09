import os

folder = "version_controlled_chaos"  # Replace with your folder name

# The cursed sequence of version names
version_names = [
    "v1",
    "v1_final",
    "v1_final_FINAL",
    "v1_final_FINAL_for_real_THIS_time",
    "v1_final_FINAL_for_real_THIS_time_LAST_EDIT",
    "v1_final_FINAL_for_real_THIS_time_LAST_EDIT_I_PROMISE"
]

files = os.listdir(folder)

for i, filename in enumerate(files):
    base, ext = os.path.splitext(filename)
    try:
        new_base = f"project_{version_names[i]}"
    except IndexError:
        new_base = f"project_backup_{i+1}"

    old_path = os.path.join(folder, filename)
    new_filename = f"{new_base}{ext}"
    new_path = os.path.join(folder, new_filename)

    os.rename(old_path, new_path)
    print(f"Renamed '{filename}' → '{new_filename}'")
