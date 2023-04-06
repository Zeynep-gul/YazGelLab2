import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import random


class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Viewer")

        # GUI tasarımları
        self.image_label = tk.Label(self.master)
        self.select_button = tk.Button(self.master, text="Select Photo", command=self.select_photo)
        self.score_label = tk.Label(self.master, text="SCORE:")
        self.mix_button = tk.Button(self.master, text="KARIŞTIR", command=self.mix_pieces)
        self.grid_layout = tk.Frame(self.master)

        # düzenleme
        self.image_label.grid(row=0, column=0, columnspan=4)
        self.select_button.grid(row=1, column=0)
        self.score_label.grid(row=1, column=1)
        self.mix_button.grid(row=1, column=2)
        self.grid_layout.grid(row=2, column=0, columnspan=4)

        # butonlar için bağlı liste oluştur
        self.piece_list = [i for i in range(16)]

    def select_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.bmp")])
        if file_path:
            self.display_photo(file_path)

    def display_photo(self, file_path):
        # resim yükle, görüntüle
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

        # Resmi 16 parçaya böl
        piece_width = image.width // 4
        piece_height = image.height // 4

        # önceki düğmeleri temizle
        for widget in self.grid_layout.winfo_children():
            widget.destroy()

        # resmi sırayla parça parça butonlara böl
        self.buttons = []
        for i in range(16):
            row, col = divmod(i, 4)
            left = col * piece_width
            top = row * piece_height
            right = (col + 1) * piece_width
            bottom = (row + 1) * piece_height
            piece = image.crop((left, top, right, bottom))
            piece_photo = ImageTk.PhotoImage(piece)
            piece_button = tk.Button(self.grid_layout, image=piece_photo)
            piece_button.image = piece_photo
            piece_button.grid(row=row, column=col)
            self.buttons.append(piece_button)

        # parçaların orijinal sırasını takip et
        self.piece_list = list(range(16))

    def mix_pieces(self):
        # Parça listesini karıştır
        random.shuffle(self.piece_list)
        # Düğmeleri yeni konumlarla yeniden çiz
        for i in range(16):
            row, col = divmod(self.piece_list[i], 4)
            self.buttons[i].grid(row=row, column=col)



    # def move_piece(self, index):
    #
    #
    # def is_adjacent(self, index1, index2):
    #     İki parçalı indekslerin bitişik olup olmadığını kontrol et
    #    return abs(index1 - index2) == 1 or abs(index1 - index2) == 4
    #


if __name__ == '__main__':
    root = tk.Tk()
    viewer = ImageViewer(root)
    root.mainloop()




