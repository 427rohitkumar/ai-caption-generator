import cv2, os

def extract_frames(video_path, out="app/outputs/frames"):
    os.makedirs(out, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frames = []
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % fps == 0:
            path = f"{out}/frame_{count}.jpg"
            cv2.imwrite(path, frame)
            frames.append(path)

        count += 1

    cap.release()
    return frames