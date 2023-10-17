from PIL import Image
import os


def split_image(image_path, output_dir):
    """
    Splits an image into left and right halves and saves them as separate files.

    Args:
    - image_path (str): The path to the image file to be split.

    Returns:
    - None
    """
    original_image = Image.open(image_path)

    original_image = original_image.transpose(Image.ROTATE_90)

    width, height = original_image.size

    left_half = original_image.crop((0, 0, width // 2, height))

    right_half = original_image.crop((width // 2, 0, width, height))

    if len(os.listdir(output_dir)) == 0:
        left_half.save(f"{output_dir}/1.jpg")
        right_half.save(f"{output_dir}/2.jpg")
    else:
        left_half.save(
            f"{output_dir}/{str(len(os.listdir(output_dir)) + 1).zfill(3)}.jpg"
        )
        right_half.save(
            f"{output_dir}/{str(len(os.listdir(output_dir)) + 1).zfill(3)}.jpg"
        )


if __name__ == "__main__":
    for i in sorted(os.listdir("./form_data")):
        split_image(f"./form_data/{i}", "./preprocess_data")
