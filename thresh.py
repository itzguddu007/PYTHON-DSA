import cv2
import matplotlib.pyplot as plt

try:
    path = input("Enter grayscale image path: ")

    # Read image in grayscale
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise FileNotFoundError

    # Compute mean pixel intensity
    mean_val = img.mean()
    print("Mean Intensity:", mean_val)

    # Apply binary thresholding
    # Pixels > mean → 255, else → 0
    _, thresh = cv2.threshold(img, mean_val, 256, cv2.THRESH_BINARY)

    # Display images side by side
    plt.figure(figsize=(10, 6))

    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    # Thresholded image
    plt.subplot(1, 2, 2)
    plt.imshow(thresh, cmap='gray')
    plt.title("Thresholded Image")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: Invalid file path!")

except Exception as e:
    print("Error:", e)
