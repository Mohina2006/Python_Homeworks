import numpy as np
from PIL import Image
import os

# Load Image
def load_image(path):
    image = Image.open(path)
    return np.array(image)

# Save Image
def save_image(np_img, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)  # Creates the folder if it doesn't exist
    img = Image.fromarray(np_img.astype('uint8'))
    img.save(path)

# Flip Image
def flip_image(np_img):
    flipped_h = np.fliplr(np_img)  # Horizontal flip
    flipped_v = np.flipud(np_img)  # Vertical flip
    return flipped_h, flipped_v

# Add random Noise
def add_noise(np_img, noise_level=25):
    noise = np.random.randint(-noise_level, noise_level + 1, np_img.shape, dtype="int16")
    noisy_img = np.clip(np_img.astype("int16") + noise, 0, 255).astype("uint8")
    return noisy_img

# Brighten channels
def brighten_channel(np_img, increase=40):
    bright_img = np.clip(np_img.astype("int16") + increase, 0, 255).astype("uint8")
    return bright_img

# Apply center Mask
def apply_mask(np_img, mask_size=100):
    h, w = np_img.shape[:2]
    start_y = (h - mask_size) // 2
    start_x = (w - mask_size) // 2
    np_img[start_y: start_y + mask_size, start_x: start_x + mask_size] = [0, 0, 0]
    return np_img

# Run the transformations
if __name__ == "__main__":
    # Load original image
    path = "C:/Users/user/Desktop/Python/Python_Homeworks/lesson-14/homework/birds.jpg"
    original = load_image(path)

    # 1. Flip horizontally and vertically
    flipped_h, flipped_v = flip_image(original)
    save_image(flipped_h, "images/birds_flipped_horizontal.jpg")
    save_image(flipped_v, "images/birds_flipped_vertical.jpg")

    # 2. Add noise
    noisy = add_noise(original)
    save_image(noisy, "images/birds_noisy.jpg")

    # 3. Brighten channels
    bright = brighten_channel(original)
    save_image(bright, "images/birds_bright.jpg")

    # 4. Apply central mask
    masked = apply_mask(original.copy())  # Avoid modifying the original
    save_image(masked, "images/birds_masked.jpg")
