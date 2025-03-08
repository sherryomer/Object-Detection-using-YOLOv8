from ultralytics import YOLO
import cv2
model = YOLO('best.pt')
cap = cv2.VideoCapture(0) 
model.predict(source='0',show=True, conf = 0.5)
cap = cv2.VideoCapture(0, apiPreference=cv2.CAP_AVFOUNDATION)