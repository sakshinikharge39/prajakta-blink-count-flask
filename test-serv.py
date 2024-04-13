from flask import Flask, request
import base64
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
from faceDetect import match_face
from PIL import Image
import numpy as np
import os

idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
ratioList = []
blinkCounter = 0
counter = 0
color = (255, 0, 255)
detector = FaceMeshDetector(maxFaces=1)

app = Flask(__name__)


def count_blink(img_path):
    global counter
    global blinkCounter
    img = np.array(Image.open(img_path))
    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        face = faces[0]
        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]
        lenghtVer, _ = detector.findDistance(leftUp, leftDown)
        lenghtHor, _ = detector.findDistance(leftLeft, leftRight)

        # so we will take the ratio like up doen and left right
        ratio = int((lenghtVer / lenghtHor) * 100)
        ratioList.append(ratio)
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList) / len(ratioList)
        print("rationAVG", ratioAvg, "counter ", counter)
        if ratioAvg < 40 and counter == 0:
            blinkCounter += 1
            counter = 1
        if counter != 0:
            counter += 1
            if counter > 2:
                counter = 0

    else:
        print("No face")

    return blinkCounter


@app.route('/camera', methods=['POST'])
def upload_video():
    face = request.files["face"]
    face.save(f"captures/{face.filename}")
    cnt = count_blink(f"captures/{face.filename}")
    print(cnt)
    return f"{cnt}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
