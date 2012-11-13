import cv2
classifier = cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture()
camera.open(0)
while True:
    frame = camera.read()[1]
    detections = classifier.detectMultiScale(frame)

    print('n_faces: {}'.format(len(detections)))
