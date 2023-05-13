# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:50:54 2021

@author: Aniket
"""


import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import shutil



def findEncodings():
    encodeListKnown = []
    imgNames = []
    
    
    with open("attendance_encodings.csv", "r") as f:
        
       for ln in f.readlines():
            imgNames.append(ln.split(',')[0].strip())
            encode = list(map(float,ln.split(',')[1:]))
            print(encode)
            encodeListKnown.append(encode)
        
    return encodeListKnown, imgNames


def checkName(name):
    enc, names = findEncodings()
    names = [x.lower().strip() for x in names]
    print(names)
    name = name.split('.')[0].lower()
    print(name)
    if name in names:
        return True
    else:
        return False

def live():
    
    encodeListKnown = []
    imgNames = []
    
    encodeListKnown, imgNames = findEncodings()
    
    ############################
    # Testing using the video Camera
    ############################
    
    frameWidth = 640
    frameHeight = 480
    
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    
    
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
        # Finding encoding of the web cam
        
        
        facesCurFrame = face_recognition.face_locations(imgS)  # To get locations of all the faces in the frame
        encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)   # To get encoding of the faces in the current frame    
        
        for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)
            
            if matches[matchIndex]:
                name = imgNames[matchIndex].upper()
                # print(name)
                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            
            
        cv2.imshow("Video", img)
        
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
    
    
def upload(img, name):
    originalD = img
    print(originalD)
    imgnm = os.path.basename(originalD)
    path = r"C:\Users\Kratika\Python36\gui\attendace app"
    path = os.path.join(path,imgnm)
    print(path)    
    attendPath = r"C:\Users\Kratika\Python36\gui\attendace app\attendance_encodings.csv"
    name = name.strip()
    if not os.path.isfile(path):
        shutil.copyfile(originalD, path)
    if not checkName(name):
        img = cv2.imread(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        with open(attendPath, 'a+') as f:
            encode = str(list(encode))
            encode = encode.replace('[','')
            encode = encode.replace(']','')
            
            f.writelines(f'{name},{encode}\n')
        print("Encoding Complete")
    else:
        print("Already There")
        

def identify(img):
    
    cap = cv2.imread(img)  # AniDha2.jpeg, AniDha3.jpeg
    
    img = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)
    
    
    encodeListKnown = []
    imgNames = []
    
    encodeListKnown, imgNames = findEncodings()
    
    
    facesCurFrame = face_recognition.face_locations(img)  # To get locations of all the faces in the frame
    encodeCurFrame = face_recognition.face_encodings(img, facesCurFrame)   # To get encoding of the faces in the current frame    
    
    print(facesCurFrame)
    print(encodeCurFrame)
    
            
    
    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        
        if min(faceDis)<0.50:
            if matches[matchIndex]:
                name = imgNames[matchIndex].upper()
                print(name)
                y1,x2,y2,x1 = faceLoc
                print(faceLoc)
                cv2.rectangle(cap, (x1,y1), (x2,y2), (255,0,255), 2)
                cv2.rectangle(cap, (x1, y2-10), (x2,y2+10), (255,0, 255), cv2.FILLED)
                cv2.putText(cap, name, (x1+2, y2+10), cv2.FONT_HERSHEY_COMPLEX, 0.80, (255,255,255), 2)
                # markAttendance(name)
    
            
            
    
    cv2.imshow("Identify", cap)
    
    cv2.waitKey(0)    
        
    
    cv2.destroyAllWindows()
    

            
        
        
