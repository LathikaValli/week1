import os
from matplotlib import pyplot as plt
import cv2

# Update this to your actual path
dataset_path = r"C:\Users\Lathika\OneDrive\Desktop\E_Waste_Project\archive\underwater_plastics"

for split in ["train", "valid", "test"]:
    split_path = os.path.join(dataset_path, split, "images")
    
    if not os.path.exists(split_path):
        print(f"Path does not exist: {split_path}")
        continue
    
    num_images = len([f for f in os.listdir(split_path) if f.endswith(".jpg") or f.endswith(".png")])
    print(f"{split} has {num_images} images")

    # Display first image
    img_files = [f for f in os.listdir(split_path) if f.endswith(".jpg") or f.endswith(".png")]
    if img_files:
        img = cv2.imread(os.path.join(split_path, img_files[0]))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.title(f"{split} sample image")
        plt.show()

