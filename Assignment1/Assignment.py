import cv2
import numpy as np

def process_face(image_path, start_x, start_y, stride):
    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        return None
        
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    face_array = np.zeros((3, 3, 3), dtype=np.uint8)

    for row in range(3):
        for col in range(3):
            target_x = start_x + (col * stride)
            target_y = start_y + (row * stride)

            patch = img_hsv[target_y-5:target_y+5, target_x-5:target_x+5]
            mean_hsv = np.mean(patch, axis=(0, 1))
            face_array[row, col] = mean_hsv.astype(np.uint8)

    return face_array

def build_cube_database(image_paths, tracking_configs):
    cube_data = np.zeros((6, 3, 3, 3), dtype=np.uint8)

    for face_idx in range(6):
        config = tracking_configs[face_idx]
        face_matrix = process_face(
            image_paths[face_idx],
            config['start_x'],
            config['start_y'],
            config['stride']
        )
        if face_matrix is not None:
            cube_data[face_idx] = face_matrix

    return cube_data

if __name__ == "__main__":
    images = ["Top.png", "Bottom.png", "Front.png", "Back.png", "Left.png", "Righ.png"]
    configs = [
        {"start_x": 100, "start_y": 100, "stride": 50},
        {"start_x": 100, "start_y": 100, "stride": 50},
        {"start_x": 100, "start_y": 100, "stride": 50},
        {"start_x": 100, "start_y": 100, "stride": 50},
        {"start_x": 100, "start_y": 100, "stride": 50},
        {"start_x": 100, "start_y": 100, "stride": 50}
    ]

    print("Processing images...")
    
    cube_database = build_cube_database(images, configs)
    
    print("Database built successfully! Matrix shape:", cube_database.shape)
    
print("Top-Left Sticker [H, S, V] on UP Face:", cube_database[0][0][0])