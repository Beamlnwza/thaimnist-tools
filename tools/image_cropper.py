import tkinter as tk
from PIL import Image, ImageTk
import os
from utils import path_range


class ImageCropperApp:
    def __init__(self, master, image_path, output_path):
        self.master = master
        self.master.title("Image Cropper")

        self.image_path = image_path
        self.output_path = output_path

        self.image = Image.open(image_path)
        self.zoom_percentage = 50

        self.image = self.image.resize(
            (
                int(self.image.width * self.zoom_percentage / 100),
                int(self.image.height * self.zoom_percentage / 100),
            )
        )

        self.canvas = tk.Canvas(
            master, width=self.image.width, height=self.image.height
        )
        self.canvas.pack()

        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

        self.rect = None
        self.start_x = None
        self.start_y = None
        self.scale = 1

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.master.bind("<Return>", self.crop_image)

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if not self.rect:
            box_width = 300
            box_height = 100
            self.rect = self.canvas.create_rectangle(
                self.start_x,
                self.start_y,
                self.start_x + box_width,
                self.start_y + box_height,
                outline="red",
            )

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        if self.rect:
            self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        pass

    def crop_image(self, event):
        if self.rect:
            x0 = int(min(self.start_x, self.canvas.coords(self.rect)[2]))
            y0 = int(min(self.start_y, self.canvas.coords(self.rect)[3]))
            x1 = int(max(self.start_x, self.canvas.coords(self.rect)[2]))
            y1 = int(max(self.start_y, self.canvas.coords(self.rect)[3]))

            cropped_image = self.image.crop((x0, y0, x1, y1))
            save_path = os.path.join(
                self.output_path, os.path.basename(self.image_path)
            )
            cropped_image.save(save_path)
            print(f"Image saved at {save_path} : size: {cropped_image.size}")
            self.master.destroy()


if __name__ == "__main__":
    for i in path_range("./preprocess_data/{}.jpg", range(251, 301)):
        root = tk.Tk()
        root.state("zoomed")
        app = ImageCropperApp(root, i, "./area_data")
        root.mainloop()

# 1-11 done
# 11-21 done
# 21-31 done
# 31-41 done
# 41-51 done
# 51-61 done 56-57
# 61-71 done
# 71-81 done
# 81-91 done
# 91-101 done
# 101-111 done
# 111-121 done
# 121-131 done
# 131-141 done
# 141-151 done
# 151-161 done
# 161-171 done
# 171-181 done
# 181-191 done
# 191-201 done
# 201-211 done
# 211-221 done
# 221-231 done
# 231-241 done
# 241-251 done
# 251-261
# 261-271
# 271-281
# 281-291
# 291-301
