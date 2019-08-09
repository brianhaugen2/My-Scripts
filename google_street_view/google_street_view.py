import numpy as np
import pandas as pd
import google_streetview.api as gsv
import cv2
import os
import shutil

def delta_calc(original: list) -> list:
    temp = original
    temp.remove(temp[-1])
    temp.insert(0, temp[0])
    return list(np.subtract(original, temp))







main_save_link = "/home/brian/Pictures/GSV_scrape/"

lat = 42.160673
lon = -83.797689

heading = ['0', '90', '180', '270']
rtk_csv = "/home/brian/Downloads/190710_132237.csv"

gps_df = {
    "latitude": [],
    "longitude": []
}
df = pd.read_csv(rtk_csv)
flag = 0
dist_threshold = 40
i = 0

gps_df = pd.DataFrame()
gps_df["latitude"] = list(df["Latitude (deg)"])
gps_df["longitude"] = list(df["Longitude (deg)"])
gps_df["time"] = list(df["Time from initialisation (s)"])
gps_df["speed"] = list(df["Speed 3D (m/s)"])
gps_df["time_delta"] = delta_calc(list(gps_df["time"]))
gps_df["dist_inst"] = gps_df["speed"] * gps_df["time_delta"]
gps_df["dist_cum"] = list(np.cumsum(gps_df["dist_inst"]))
temp_mask = list(np.diff(np.floor_divide(list(gps_df["dist_cum"]), dist_threshold)))
temp_mask.insert(0, 0)
gps_df["mask"] = list(temp_mask)




for index, row in df.iterrows():
    if not flag:
        prev_time = row["Time from initialisation (s)"]
        dist = 0
        flag = 1
    else:
        time = row["Time from initialisation (s)"]
        speed = row["Speed 3D (m/s)"]
        dist += speed * (time - prev_time)
        if dist >= dist_threshold:
            gps_df["latitude"].append(row["Latitude (deg)"])
            gps_df["longitude"].append(row["Longitude (deg)"])
            dist = 0
            prev_time = row["Time from initialisation (s)"]
        else:
            prev_time = row["Time from initialisation (s)"]


print(gps_df[:100])



#
# # for coord in gps_points:
# for i in list(range(100)):
#     lat = round(lat - 0.0001, 6)
#     lon = round(lon - 0.0001, 6)
#     coord = str(lat)+","+str(lon)
#     coord = coord.replace(" ", "")
#     for head in heading:
#         params = [{
#             'size': '640x640',  # max 640x640 pixels
#             'location': coord,
#             'heading': head,
#             'pitch': '0.0',
#             'fov': '90',
#             'save_downloads': '/home/brian/Pictures/GSV_scrape/gvc.jpg',
#             'key': 'AIzaSyCCpqGNlnuqVbJ70zFMBaQMuUE-eqjwCzQ'
#
#         }]
#
#         results = gsv.results(params)
#         results.download_links(main_save_link + coord + '/' + head)
#     img_concat = []
#     for head in heading:
#         for root, dirs, files in os.walk(main_save_link+coord+'/'+head):
#             for file in files:
#                 if file[-4:] == '.jpg':
#                     picture_file = os.path.join(root, file)
#                     img = cv2.imread(picture_file)
#                     if not len(img_concat):
#                         img_concat = img
#                     else:
#                         img_concat = np.concatenate((img_concat, img), axis=1)
#     cv2.imwrite(os.path.join(main_save_link, coord+".jpg"), img_concat)
#     cv2.imshow("img", img_concat)
#     cv2.waitKey(0)
#     shutil.rmtree(main_save_link + "/" + coord)
#     #                 copyfile(picture_file, os.path.join(remember, heading + ".jpg"))
#     #     else:
#     #         remember = root
#     #
#     #     print(root)
#     #     print(dirs)
#     #     print(files)
#
#
