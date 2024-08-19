import os

# Paths to the edited images
edited_images = [
    '/workspaces/coding_photo_editting/Photo_for_Aaron/grayscale_Aaron_2yrs_old.jpg',
    '/workspaces/coding_photo_editting/Photo_for_Aaron/resized_Aaron_2yrs_old.jpg',
    '/workspaces/coding_photo_editting/Photo_for_Aaron/filtered_Aaron_2yrs_old.jpg',
    '/workspaces/coding_photo_editting/Photo_for_Aaron/enhanced_Aaron_2yrs_old.jpg'
]

# Remove the edited images
for image_path in edited_images:
    try:
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Removed {image_path}")
        else:
            print(f"{image_path} does not exist")
    except Exception as e:
        print(f"An error occurred while trying to remove {image_path}: {e}")