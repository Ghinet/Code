import face_recognition
import cv2 # pip install opencv-python

webcam = cv2.VideoCapture(0) # 0 è la prima webcam del sistema, per me è 1000 (id -a, gid)

image_file = input("Immagine target > ") # l'utente può inserire l'immagine target (know)
target_image = face_recognition.load_image_file(image_file)
target_encoding = face_recognition.face_encodings(target_image)[0]

print("Immagine caricata;\nCodifica a 128 dimensioni: generata;")
target_name = input("Nome Target > ")

# riduciamo un po' di carico sul processo

process_this_frame = True #loop infinito perchè analiziamo un flusso continuo di dati dalla webcam

while True:   
    ret, frame = webcam.read() # ret sta per return, flag booleano
    
    small_frame = cv2.resize(frame, None, fx=0.20, fy=0.20) #scaliamo la dimensione del frame di 1\5 della sua dimensione originale
    rgb_small_frame = cv2.cvtColor(small_frame, 4) # convertire da bgr usato da cv2  a rgb usato da face_recognition, 4 è il numero associato alla conversione da bgr a rgb
    

    if process_this_frame:

        face_location = face_recognition.face_locations(rgb_small_frame) # posizione del viso all'interno dell'immagine
        frame_encoding = face_recognition.face_encodings(rgb_small_frame) # codifico quel frame per quell'immagine

        if frame_encodings:
            frame_face_encoding = frame_encodings[0]
            match = face_recognition.compare_faces([target_encoding], frame_face_encoding)[0] #compariamo i frame della webcam col nostro target
            label = target_name if match else "Unknown"

    process_this_frame = not process_this_frame #???

    if face_location:
        top, right, bottom, left = face_location[0] # verifico che esistano le coordinate della locazione

        top *= 5  # resize alla dimensione originale
        right *= 5
        bottom *= 5
        left *= 5
 
        #disegno il rettangolo attorno al volto dato che ho le coordinate di riconoscimento 
        cv2.rectangle(frame, (left,top), (right,bottom), (0, 255 ,0), 2) #2 è lo spessore
        cv2.rectangle(frame, (left, bottom - 30), (right,bottom), (0, 255 ,0), cv2.FILLED) #riemimento filled
        label_font = cv2.FONT_HERSEY_DUPLEX #definiamo una tipologia di font
        cv2.putText(frame, label, (left + 6, bottom - 6), label_font, 0.8, (255, 255, 255), 1) #inseriamo tsto nell'etichetta
    cv2.imshow("Video Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #definiamo il tasto 'q' per chiudere il programma 
        break

    webcam.release()
    cv2.destroyAllWindows()




