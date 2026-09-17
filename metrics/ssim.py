from skimage.metrics import structural_similarity as ssim
import cv2

def calculate_ssim(original_path, stego_path):
    original = cv2.imread(original_path)
    stego = cv2.imread(stego_path)

    original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    stego_gray = cv2.cvtColor(stego, cv2.COLOR_BGR2GRAY)

    score, _ = ssim(original_gray, stego_gray, full=True)

    return score