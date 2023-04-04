import customtkinter as ctk
from panels import *


class Menu(ctk.CTkTabview):
    def __init__(self, parent, pos_vars, color_vars, effect_vars):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        # tabs
        self.add('Position')
        self.add('Color')
        self.add('Effect')
        self.add('Export')

        # widgets
        PositionFrame(self.tab('Position'), pos_vars)
        ColorFrame(self.tab('Color'), color_vars)
        EffectFrame(self.tab('Effect'), effect_vars)
        ExportFrame(self.tab('Export'))


class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        SliderPanel(self, 'Rotation', pos_vars['rotation'], 0, 360)
        SliderPanel(self, 'Zoom', pos_vars['zoom'], 1, 200)


class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent, color_vars):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        SliderPanel(self, 'Brightness', pos_vars['brightness'], 0, 5)
        SliderPanel(self, 'Vibrance', pos_vars['vibrance'], 0, 5)


class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent, effect_vars):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        SliderPanel(self, 'Blur', pos_vars['blur'], 0, 3)
        SliderPanel(self, 'Contrast', pos_vars['contrast'], 0, 10)


class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')
