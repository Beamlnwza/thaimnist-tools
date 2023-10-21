import os
from PIL import Image
from tqdm import tqdm


def box_cropper(path):
    init_1 = (2, 2)
    init_2 = (24, 24)
    ledder = -1
    for i in range(0, 54):
        img = Image.open(path)

        if i % 9 == 0:
            ledder += 1

        pos1_x, pos1_y, pos2_x, pos2_y = init_1[0], init_1[1], init_2[0], init_2[1]

        if i != 0:
            pos1_x = pos1_x + (62 * (i % 9))
            pos1_y = pos1_y + (76 * ledder)
            pos2_x = pos2_x + (62 * (i % 9))
            pos2_y = pos2_y + (76 * ledder)

        img_cropped = img.resize((522, 408))
        img_cropped = img_cropped.crop((pos1_x, pos1_y, pos2_x, pos2_y))
        img_cropped = img_cropped.resize((128, 128))
        save_path = "./box_data/" + str(i).zfill(2) + "/"
        img_cropped.save(save_path + str(item_inside(save_path)).zfill(3) + ".jpg")


def item_inside(path):
    return len(os.listdir(path))


if __name__ == "__main__":
    for i in tqdm(range(1, 301)):
        path = "./area_data/" + str(i).zfill(3) + ".jpg"
        box_cropper(path)
