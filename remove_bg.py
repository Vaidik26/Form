from PIL import Image
import numpy as np
import os

def process_logo(input_path, output_path):
    print(f"Processing {input_path}...")
    img = Image.open(input_path).convert("RGBA")
    data = np.array(img)
    
    r = data[..., 0].astype(np.float32)
    g = data[..., 1].astype(np.float32)
    b = data[..., 2].astype(np.float32)
    
    grayscale = (r * 0.299 + g * 0.587 + b * 0.114)
    
    # Map grayscale to an alpha channel
    # Values above 200 (light background) becomes 0
    # Values below 120 (dark logo text) becomes 255
    alpha = np.interp(grayscale, [120, 220], [255, 0])
    
    # To fix white fringes, we replace ALL RGB pixels with the solid logo color
    # Logo color is roughly #183e20 -> (24, 62, 32)
    data[..., 0] = 24
    data[..., 1] = 62
    data[..., 2] = 32
    data[..., 3] = alpha.astype(np.uint8)
    
    Image.fromarray(data).save(output_path)
    print(f"Saved transparent logo to {output_path}")

input_img = "c:/Job Workspace/Form/static/images/logo.jpeg"
output_img = "c:/Job Workspace/Form/static/images/logo_transparent.png"
process_logo(input_img, output_img)
