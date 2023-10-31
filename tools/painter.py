import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageEnhance, ImageOps
import PIL.ImageOps
import os

accpet = 0
decline = 0


class ImagePainter:
    def __init__(self, master, image_path, output_path):
        self.master = master
        self.master.title(f"accpeted : {accpet}, denied : {decline} - {image_path}")
        self.brush_size = 40

        self.brightness = 1.0
        self.contrast = 2.0
        self.threshold = 225

        self.zoom_percentage = 350

        self.image = self.load_and_process_image(image_path)

        self.output_path = output_path

        self.setup_canvas()

    def load_and_process_image(self, image_path):
        image = Image.open(image_path)
        image = image.convert("L")
        image = ImageEnhance.Brightness(image).enhance(self.brightness)
        image = ImageEnhance.Contrast(image).enhance(self.contrast)
        image = image.point(lambda p: 255 if p > self.threshold else 0)

        image = image.convert("1")
        image = PIL.ImageOps.invert(image)
        image = image.resize(
            (
                int(image.width * self.zoom_percentage / 100),
                int(image.height * self.zoom_percentage / 100),
            )
        )
        return image

    def setup_canvas(self):
        self.canvas = tk.Canvas(
            self.master, width=self.image.width, height=self.image.height
        )
        self.canvas.pack()

        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        self.canvas.bind("<Motion>", self.paint)
        self.master.bind("<Button-1>", self.save)
        # right click to deny
        self.master.bind("<Button-3>", self.deny)

    def paint(self, event):
        x, y = event.x, event.y
        r = self.brush_size
        draw = ImageDraw.Draw(self.image)
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def save(self, event):
        # Your existing code...
        if not os.path.exists(os.path.dirname(self.output_path)):
            os.makedirs(os.path.dirname(self.output_path))
        self.image = self.image.resize(
            (
                int(self.image.width * 100 / self.zoom_percentage),
                int(self.image.height * 100 / self.zoom_percentage),
            )
        )
        self.image = self.image.convert("L")
        self.image = self.image.point(lambda p: 0 if p < self.threshold else 255)
        self.image.save(self.output_path)
        print("Saved to {}".format(self.output_path))

        global accpet
        accpet += 1

        self.master.destroy()

    def make_white_to_black(self, image):
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

    def deny(self, event):
        global decline
        decline += 1
        self.master.destroy()


if __name__ == "__main__":
    main_path = "./box_data/22"
    main_output_path = f"./uncenter_data/{main_path[-2:]}"

    for i in sorted(os.listdir(main_path)):
        path = os.path.join(main_path, i)
        output_path = os.path.join(main_output_path, i)
        root = tk.Tk()
        root.state("zoomed")

        image_painter = ImagePainter(root, path, output_path)
        root.mainloop()

    # command to handle for in list [number, number...]

    """ for i in [221]:
        i = str(i).zfill(3)
        path = os.path.join(main_path, f"{i}.jpg")
        output_path = os.path.join(main_output_path, f"{i}.jpg")
        root = tk.Tk()

        root.state("zoomed")

        image_painter = ImagePainter(root, path, output_path)
        root.mainloop() """
