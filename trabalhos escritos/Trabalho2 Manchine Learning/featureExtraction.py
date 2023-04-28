import skimage
import cv2 #OpenCV
import numpy as np

def HU_FE(image):
    moments = cv2.moments(image.astype(np.float64))
    return np.asarray(cv2.HuMoments(moments).flatten())

def LBP_FE(image):
    lbp_image = local_binary_pattern(image, 59, 1, "uniform")
    return np.asarray(np.histogram(lbp_image.ravel(), bins=59)).tolist()[0]

def GLCM_FE(image):
    glcm = greycomatrix(image, [1], [0], 256, symmetric=True, normed=True)
    xs = []
    xs.append(greycoprops(glcm, 'dissimilarity')[0, 0])
    xs.append(greycoprops(glcm, 'correlation')[0, 0])
    xs.append(greycoprops(glcm, 'homogeneity')[0, 0])
    xs.append(greycoprops(glcm, 'ASM')[0, 0])
    xs.append(greycoprops(glcm, 'energy')[0, 0])
    xs.append(greycoprops(glcm, 'correlation')[0, 0])
    return np.asarray(xs);

		