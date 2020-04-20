import cv2

def main():
    
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,frame2=cap.read() 
    else:
        ret=False
    
    frame1=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    
    while ret:
        
        frame2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        d = cv2.absdiff(frame1,frame2)
        cv2.imshow("motion tracking",d)
        if cv2.waitKey(1)==27:
            break
        
        frame1=frame2
        ret, frame2 = cap.read()
        
    cv2.destroyAllWindows()    
    cap.release()
    
if __name__=="__main__":
    main()
