import cv2
import os
import json
import numpy as np
import keyboard

filepath = "/home/brian/Pictures/GSV_scrape/"

def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_RBUTTONDOWN:
        coordinates.append((x, y))
        print(coordinates)

if __name__ == "__main__":
    cv2.namedWindow('img')
    cv2.setMouseCallback('img', mouse_drawing)
    for root, dirs, files in os.walk(filepath):
        files = sorted(files)
        label = {}
        for file in files:
            label[file] = 0
        done_labeling_flag = 0
        i = 0
        coordinates = []
        while not done_labeling_flag:
            if i != len(files):
                if files[i].endswith(".jpg"):
                    img = cv2.imread(os.path.join(root, files[i]))
                    cv2.imshow(os.path.join(root, files[i]), img)
                    k = cv2.waitKey(33)
                    print(k)
                    if k == 97: # a
                        i = i - 1
                        cv2.destroyAllWindows()
                        coordinates = []
                    if k == 100: # d
                        i += 1
                        cv2.destroyAllWindows()
                        coordinates = []
                    if k == 119: # w
                        label[files[i]] = 1
                        i += 1
                        cv2.destroyAllWindows()
                        coordinates = []
                    if k == 101: # e
                        label[files[i]] = 0
                        i += 1
                        cv2.destroyAllWindows()
                        coordinates = []
                    if k == 122: # z
                        coordinates = []
                    if k == 120: # x
                        coordinates = coordinates[:-1]
                    if k == 102: # f
                        i += 7
                        cv2.destroyAllWindows()
                        coordinates = []
                    if k == 115: # s
                        import pdb; pdb.set_trace()
                        coordinates = []
                    if k == 113: # q
                        cv2.destroyAllWindows()
                        done_labeling_flag = 1
                else:
                    i += 1
                    coordinates = []
            else:
                done_labeling_flag = 1


        #
        # for file in files:
        #     if file[-3:] == "jpg":
        #         picture_files.append(os.path.join(root, file))
        #         coordinates = []
        #         img = cv2.imread(os.path.join(root, file))
        #         print(os.path.join(root, file))
        #         cv2.imshow('img', img)
        #         flag = 1
        #         while flag:
        #             if cv2.waitKey(0):
        #                 flag = 0
        #         if len(coordinates):
        #             with open(os.path.join(root, file[:-4] + ".txt"), 'w+') as f:
        #                 f.write(str(coordinates))
        #             first_pt = []
        #             second_pt = []
        #             flag = 0
        #             for coord in coordinates:
        #                 if flag:
        #                     second_pt.append(coord)
        #                     flag = 0
        #                 else:
        #                     first_pt.append(coord)
        #                     flag = 1
        #             for f, s in zip(first_pt, second_pt):
        #                 cv2.rectangle(img, f, s, (255, 0, 0), 1)
        #             cv2.imshow('img', img)
        #             cv2.waitKey(0)

        break

    with open(os.path.join(filepath, "labels.json"), "w+") as f:
        json.dump(label, f)
