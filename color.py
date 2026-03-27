import cv2
import matplotlib.pyplot as plt

try:
    path = input("Enter image path: ")

    # Read image (color)
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Show grayscale image
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')

    # Plot histogram
    plt.subplot(1, 2, 2)
    plt.hist(gray.flatten(), bins=256, range=(0, 255))
    plt.title("Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: File not found or invalid path!")

except Exception as e:
    print("Error:", e)
