import os
import cv2
import numpy as np

filepath = "/home/brian/Pictures/GSV_scrape/"

for root, dirs, files in os.walk(filepath):
    for file in files:
        if file.endswith(".jpg"):
            img = cv2.imread(os.path.join(root, file))
            img1 = img[:, :1280]
            img2 = img[:, 1280:]
            img = np.concatenate((img1, img2), axis=0)

            cv2.imshow("img", img)
            cv2.waitKey(0)
        break

    break

cv2.destroyAllWindows()