import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageEnhance, ImageFilter, ImageOps
import PIL.ImageOps
import os


class ImagePainter:
    def __init__(self, master, image_path, output_path):
        self.master = master

        threshold = 230

        self.image = Image.open(image_path)

        self.image = ImageEnhance.Brightness(self.image).enhance(0.962)
        self.image = ImageEnhance.Contrast(self.image).enhance(0.5)

        self.image = self.image.convert("L")
        self.image = self.image.point(lambda p: 255 if p > threshold else 0)
        self.image = self.image.convert("1")

        self.image = PIL.ImageOps.invert(self.image)

        self.zoom_percentage = 350

        self.image = self.image.resize(
            (
                int(self.image.width * self.zoom_percentage / 100),
                int(self.image.height * self.zoom_percentage / 100),
            )
        )

        self.output_path = output_path

        self.canvas = tk.Canvas(
            master, width=self.image.width, height=self.image.height
        )
        self.canvas.pack()

        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        self.canvas.bind("<Motion>", self.paint)

        self.master.bind("<Return>", self.save)

    def paint(self, event):
        x, y = event.x, event.y
        r = 30
        draw = ImageDraw.Draw(self.image)
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def save(self, event):
        # resize back

        self.image = self.image.resize(
            (
                int(self.image.width * 100 / self.zoom_percentage),
                int(self.image.height * 100 / self.zoom_percentage),
            )
        )

        self.image = make_white_to_black(self.image)
        self.image = self.image.convert("1")
        self.image.save(self.output_path)
        print("Saved to {}".format(self.output_path))
        self.master.destroy()


def make_white_to_black(image):
    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            if pixel == (255, 255, 255):
                neighbors = []

                if x > 0:
                    neighbors.append(image.getpixel((x - 1, y)))
                if x < width - 1:
                    neighbors.append(image.getpixel((x + 1, y)))
                if y > 0:
                    neighbors.append(image.getpixel((x, y - 1)))
                if y < height - 1:
                    neighbors.append(image.getpixel((x, y + 1)))
                if all(n != (255, 255, 255) for n in neighbors):
                    image.putpixel((x, y), (0, 0, 0))

    return image


if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    image_path = "./box_data/00/067.jpg"
    output_path = "001.jpg"

    image_painter = ImagePainter(root, image_path, output_path)
    root.mainloop()

    """ main_path = "./box_data/04"
    main_output_path = f"./uncenter_data/{main_path[-2:]}"
    for i in sorted(os.listdir(main_path)):
        path = os.path.join(main_path, i)
        output_path = os.path.join(main_output_path, i)
        root = tk.Tk()

        root.state("zoomed")

        image_painter = ImagePainter(root, path, output_path)
        root.mainloop() """
