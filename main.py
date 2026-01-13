import cv2
import mediapipe as mp
import PoseModule as pm
import time
import math

cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()

def distance(point1,point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

while True:
    success,img = cap.read()
    h,w,c = img.shape

    img = detector.findPose(img,draw=False)
    lmlist = detector.findPosition(img)

    if lmlist:
        right_shoulder = lmlist[12][1:]
        left_shoulder = lmlist[11][1:]
        cv2.line(img,left_shoulder,right_shoulder,(255,255,255),2)
        cv2.circle(img,left_shoulder,10,(0,0,255),cv2.FILLED)
        cv2.circle(img,right_shoulder,10,(0,0,255),cv2.FILLED)
        
        # cv2.circle(img,(w//2,0),10,(0,0,255),cv2.FILLED)
        # cv2.circle(img,(w//2,h),10,(0,0,255),cv2.FILLED)
        upper_point = (w//2,0)
        lower_point = (w//2,h)

        mid_point = ((left_shoulder[0]+right_shoulder[0])//2,(left_shoulder[1]+right_shoulder[1])//2)

        upper_distance = distance(mid_point,upper_point)
        lower_distance = distance(mid_point,lower_point)

        print(f"upper distance: {upper_distance}")
        print(f"lower distance: {lower_distance}")


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime= cTime

    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow('image',img)

    if cv2.waitKey(30)==27:
        break
