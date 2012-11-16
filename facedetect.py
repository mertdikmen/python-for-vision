import cv2
classifier = cv2.CascadeClassifier("data/haarcascade_frontalface_alt.xml")
camera = cv2.VideoCapture()
camera.open(0)
cv2.namedWindow('video')
while True:
    frame = camera.read()[1]
    detections = classifier.detectMultiScale(frame)
    for detection in detections:
        cv2.rectangle(frame, tuple(detection[:2]), tuple(detection[:2] + detection[2:]), (255,0,0))
    cv2.imshow('video',frame)
    key = cv2.waitKey(1)
    if key == 113:
        break
cv2.destroyAllWindows()