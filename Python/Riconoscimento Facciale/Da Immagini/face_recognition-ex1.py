# restituisce i vnumpy array delle immagini caricate


import face_recognition

known_image = face_recognition.load_image_file("enrico_mentana.jpg")
unknown_image = face_recognition.load_image_file("other1.jpg")

#print(type(known_image)) # class 'numpy.ndarray'
#print(f"{known_image}")  # l'array

known_encoding = face_recognition.face_encodings(known_image)[0] #indice 0 perchè mi interessa solo il primo elemnto della lista, ovvero il primo volto essendo anche l'unico
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

#print(known_encoding) # risultato della codifica, 129 misurazioni, embeding dell'immagine

results = face_recognition.compare_faces([known_encoding], unknown_encoding) #primo parametro, lista di encoding da comparare con il secondo parametro, l'encoding dell'immagine di interesse
answer = "Si" if results[0] else "No"

print(f"L'immagine sconosciuta raffigura Enrico Mentana? { answer }")

face_distance = face_recognition.face_distance([known_encoding], unknown_encoding)
match = True if face_distance[0] <= 0.6 else False

#print("Range Distanza [0.0 - 1.0]")
#print(f"L'immagine testata ha una distanza di {face_distance[0]:.2} dell'immagine conosciuta")
#print(f"Match: {match}")

percentuale = 100-(float(face_distance[0]) * 100)
print(f"Somiglianza del {percentuale:.5}%\nTra lo 0 e il 40% di somiglianza, risulterà che la persona presente non è la stessa.\nOltre il 40% di somiglianza, risuletrà essere la stessa persona.")

# è possibile confrontare una cartella di immagine note con una cartella di immagini sconosciute per 
# ottenere l'abbinamento di un'immagine nota ad una ignota a seconda della somiglianza
# con i comandi "face_recognition knwon_people_folder unknown_people_folder"
# es face_recognition ./know_people/ ./random_photos/
# il comando va eseguito nella directory cove sono presenti le due cartelle

