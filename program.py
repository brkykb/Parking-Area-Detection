import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("model.keras")

root = tk.Tk()
root.title("Video Analysis Interface")
root.geometry("400x200")

video_path = ""
coord_path = ""



def select_video():
    global video_path
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
    print(f"📹 Selected video: {video_path}" if video_path else "❗ No video selected.")

def select_coords():
    global coord_path
    coord_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    print(f"📌 Selected coordinate file: {coord_path}" if coord_path else "❗ No coordinate file selected.")

def run_model():
    if not video_path or not coord_path:
        print("❌ Please select both video and coordinate file.")
        return

    cap = cv2.VideoCapture(video_path)

    boxes = []
    with open(coord_path, 'r') as f:
        for line in f:
            try:
                parts = list(map(int, line.strip().split(',')))
                if len(parts) == 4:
                    boxes.append(tuple(parts))
            except:
                print(f"⚠️ Skipped invalid line: {line.strip()}")

    if not boxes:
        print("❌ Coordinate file is empty or invalid.")
        cap.release()
        return

    frame_count = 0
    predictions = [("Empty", (0, 255, 0))] * len(boxes)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 5 == 0:
            new_predictions = []
            for (x1, y1, x2, y2) in boxes:
                h, w, _ = frame.shape
                x1 = max(0, min(x1, w - 1))
                x2 = max(0, min(x2, w - 1))
                y1 = max(0, min(y1, h - 1))
                y2 = max(0, min(y2, h - 1))

                if x2 <= x1 or y2 <= y1:
                    print(f"⚠️ Invalid box skipped: ({x1}, {y1}, {x2}, {y2})")
                    new_predictions.append(("Invalid", (255, 255, 255)))
                    continue

                roi = frame[y1:y2, x1:x2]
                resized = cv2.resize(roi, (300, 150))
                norm = resized.astype(np.float32) / 255.0
                pred = model.predict(np.expand_dims(norm, axis=0), verbose=0)[0][0]

                label = "Full" if pred < 0.5 else "Empty"
                color = (0, 0, 255) if pred < 0.5 else (0, 255, 0)
                new_predictions.append((label, color))

            predictions = new_predictions

        # Draw model predictions
        for (coords, (label, color)) in zip(boxes, predictions):
            x1, y1, x2, y2 = coords
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Draw manual red box (always occupied)
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(frame, "Full", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv2.imshow("Prediction Result", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

btn1 = tk.Button(root, text="🎥 Select Video", command=select_video)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="📝 Select Coordinate File", command=select_coords)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="🚀 Run Model", command=run_model)
btn3.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", root.destroy)
root.mainloop()
