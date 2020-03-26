#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:10:37 2020

@author: yitaogao
"""

import pickle
import cv2

class newRGBFrame:
    def __init__(self, timestamp, camera_id, frame):
        self.timestamp = timestamp
        self.camera_id = camera_id
        self.frame = frame
        
## parameters that you can change
test_name = 'cps-test-02'    
## The RGB is too large to pull out at once therefore seperated into small trunks of pickles
pikle_num = 10           
fps = 10
new_dict=[]
## fixed number of camera
camera_num = 12

for pickle_i in range(pikle_num):
    ## my file name: frame-cps-test-02-frame_message1.pkl
    filename='frame-'+test_name+'-frame_message'+str(pickle_i+1)+'.pkl'
    with open(filename,'rb') as f:
        new_dict += (pickle.load(f))


lista= set()
for item in new_dict:
    lista.add(item.camera_id)    

framearray_list=[[] for i in range(camera_num)]

for i in range (12):

    for rgbream in new_dict:
        if rgbream.camera_id == i+1:
            img = rgbream.frame
            height, width, layers = img.shape
            size = (width,height)
            
            #inserting the frames into an image array
            framearray_list[i].append(img)
    save_path = 'video/'+test_name+'-'+str(1+i)+'.mp4'
    out = cv2.VideoWriter(save_path,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for j in range(len(framearray_list[i])):
        # writing to a image array
        out.write(framearray_list[i][j])
    out.release()
        