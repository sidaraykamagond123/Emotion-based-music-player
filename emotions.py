#! C:\Python\Python39\python.exe
from tkinter import *
from subprocess import call
from random import randint
from pathlib import Path
import time
import vlc
import cgi
import os
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.models import Sequential
import cv2
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'
# music player function


def music_player(emotion_str):
    from musicplayer import MusicPlayer
    root = Tk()
    print('\nPlaying ' + emotion_str + ' songs')
    MusicPlayer(root, emotion_str)
    root.mainloop()


# Create the model
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3),
          activation='relu', input_shape=(48, 48, 1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))


model.load_weights('model.h5')

print('\n Welcome to Emotion based Music Player \n')
print('\n Press \'q\' to exit the music player \n')
# prevents openCL usage and unnecessary logging messages
cv2.ocl.setUseOpenCL(False)

# dictionary which assigns each label an emotion (alphabetical order)
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful",
                3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# File to append the emotions
with open(str(Path.cwd())+"\emotion.txt", "w") as emotion_file:

    # start the webcam feed
    cap = cv2.VideoCapture(0)
    now = time.time()  # For calculate seconds of video
    future = now + 10
    while True:
        # Find haar cascade to draw bounding box around face
        ret, frame = cap.read()
        if not ret:
            break
        facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facecasc.detectMultiScale(
            gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(
                cv2.resize(roi_gray, (48, 48)), -1), 0)
            prediction = model.predict(cropped_img)
            maxindex = int(np.argmax(prediction))
            cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            text = emotion_dict[maxindex]
            emotion_file.write(emotion_dict[maxindex]+"\n")
            emotion_file.flush()

        cv2.imshow('Video', cv2.resize(
            frame, (1600, 960), interpolation=cv2.INTER_CUBIC))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if time.time() > future:  # after 2 second music will play
            cv2.destroyAllWindows()
            music_player(text)
            future = time.time() + 2

    cap.release()