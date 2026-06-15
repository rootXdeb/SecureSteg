import cv2
import numpy as np

def calculate_psnr(original_path, stego_path):
    original = cv2.imread(original_path)
    stego = cv2.imread(stego_path)

    mse = np.mean((original - stego) ** 2)

    if mse == 0:
        return 100

    return 20 * np.log10(255.0 / np.sqrt(mse))