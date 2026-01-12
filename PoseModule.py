import cv2
import mediapipe as mp
import time

class poseDetector():

    def __init__(self,mode = False,upBody = False,smooth = True):
        
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        # self.detectionCon = detectionCon
        # self.trackCon = trackCon

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth)
        self.mpDraw = mp.solutions.drawing_utils


    def findPose(self,img,draw=True):


        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        # print(results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)

        return img
    

    def findPosition(self,img,draw=False):
        lmlist = []
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                # print(id,lm)
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
        return lmlist
    

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmlist = detector.findPosition(img)

        if lmlist:
            print(lmlist)
            # to highlight particular point
            #cv2.circle(img,(lmlist[0][1],lmlist[0][2]),15,(0,0,255),cv2.FILLED)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime= cTime

        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

        cv2.imshow('image',img)

        if cv2.waitKey(30)==27:
            break


if __name__ == '__main__':
    main()