import cv2

capture = cv2.VideoCapture("source_video.MP4")
fps = capture.get(cv2.CAP_PROP_FPS)
count = 0

while True:
    ret, frame = capture.read()
    if not ret:
        break
    cv2.imwrite(f"calib_{count:02}.png", frame)
    count += 1