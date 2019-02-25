import os
import base64

# pip install pillow ( the new PIL )
from PIL import Image


class ImageConverter:
    def __init__(self):
        self.image_default_path = os.getcwd() + "\images" + "\default_img_user.png"
        self.image_user_path = os.getcwd() + "\images" + "\image_user.png"

    def convert_bytes_to_img(self, bytes_string):
        bytes_string = base64.b64decode(bytes_string)
        with open(self.image_user_path, "wb") as f:
            f.write(bytes_string)

    def resize_img_resolution(self, image_path=None):
        try:
            image = Image.open(image_path)
            image.save(self.image_user_path, dpi=(1600, 1024))
            return True

        except OSError:
            return False

    def convert_img_to_bytes_(self):
        # Convert for the new image of current user
        with open(self.image_user_path, "rb") as image_file:
            image_bytes = base64.b64encode(image_file.read())

        return image_bytes

    @staticmethod
    def convert_img_to_bytes(image_path):

        with open(image_path, "rb") as image_file:
            image_bytes = base64.b64encode(image_file.read())

        return image_bytes

