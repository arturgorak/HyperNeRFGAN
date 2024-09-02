from PIL import Image


def count_channels(path):
    obraz = Image.open(path)
    channels = obraz.mode
    return channels


if __name == '__main':
    path = "0.png"
    channels = count_channels(path)
    print(channels)
