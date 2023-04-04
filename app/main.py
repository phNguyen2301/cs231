import customtkinter as ctk
from image_widgets import *
from PIL import Image, ImageTk, ImageOps
from menu import Menu


class App(ctk.CTk):
    def __init__(self):
        # setup
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('800x500')
        self.title('Photo Editor')
        self.minsize(800, 500)
        self.init_parameter()

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        # canvas
        self.image_width = 0
        self.image_height = 0
        self.canvas_height = 0
        self.canvas_width = 0

        # widget
        self.image_import = ImageImport(self, self.import_image)

        # run
        self.mainloop()

    def init_parameter(self):
        self.pos_vars = {
            'rotation': ctk.DoubleVar(value=ROTATION_DEFALT),
            'zoom': ctk.DoubleVar(value=ZOOM_DEFAULT),
            'flip': ctk.StringVar(value=FLIP_OPTIONS[0])
        }

        self.color_vars = {
            'brightness': ctk.DoubleVar(value=BRIGHTNESS_DEFAULT),
            'grayscale': ctk.BooleanVar(value=GRAYSCALE_DEFAULT),
            'invert': ctk.BooleanVar(value=INVERT_DEFAULT),
            'vibrance': ctk.BooleanVar(value=VIBRANCE_DEFAULT)
        }

        self.effect_vars = {
            'blur': ctk.DoubleVar(value=BLUR_DEFAULT),
            'contrast': ctk.IntVar()(value=CONTRAST_DEFAULT),
            'effect': ctk.StringVar()(value=EFFECT_OPTIONS[0])
        }
        combined_vars = list(self.pos_vars.values(
        )) + list(self.color_vars.values()) + list(self.effect_vars.values())
        for var in combined_vars:
            var.trace('w', self.edit_image)

    def import_image(self, path):
        self.original = Image.open(path)
        self.image = self.original
        self.image_ratio = self.image.size[0]/self.image.size[1]

        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.menu = Menu(self, self.pos_vars,
                         self.color_vars, self.effect_vars)

    def close_edit(self):
        self.menu.grid_forget()
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.image_import = ImageImport(self, self.import_image)

    def resize_image(self, event):
        # canvas
        self.canvas_height = event.height
        self.canvas_width = event.width
        canvas_ratio = event.width/event.height

        # resize
        if canvas_ratio > self.image_ratio:
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * self.image_ratio)
        else:
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / self.image_ratio)
        self.place_image()

    def place_image(self):
        self.image_output.delete('all')
        resized_image = self.image.resize(
            (self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(
            self.canvas_width/2, self.canvas_height/2, image=self.image_tk)

    def edit_image(self, *args):
        self.image = self.original

        # rotate
        self.image = self.image.rotate(self.pos_vars['rotation'].get())

        # zoom
        self.image = ImageOps.crop(
            image=self.image, border=self.pos_vars['zoom'].get())

        self.place_image()


App()
