import cv2,winsound
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    faces = face.detectMultiScale(gray, 1.3, 6,0,(140,140),(250,250))
    mask = True
    for x, y, w, h in faces:
        smiles = smile.detectMultiScale(gray[y:y + h, x:x + w], 1.2, 4,0,(85,85),(90,90))
        #pesan = 'Dengan Masker'
        #color=(255, 0, 0)
        for ex, ey, ew, eh in smiles:
            pesan = 'Tanpa Masker'
            color = (0,0, 255)
            winsound.Beep(2500, 100)
        cv2.rectangle(gray, (x, y), (x + w, y + h), color, 2)
        cv2.putText(gray, pesan, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,color, 2)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()