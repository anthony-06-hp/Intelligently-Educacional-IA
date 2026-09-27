import cv2
import os

def get_next_person_name(save_dir='dataset'):
    os.makedirs(save_dir, exist_ok=True)
    existing = [d for d in os.listdir(save_dir) if os.path.isdir(os.path.join(save_dir, d)) and d.startswith("persona")]
    numbers = [int(d.replace("persona", "")) for d in existing if d.replace("persona", "").isdigit()]
    next_number = max(numbers) + 1 if numbers else 1
    return f"persona{next_number}"

def capture_faces(person_name, save_dir='dataset', num_images=200):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    person_dir = os.path.join(save_dir, person_name)
    os.makedirs(person_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    count = 0

    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            face_img = cv2.resize(face_img, (224, 224))  # tamaño recomendado para VGG-Face
            
            img_path = os.path.join(person_dir, f'{count}.jpg')
            cv2.imwrite(img_path, face_img)
            count += 1

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, f'{person_name} | {count}/{num_images}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        
        cv2.imshow('Capture Faces', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Captura completada para {person_name}.")

# --- Ejecutar automáticamente con nombre incremental ---
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        nombre_persona = sys.argv[1]
    else:
        nombre_persona = get_next_person_name()
    capture_faces(nombre_persona, num_images=200)
# --- Fin del código ---
