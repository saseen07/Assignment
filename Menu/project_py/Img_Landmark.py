import sys
import cv2
import matplotlib.pyplot as plt
#import face_recognition

filePath = sys.argv[1]
# Load image:
img = cv2.imread(filePath)

# Create imgs to show the results:
img68 = img.copy()
img5 = img.copy()



# Detect 68 landmarks:
face_landmarks_list_68 = face_recognition.face_landmarks(img68)

#print(face_landmarks_list_68)

# Draw all detected landmarks:
for face_landmarks in face_landmarks_list_68:
    for facial_feature in face_landmarks.keys():
        for p in face_landmarks[facial_feature]:
            cv2.circle(img68, p, 3, (0, 255, 0), -1)

# Detect 5 landmarks:
face_landmarks_list_5 = face_recognition.face_landmarks(img5, None, "small")

#print(face_landmarks_list_5)

# Draw all detected landmarks:
for face_landmarks in face_landmarks_list_5:
    for facial_feature in face_landmarks.keys():
        for p in face_landmarks[facial_feature]:
            cv2.circle(img5, p, 3, (0, 255, 0), -1)

if img is None:
    sys.exit("Could not read the image.")

# display file
cv2.imshow("68 Facial Landmark", img68)

k = cv2.waitKey(0)

if k != ord("q"):
    cv2.imshow("5 Facial Landmark", img5)
    y = cv2.waitKey(0)


cv2.destroyAllWindows()