import cv2
import numpy as np
from scipy.stats import chisquare

def analyze(image_path):
    img = cv2.imread(image_path, 0)

    hist = cv2.calcHist([img], [0], None, [256], [0,256]).flatten()

    even = hist[0::2]
    odd = hist[1::2]

    even = np.where(even == 0, 1, even)
    odd = np.where(odd == 0, 1, odd)

    odd = odd * (np.sum(even) / np.sum(odd))

    chi, p = chisquare(f_obs=even, f_exp=odd)

    return {
        "chi_square": round(float(chi), 4),
        "p_value": round(float(p), 6)
    }