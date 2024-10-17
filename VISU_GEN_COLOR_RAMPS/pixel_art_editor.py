# Pixel Art Color Ramps Viewer & Generator for 320x200 16 colors Pictures
# by Hylst v0.3 2024

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import colorsys
import random
import struct

class PixelArtEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Pixel Art Color Ramps Viewer & Generator for 320x200 16 colors Pictures")
        self.setup_ui()

    def setup_ui(self):
        # Buttons
        self.load_button = tk.Button(self.master, text="Load", command=self.load_image)
        self.load_button.grid(row=0, column=0, sticky="nw", padx=5, pady=5)

        self.save_button = tk.Button(self.master, text="Save", command=self.save_image)
        self.save_button.grid(row=0, column=4, sticky="ne", padx=5, pady=5)

        # File info
        self.file_info = tk.Text(self.master, height=3, width=50)
        self.file_info.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

        # Image canvases
        self.source_canvas = tk.Canvas(self.master, width=320, height=200)
        self.source_canvas.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.modified_canvas = tk.Canvas(self.master, width=320, height=200)
        self.modified_canvas.grid(row=2, column=3, columnspan=2, padx=5, pady=5)

        # Color palettes
        self.source_palette = tk.Frame(self.master)
        self.source_palette.grid(row=2, column=2, padx=5, pady=5)

        self.modified_palette = tk.Frame(self.master)
        self.modified_palette.grid(row=2, column=3, padx=5, pady=5)

        # Color editor
        self.color_editor = tk.Frame(self.master)
        self.color_editor.grid(row=3, column=0, columnspan=5, padx=5, pady=5)

        self.r_slider = tk.Scale(self.color_editor, from_=0, to=15, orient=tk.HORIZONTAL, label="R")
        self.r_slider.grid(row=0, column=0)
        self.g_slider = tk.Scale(self.color_editor, from_=0, to=15, orient=tk.HORIZONTAL, label="G")
        self.g_slider.grid(row=0, column=1)
        self.b_slider = tk.Scale(self.color_editor, from_=0, to=15, orient=tk.HORIZONTAL, label="B")
        self.b_slider.grid(row=0, column=2)

        self.h_slider = tk.Scale(self.color_editor, from_=0, to=359, orient=tk.HORIZONTAL, label="H")
        self.h_slider.grid(row=1, column=0)
        self.s_slider = tk.Scale(self.color_editor, from_=0, to=100, orient=tk.HORIZONTAL, label="S")
        self.s_slider.grid(row=1, column=1)
        self.v_slider = tk.Scale(self.color_editor, from_=0, to=100, orient=tk.HORIZONTAL, label="V")
        self.v_slider.grid(row=1, column=2)

        # Ramp generator
        self.ramp_generator = tk.Frame(self.master)
        self.ramp_generator.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

        tk.Button(self.ramp_generator, text="Auto", command=self.generate_auto_ramp).grid(row=0, column=0)
        tk.Button(self.ramp_generator, text="Semi-Auto", command=self.generate_semi_auto_ramp).grid(row=0, column=1)
        tk.Button(self.ramp_generator, text="Random", command=self.generate_random_ramp).grid(row=0, column=2)

        # Ramp display
        self.ramp_display = tk.Canvas(self.master, width=320, height=100)
        self.ramp_display.grid(row=5, column=0, columnspan=5, padx=5, pady=5)

        # Ajout d'un bouton pour sauvegarder les rampes
        tk.Button(self.ramp_generator, text="Save Ramps", command=self.save_ramps).grid(row=0, column=3)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("PI1 files", "*.pi1")])
        if file_path:
            self.image = Image.open(file_path)
            if self.image.mode != 'P':
                self.image = self.image.convert('P', palette=Image.ADAPTIVE, colors=16)
            
            self.update_file_info(file_path)
            self.update_canvases()
            self.update_palettes()

    def load_pi1(self, file_path):
        with open(file_path, 'rb') as f:
            # Lire l'en-tête PI1
            header = f.read(4)
            if header != b'PI1 ':
                raise ValueError("Invalid PI1 file")
            
            # Lire la palette
            palette = []
            for _ in range(16):
                color = struct.unpack('>H', f.read(2))[0]
                r = ((color >> 8) & 0x7) * 36
                g = ((color >> 4) & 0x7) * 36
                b = (color & 0x7) * 36
                palette.extend([r, g, b])
            
            # Lire les données de l'image
            image_data = f.read()
        
        # Créer une image PIL à partir des données
        image = Image.frombytes('P', (320, 200), image_data)
        image.putpalette(palette)
        
        return image

    def update_file_info(self, file_path):
        info = f"File: {file_path}\n"
        info += f"Format: {self.image.format}\n"
        info += f"Size: {self.image.size[0]}x{self.image.size[1]}\n"
        self.file_info.delete('1.0', tk.END)
        self.file_info.insert(tk.END, info)

    def update_canvases(self):
        self.source_image = ImageTk.PhotoImage(self.image)
        self.source_canvas.create_image(0, 0, anchor="nw", image=self.source_image)
        
        self.modified_image = ImageTk.PhotoImage(self.image)
        self.modified_canvas.create_image(0, 0, anchor="nw", image=self.modified_image)

    def update_palettes(self):
        palette = self.image.getpalette()
        for i in range(16):
            color = f'#{palette[i*3]:02x}{palette[i*3+1]:02x}{palette[i*3+2]:02x}'
            
            tk.Button(self.source_palette, bg=color, width=2, height=1).grid(row=i, column=0)
            
            button = tk.Button(self.modified_palette, bg=color, width=2, height=1)
            button.grid(row=i, column=0)
            button.bind('<Button-1>', lambda e, idx=i: self.edit_color(idx))

    def edit_color(self, index):
        r, g, b = self.image.getpalette()[index*3:index*3+3]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        self.r_slider.set(r//16)
        self.g_slider.set(g//16)
        self.b_slider.set(b//16)
        self.h_slider.set(int(h*359))
        self.s_slider.set(int(s*100))
        self.v_slider.set(int(v*100))
        
        self.current_color_index = index
        
        for slider in [self.r_slider, self.g_slider, self.b_slider, self.h_slider, self.s_slider, self.v_slider]:
            slider.config(command=self.update_color)

    def update_color(self, _):
        if hasattr(self, 'current_color_index'):
            if self.master.focus_get() in [self.r_slider, self.g_slider, self.b_slider]:
                r = self.r_slider.get() * 16
                g = self.g_slider.get() * 16
                b = self.b_slider.get() * 16
            else:
                h = self.h_slider.get() / 359
                s = self.s_slider.get() / 100
                v = self.v_slider.get() / 100
                r, g, b = [int(x * 255) for x in colorsys.hsv_to_rgb(h, s, v)]
                self.r_slider.set(r//16)
                self.g_slider.set(g//16)
                self.b_slider.set(b//16)
            
            palette = self.image.getpalette()
            palette[self.current_color_index*3:self.current_color_index*3+3] = [r, g, b]
            self.image.putpalette(palette)
            
            self.update_canvases()
            self.update_palettes()

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("PI1 files", "*.pi1")])
        if file_path:
            self.image.save(file_path)

    def save_pi1(self, file_path):
        with open(file_path, 'wb') as f:
            # Écrire l'en-tête PI1
            f.write(b'PI1 ')
            
            # Écrire la palette
            palette = self.image.getpalette()
            for i in range(0, 48, 3):
                r, g, b = palette[i:i+3]
                color = ((r // 36) << 8) | ((g // 36) << 4) | (b // 36)
                f.write(struct.pack('>H', color))
            
            # Écrire les données de l'image
            f.write(self.image.tobytes())        

    def generate_auto_ramp(self):
        palette = self.image.getpalette()
        colors = [tuple(palette[i:i+3]) for i in range(0, 48, 3)]
        
        # Trier les couleurs par luminosité
        sorted_colors = sorted(colors, key=lambda c: sum(c))
        
        # Créer 3 rampes de 5 couleurs
        ramps = [sorted_colors[i:i+5] for i in range(0, 15, 5)]
        
        self.display_ramps(ramps)


    def generate_semi_auto_ramp(self):
        palette = self.image.getpalette()
        colors = [tuple(palette[i:i+3]) for i in range(0, 48, 3)]
        
        # Trier les couleurs par teinte
        sorted_colors = sorted(colors, key=lambda c: colorsys.rgb_to_hsv(*[x/255 for x in c])[0])
        
        # Créer 3 rampes de 5 couleurs
        ramps = [sorted_colors[i:i+5] for i in range(0, 15, 5)]
        
        self.display_ramps(ramps)

    def generate_random_ramp(self):
        palette = self.image.getpalette()
        colors = [tuple(palette[i:i+3]) for i in range(0, 48, 3)]
        
        # Créer 3 rampes aléatoires de 5 couleurs
        ramps = [random.sample(colors, 5) for _ in range(3)]
        
        self.display_ramps(ramps)

    def display_ramps(self, ramps):
        self.ramp_display.delete("all")
        
        for i, ramp in enumerate(ramps):
            for j, color in enumerate(ramp):
                x = j * 30
                y = i * 30
                self.ramp_display.create_rectangle(x, y, x+30, y+30, fill='#%02x%02x%02x' % color, outline='')
        
        self.ramps = ramps

    def save_ramps(self):
        if not hasattr(self, 'ramps'):
            messagebox.showwarning("Warning", "No ramps to save")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            ramp_image = Image.new('RGB', (150, 90))
            draw = ImageDraw.Draw(ramp_image)
            
            for i, ramp in enumerate(self.ramps):
                for j, color in enumerate(ramp):
                    x = j * 30
                    y = i * 30
                    draw.rectangle([x, y, x+30, y+30], fill=color)
            
            ramp_image.save(file_path)

root = tk.Tk()
app = PixelArtEditor(root)
root.mainloop()