from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the image
image_path = '/workspaces/coding_photo_editting/Photo_for_Aaron/Aaron_2yrs_old.jpg'
try:
    img = Image.open(image_path)
    print(f"Image loaded successfully: {image_path}")
    print(f"Image format: {img.format}")
    print(f"Image size: {img.size}")
    print(f"Image mode: {img.mode}")
except Exception as e:
    print(f"Failed to load image: {e}")
    exit()

# Convert to numpy array for further analysis
img_np = np.array(img)

# Plot Color Histogram
def plot_color_histogram(image):
    # Check if the image is grayscale
    if len(image.shape) == 2:
        plt.hist(image.ravel(), bins=256, color='gray')
        plt.title('Grayscale Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
    else:
        color = ('r', 'g', 'b')
        for i, col in enumerate(color):
            histr = cv2.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
        plt.title('Color Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
    plt.show()

plot_color_histogram(img_np)