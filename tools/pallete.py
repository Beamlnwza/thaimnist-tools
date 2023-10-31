import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance, ImageOps
import os
import PIL


class ImageProcessor:
    def __init__(self, master, image_path):
        self.master = master
        self.master.title("Image Processor")
        self.master.geometry("600x600")

        self.brightness = 1.4
        self.contrast = 1.5
        self.threshold = 233

        self.unedited_image = Image.open(image_path)
        self.image = self.load_and_process_image(image_path)

        self.setup_canvas()
        self.setup_controls()

    def load_and_process_image(self, image_path):
        image = Image.open(image_path)
        image = ImageEnhance.Brightness(image).enhance(self.brightness)
        image = ImageEnhance.Contrast(image).enhance(self.contrast)
        image = image.point(lambda p: 255 if p > self.threshold else 0)
        image = PIL.ImageOps.invert(image)
        return image

    def setup_canvas(self):
        self.canvas = tk.Canvas(
            self.master, width=self.image.width, height=self.image.height
        )
        self.canvas.pack()

        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def setup_controls(self):
        self.brightness_scale = tk.Scale(
            self.master,
            from_=0.1,
            to=2,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            label="Brightness",
            command=lambda value: self.adjust_brightness(float(value)),
        )
        self.brightness_scale.set(self.brightness)
        self.brightness_scale.pack()

        self.contrast_scale = tk.Scale(
            self.master,
            from_=0.1,
            to=2,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            label="Contrast",
            command=lambda value: self.adjust_contrast(float(value)),
        )
        self.contrast_scale.set(self.contrast)
        self.contrast_scale.pack()

        self.threshold_scale = tk.Scale(
            self.master,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            label="Threshold",
            command=lambda value: self.adjust_threshold(int(value)),
        )
        self.threshold_scale.set(self.threshold)
        self.threshold_scale.pack()

    def adjust_brightness(self, value):
        self.brightness = value
        self.image = self.load_and_process_image(image_path)
        self.update_image()

    def adjust_contrast(self, value):
        self.contrast = value
        self.image = self.load_and_process_image(image_path)
        self.update_image()

    def adjust_threshold(self, value):
        self.threshold = value
        self.image = self.load_and_process_image(image_path)
        self.update_image()

    def update_image(self):
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)


if __name__ == "__main__":
    image_path = "./box_data/14/015.jpg"  # Replace with the path to your image
    root = tk.Tk()
    image_processor = ImageProcessor(root, image_path)
    root.mainloop()

    # 1.0 1.7 225
