from PIL import Image
import os

def count_pixels(file_path):
    try:
        # Open the image
        image = Image.open(file_path)

        # Get the dimensions (width x height)
        width, height = image.size

        # Calculate the total number of pixels
        total_pixels = width * height

        return total_pixels

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

def process_folder(folder_path):
    total_pixels_per_folder = 0

    # Walk through the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        folder_pixels = 0
        for file in files:
            # Check if the file is a PNG
            if file.lower().endswith(".png"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                pixels = count_pixels(file_path)
                folder_pixels += pixels
                total_pixels_per_folder += pixels

        # Print the total pixels for the current folder
        print(f"Total pixels in folder '{root}': {folder_pixels}\n")

    # Print the final report with total pixels across all folders
    print(f"Total pixels across all folders: {total_pixels_per_folder}")

if __name__ == "__main__":
    # Specify the folder to process (current directory in this case)
    folder_to_process = "."

    # Process the folder and its subfolders
    process_folder(folder_to_process)
