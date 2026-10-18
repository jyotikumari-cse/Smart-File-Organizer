import os
import shutil

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist!")
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".doc"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Music": [".mp3", ".wav"],
        "Python_Files": [".py"],
        "Other_Files": []
    }

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()
        category = "Other_Files"

        for folder, extensions in file_types.items():
            if extension in extensions:
                category = folder
                break

        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, filename)

        if os.path.exists(destination_path):
            print("Skipped existing file:", filename)
            continue

        shutil.move(file_path, destination_path)
        print(f"Moved {filename} to {category}")

    print("\nFile organization completed!")


print("================================")
print("      SMART FILE ORGANIZER")
print("================================")

folder = input("Enter the folder path to organize: ").strip().strip('"')

organize_files(folder)