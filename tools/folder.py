import os


def create_folder_index(range, folder_name):
    for i in range:
        os.mkdir(os.path.join(folder_name, str(i).zfill(2)))


if __name__ == "__main__":
    create_folder_index(range(0, 54), "./box_data")
