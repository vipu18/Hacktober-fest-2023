import cv2
import winsound
cam = cv2.VideoCapture(0)


while cam.isOpened():
    ret, frame1 = cam.read() # Creating Frame 1 
    # Creating a second frame so that we can idenfity the motion
    ret, frame2 = cam.read() 
    # Taking the abs difference between the frames so that we can capture the motion
    diff = cv2.absdiff(frame1, frame2)
    
    # Converting the frame to Gray 
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    
    # Since we are using a  Gaussian Blur we cvted our image to gray color
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # We are then applying a threshold to get rid of the noise 
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    # We are using dilate here to increase the object area
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    # To draw a Boundary near the dilated part we are using contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Drawing the Contours to our Frame
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    
    # Getting the Motion Only for a bigger object
    for c in contours:
        # It will skip the motion < 5000 area
        if cv2.contourArea(c) < 5000:
            continue
        # Getting the x-cor, y-cor, width & height for each contours
        x, y, w, h = cv2.boundingRect(c)
        # Drawing the rectange for the above contours C
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Adding our Alert Sound
        # Sync the sound asynchronously 
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
    
    
    
    
    cv2.imshow('Security Cam', frame1)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyWindow('Security Cam')
        cam.release()
        break
