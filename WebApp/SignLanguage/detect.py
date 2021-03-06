from flask import Blueprint, render_template, Response
import cv2
import time
import pickle
import numpy as np
import pyttsx3
import mediapipe as mp

detect= Blueprint('detect',__name__)
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
drawing_styles = mp.solutions.drawing_styles

mod = pickle.load(open('/XGBoost.sav', 'rb'))
le = pickle.load(open('/XEncoder1.sav', 'rb'))
word = ' '
cap = cv2.VideoCapture(0)

def play_voice(mytext):
    converter = pyttsx3.init()
    converter.setProperty('rate', 120)
    converter.setProperty('volume', 1.0)
    converter.say(mytext)
    converter.runAndWait()

def gen_frames():  
    global word
    prev = time.time()
    with mp_hands.Hands(min_detection_confidence=0.67, min_tracking_confidence=0.4) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break
            else:
                curr = time.time()
                image = cv2.cvtColor(cv2.flip(image,1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                # Draw the hand annotations on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:
                    lst = []
                    for coords in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image, coords, mp.solutions.hands.HAND_CONNECTIONS,
                            drawing_styles.get_default_hand_landmarks_style(),
                            drawing_styles.get_default_hand_connections_style())
                    for crd in coords.landmark:
                        lst.append(crd.x)
                        lst.append(crd.y)
                        lst.append(crd.z)
                    lst = np.asarray(lst).reshape(1,-1)
                    if (curr-prev) >= 4:
                        prev = time.time()
                        txt = predict(lst)
                        if txt=='del': word = word[:-1]
                        elif txt == 'space': word += ' '
                        else: word+=txt
                        print(f'{txt} ---- {word}')
                ret, buffer = cv2.imencode('.jpg', image)
                frame = buffer.tobytes()
                yield (b'--frame\r\n' b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')
                        # play_voice.remote(word)
            #     cv2.imshow('MediaPipe Hands', image)
            #     if cv2.waitKey(5) & 0xFF == 27:
            #         break
            # cap.release()


def predict(coords):
    tmp = mod.predict(coords)
    txt = str(le.inverse_transform(tmp)).strip("'][")
    return txt 

@detect.route('/start', methods=['POST'])
def index():
    return render_template('index1.html')

@detect.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('signup.html')

@detect.route('/video_feed', methods=['GET','POST'])
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@detect.context_processor
def text_feed():
    return dict(text_feed=word)

# @app.route('/text_feed')
# def text_feed():
    
#     return Response(print_html(), mimetype='text/html')

# if __name__ == "__main__":
#     app.run(debug=True)
