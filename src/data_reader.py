import os
import numpy as np
import PIL
from PIL import Image

IMAGE_NAMES = [
        "{}_green.png",
        "{}_red.png",
        "{}_blue.png",
        "{}_yellow.png"
        ]

def read_image(img_id, data_path):
    """
    img_id: (str) id of the image to unpack
    data_path: (str) directory where to find the images

    return 4-channel image from data_path/image_id.png
    """
    paths = [
            os.path.join(data_path, img_name.format(img_id)) for img_name in IMAGE_NAMES
            ]
    assert all(os.path.isfile(path) for path in paths)

    imgs = [np.array(PIL.Image.open(path)) for path in paths]
    return np.stack(imgs, axis=-1)
