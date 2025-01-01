import cv2
import mediapipe.python.solutions.hands as mp_hands
import math
import subprocess
try:
    subprocess.Popen(['python', "SandySerial.py"])
    print(f"Started running SandySerial.py in the background.")
except FileNotFoundError:
    print(f"Error: Could not find SandySerial.py.")
except Exception as e:
    print(f"An error occurred while running SandySerial.py: {e}")
cap = cv2.VideoCapture(0)
file = open("liveDrawComms.txt","w")
file.write("0,0")
file.close()
with mp_hands.Hands(
    model_complexity=1,
    max_num_hands=2,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8,
) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame...")
            continue
        height, width, channels = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            x=0
            fx = 0
            fy = 0
            for hand_landmarks in results.multi_hand_landmarks:
                for xy in hand_landmarks.landmark:
                    x+=1  
                    if x == 5:
                        fx = int(xy.x*width)
                        fy = int(xy.y*height)      
                        cv2.circle(frame,(int(xy.x*width),int(xy.y*height)),2,(0,0,0),-1)
                    if x == 9:
                        cv2.line(frame,(fx,fy),(int(xy.x*width),int(xy.y*height)),(255,0,0),3)                 
                        cv2.circle(frame,(int(xy.x*width),int(xy.y*height)),2,(0,0,0),-1)
                        color = (0,0,0)
                        if (((fx-int(xy.x*width))**2)+((fy-int(xy.y*height))**2))**0.5 < 15*2:
                            color = (0,255,0)
                            x2,y2 = (int((xy.x*width + fx)/2),int((xy.y*height + fy)/2))
                            x1,y1 = (int(0.5*width),int(0.5*height))
                            cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),3)
                            delta_x = x2 - x1
                            delta_y = y2 - y1
                            angle_radians = math.atan2(delta_y, delta_x)
                            angle_degrees = math.degrees(angle_radians)
                            angle_degrees-=90
                            if angle_degrees < 0:
                                angle_degrees += 360
                            distance = (((y2-y1)**2)+((x2-x1)**2))**0.5
                            distance*=83/150
                            if distance > 83:
                                distance = 83
                            file = open("liveDrawComms.txt","r")
                            a = file.read()
                            a = a.split("\n")
                            b = a[len(a)-1].split(",")
                            if len(b)!=2:
                                file.close()
                                f = open("liveDrawComms.txt","a")
                                f.write(str(int(angle_degrees))+","+str(int(distance)))
                                f.close()
                            elif abs(int(b[0])-angle_degrees)>5:
                                file.close()
                                f = open("liveDrawComms.txt","a")
                                f.write("\n"+str(int(angle_degrees))+","+str(int(distance)))
                                f.close()
                            elif abs(int(b[1])-distance)>5:
                                file.close()
                                f = open("liveDrawComms.txt","a")
                                f.write("\n"+str(int(angle_degrees))+","+str(int(distance)))
                                f.close()
                            else:
                                file.close()
                        cv2.circle(frame,(int((xy.x*width + fx)/2),int((xy.y*height + fy)/2)),5,color,-1)
                        cv2.circle(frame,(int((xy.x*width + fx)/2),int((xy.y*height + fy)/2)),15,color,2)
        cv2.circle(frame,(int(0.5*width),int(0.5*height)),150,(0,0,0),2)
        cv2.imshow("Hand Tracking", cv2.flip(frame, 1))
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
