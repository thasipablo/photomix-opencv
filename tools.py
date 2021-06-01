import cv2
from base64 import b64encode


def read_image(img_path):
    img = cv2.imread(img_path)
    return img


def save_image(img):
    cv2.imwrite('C:/Users/rafik/Desktop/PhotoSaved/img.jpg', img)


def img_enc(img):
    _, image = cv2.imencode('.jpeg', img)
    bit_img = image.tobytes()
    return b64encode(bit_img).decode('utf-8')


def initialize(img):
    return img[0:2]


# THRESHOLD
# ***************************

def to_gray_scale(img):
    if img.shape[-1] == 3:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        return img


def to_binary_inv(img, thresh=100):
    if img.shape[-1] == 3:
        img = to_gray_scale(img)
        _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY_INV)
    else:
        _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY_INV)
    return img


def to_truncate(img, thresh=100):
    if img.shape[-1] == 3:
        img = to_gray_scale(img)
        _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_TRUNC)
    else:
        _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_TRUNC)
    return img


def to_zero(img, thresh=100):
    if img.shape[-1] == 3:
        img = to_gray_scale(img)
        _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_TOZERO)
    else:
        _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_TOZERO)
    return img


def to_zero_inv(img, thresh=100):
    if img.shape[-1] == 3:
        img = to_gray_scale(img)
        _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_TOZERO_INV)
    else:
        _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_TOZERO_INV)
    return img


# MORPHOLOGY
# *******************

# Element structurant
iterations = 1
elt_structurant = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))


# erosion
# **********

def erosion(img, iterations=iterations):
    return cv2.erode(img, elt_structurant, iterations=iterations)


# dilatation
# ************
def dilatation(img, iterations=iterations):
    return cv2.dilate(img, elt_structurant, iterations=iterations)


# ouverture
# *********
def open(img, iterations=iterations):
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, elt_structurant, iterations=iterations)


# fermeture
# **********
def close(img, iterations=iterations):
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, elt_structurant, iterations=iterations)


# gradient
# **********************
def gradient(img, iterations=iterations):
    return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, elt_structurant, iterations=iterations)


# FILTERS
# ********
def median_blur(img):
    return cv2.medianBlur(img, 5)


def gaussian_blur(img):
    return cv2.GaussianBlur(img, (5, 5), 0)


def edge_detect(img):
    return cv2.Canny(img, 100, 200)
