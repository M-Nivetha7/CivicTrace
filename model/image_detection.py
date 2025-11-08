import cv2
import os
import numpy as np

def check_image_in_database(upload_path, db_path):
    uploaded_img = cv2.imread(upload_path)

    if uploaded_img is None:
        return "⚠️ Invalid image uploaded"

    for file in os.listdir(db_path):
        file_path = os.path.join(db_path, file)
        db_img = cv2.imread(file_path)

        if db_img is None:
            continue

        # Resize both to same size
        try:
            resized_db_img = cv2.resize(db_img, (uploaded_img.shape[1], uploaded_img.shape[0]))
        except:
            continue

        # Compare pixel difference
        diff = cv2.absdiff(uploaded_img, resized_db_img)
        similarity = 1 - (np.sum(diff) / (uploaded_img.size * 255))

        if similarity > 0.98:  # 98% match threshold
            return f"✅ Image Found in Database ({file})"

    return "❌ Image Not Found in Database"
