import pyautogui
import cv2
import numpy as np
import webbrowser
import imdb
from PIL import Image
from pytesseract import *
from turtle import title

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# dilation
def dilate(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
# erosion
def erode(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

# resizing image
def resize_img(image):
    return cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

# image read

img = cv2.imread('test17.png')

#output = pytesseract.image_to_string(img)
#array = output.split()

# pre-processing

img = resize_img(img)
gray = get_grayscale(img)
#noise = remove_noise(img)
#thresh = thresholding(img)
dilation = dilate(gray)
erosion = erode(dilation)

output = pytesseract.image_to_string(erosion)
array = output.split()

#print(array)
#print(output)

moviesDB = imdb.IMDb()

# Title search

#temp = 'THE WALK'
temp = output
movies = moviesDB.search_movie(temp)

#for movie in movies:
#    title = movie['title']
#    year  = movie['year']
#    print(f'{title} - {year}')

# Get ID of movie

id = movies[0].getID()

# Open the link of the movie

#url = 'https://www.imdb.com/find?q=XYZ&s=tt'
url = 'https://www.imdb.com/title/ttXYZ/'

url = url.replace("XYZ", id)

webbrowser.open(url)

