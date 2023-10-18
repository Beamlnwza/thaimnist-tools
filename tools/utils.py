def path_range(path, range: tuple):
    """
    Returns a list of paths for a given range of numbers.
    """
    return [path.format(str(i).zfill(3)) for i in range]


if __name__ == "__main__":
    for i in path_range("./preprocess_data/{}.png", range(1, 11)):
        print(i)
