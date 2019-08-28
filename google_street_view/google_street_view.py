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
heading = ['0', '90', '180', '270']
rtk_csv = "/home/brian/Downloads/190710_132237_short.csv"
df = pd.read_csv(rtk_csv)


##### USED FOR FILTERING OUT RTK GPS LOGS TO FEWER GPS POINTS #######
# flag = 0
# dist_threshold = 40
# i = 0
#
# gps_df = pd.DataFrame()
# gps_df["latitude"] = list(df["Latitude (deg)"])
# gps_df["longitude"] = list(df["Longitude (deg)"])
# gps_df["time"] = list(df["Time from initialisation (s)"])
# gps_df["speed"] = list(df["Speed 3D (m/s)"])
# sampling_rate = (gps_df["time"][len(gps_df) - 1] - gps_df["time"][0]) / len(gps_df["time"])
# gps_df["dist_inst"] = gps_df["speed"] *sampling_rate
# gps_df["dist_cum"] = list(np.cumsum(gps_df["dist_inst"]))
# temp_mask = list(np.diff(np.floor_divide(list(gps_df["dist_cum"]), dist_threshold)))
# temp_mask.insert(0, 0)
# gps_df["mask"] = list(temp_mask)
#
#
# filered_df = pd.DataFrame()
# for index, row in gps_df.iterrows():
#     if row["mask"]:
#         filered_df = filered_df.append(row)
#
#
# print(filered_df)
# filered_df.to_csv("/home/brian/Downloads/190710_132237_short.csv")



latitude = df["latitude"]
longitude = df["longitude"]
i=195
for lat, lon in zip(latitude[295:], longitude[295:]):
    lat = round(lat, 6)
    lon = round(lon, 6)
    coord = str(lat)+","+str(lon)
    coord = coord.replace(" ", "")
    for head in heading:
        params = [{
            'size': '640x640',  # max 640x640 pixels
            'location': coord,
            'heading': head,
            'pitch': '0.0',
            'fov': '90',
            'save_downloads': '/home/brian/Pictures/GSV_scrape/gvc.jpg',
            'key': 'AIzaSyCCpqGNlnuqVbJ70zFMBaQMuUE-eqjwCzQ'

        }]
#
        results = gsv.results(params)
        results.download_links(main_save_link + coord + '/' + head)
    img_concat = []
    for head in heading:
        for root, dirs, files in os.walk(main_save_link+coord+'/'+head):
            for file in files:
                if file[-4:] == '.jpg':
                    picture_file = os.path.join(root, file)
                    img = cv2.imread(picture_file)
                    if not len(img_concat):
                        img_concat = img
                    else:
                        img_concat = np.concatenate((img_concat, img), axis=1)
    try:
        cv2.imwrite(os.path.join(main_save_link, str(i).zfill(4)+"_"+coord+".jpg"), img_concat)
        i +=1
    except:
        print("There is no image available for (" + coord + ").")
    shutil.rmtree(main_save_link + "/" + coord)
#     #                 copyfile(picture_file, os.path.join(remember, heading + ".jpg"))
#     #     else:
#     #         remember = root
#     #
#     #     print(root)
#     #     print(dirs)
#     #     print(files)
#
#
