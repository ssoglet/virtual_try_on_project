from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
from colorthief import ColorThief
import matplotlib.pyplot as plt

# Initialize 68 landmarks
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Users/sophi/AppData/Local/Programs/Python/Python39/shape_predictor_68_face_landmarks.dat")
image = cv2.imread("C:/Users/sophi/man.jpg")
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect face and 68 landmarks
rects = detector(gray, 1)
for (i, rect) in enumerate(rects):
	shape = predictor(gray, rect)
	shape = face_utils.shape_to_np(shape)
	(x, y, w, h) = face_utils.rect_to_bb(rect)
	for (x, y) in shape:
		cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

# Show result
cv2.imshow("Output", image)
cv2.waitKey(0)

#Extract cheek area
left_cheek = image[shape[29][1]:shape[33][1], shape[4][0]:shape[48][0]]
right_cheek = image[shape[29][1]:shape[33][1], shape[54][0]:shape[12][0]]
cheek = np.concatenate([left_cheek, right_cheek], 1)
cv2.imwrite("cheeks.jpg", cheek)

#Extract skin color
ct = ColorThief("C:/Users/sophi/cheeks.jpg")
dom = ct.get_color(quality=1)
print(dom)
plt.imshow([[dom]])
plt.show()