
import cv2
import face_recognition
imgOpen = face_recognition.load_image_file('faces/loki.jpg')
imgOpen = cv2.cvtColor(imgOpen,cv2.COLOR_BGR2RGB)
encodeOpen = face_recognition.face_encodings(imgOpen)[0]

imgClosed = face_recognition.load_image_file('faces/closed-loki.jpg')
imgClosed = cv2.cvtColor(imgClosed,cv2.COLOR_BGR2RGB)
encodeClosed = face_recognition.face_encodings(imgClosed)[0]


def match_face(imgTest):
    try:
        imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
        encodeTest = face_recognition.face_encodings(imgTest)[0]
        
        results1 = face_recognition.compare_faces([encodeOpen],encodeTest)
        # faceDis = face_recognition.face_distance([encodeOpen],encodeTest)
        
        results2 = face_recognition.compare_faces([encodeClosed],encodeTest)

        if results1[0] or results2[0]:
            return True
        else:
            return False
    except:
        print("Issue")
        return False

