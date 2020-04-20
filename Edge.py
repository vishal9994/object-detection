import cv2

def main():
    
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,frame=cap.read() 
    else:
        ret=False
    
    while ret:
        
        edge_frame = cv2.Canny(frame,50,350,L2gradient=False)
        cv2.imshow("edge detection",edge_frame)
        if cv2.waitKey(1)==27:
            break
        ret, frame = cap.read()
        
    cv2.destroyAllWindows()    
    cap.release()
    
if __name__=="__main__":
    main()