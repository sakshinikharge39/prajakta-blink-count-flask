import cv2

from faceDetect import match_face

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

print(match_face(frame))
cv2.imshow("s", frame)
if cv2.waitKey(0):
    cap.release()


# cap.release()
