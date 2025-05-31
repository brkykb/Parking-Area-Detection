import cv2
coords = []

#koordinat çıkarma yapılırken hep sol köşeden sağ alt köşeye doğru seçilmeli yoksa koordinat adresleri ters olduğu için hata veriyor 

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coords.append((x, y))
        print(f"Koordinat: {x},{y}")
        if len(coords) % 2 == 0:
            cv2.rectangle(img, coords[-2], coords[-1], (0, 255, 0), 2)
            cv2.imshow("Frame", img)

# Video veya resimden ilk frame al
cap = cv2.VideoCapture("/test_files/test_video.mp4")
ret, img = cap.read()
cap.release()

cv2.imshow("Frame", img)
cv2.setMouseCallback("Frame", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Koordinatları kaydet
with open("/test_files/testcoordinates.txt", "w") as f:
    for i in range(0, len(coords), 2):
        x1, y1 = coords[i]
        x2, y2 = coords[i+1]
        f.write(f"{x1},{y1},{x2},{y2}\n")

print("✅ Koordinatlar kaydedildi.")
