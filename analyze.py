from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/workspaces/coding_photo_editting/Photo_for_Aaron/Aaron_2yrs_old.jpg'
try:
    img = Image.open(image_path)
    print(f"Image loaded successfully: {image_path}")
except Exception as e:
    print(f"Failed to load image: {e}")
    exit()

# Convert to numpy array for further analysis
img_np = np.array(img)

# Plot Color Histogram
def plot_color_histogram(image):
    # Convert image to BGR format if it's in RGBA or RGB format
    if image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    elif image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.title('Color Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

plot_color_histogram(img_np)