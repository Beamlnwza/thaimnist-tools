from PIL import Image
import os
from tqdm import tqdm


def black_pixel_bounds(image_path, output_folder):
    image = Image.open(image_path)

    width, height = image.size

    left, top, right, bottom = None, None, None, None

    for x in range(width):
        for y in range(height):
            pixel_value = image.getpixel((x, y))

            if pixel_value == 255:
                if left is None or x < left:
                    left = x
                if right is None or x > right:
                    right = x
                if top is None or y < top:
                    top = y
                if bottom is None or y > bottom:
                    bottom = y

    image = image.crop((left, top, right, bottom))
    image.save(output_folder + "/" + image_path.split("/")[-1])


if __name__ == "__main__":
    for i in tqdm(os.listdir("./uncenter_data")):
        for j in tqdm(os.listdir(f"./uncenter_data/{i}")):
            try:
                black_pixel_bounds(f"./uncenter_data/{i}/{j}", f"./ROI_data/{i}")
            except:
                print(f"./uncenter_data/{i}/{j}")
                continue
