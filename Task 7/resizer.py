import os
from PIL import Image

# Folder paths
input_folder = 'input_images'
output_folder = 'output_images'

# Resize dimensions
new_width = 800
new_height = 600

# Output folder create karle agar nahi hai
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Har image par loop chalaye
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.webp')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize kare
        resized_img = img.resize((new_width, new_height))

        # Save kare
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path)

        print(f"Resized and saved: {filename}")