import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class AdvertisementManager:
    def __init__(self):
        self.css_content = ""
        self.html_content = ""
        self.images = []

    def add_advertisement(self, link, img_path, alt_text):
        self.images.append((link, img_path, alt_text))

    def delete_advertisement(self, index):
        if 0 <= index < len(self.images):
            del self.images[index]

    def edit_advertisement(self, index, link, img_path, alt_text):
        if 0 <= index < len(self.images):
            self.images[index] = (link, img_path, alt_text)

    def load_css(self):
        css_path = filedialog.askopenfilename(filetypes=[("CSS Files", "*.css")])
        if css_path:
            with open(css_path, "r") as css_file:
                self.css_content = css_file.read()

    def load_html(self):
        html_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
        if html_path:
            with open(html_path, "r") as html_file:
                self.html_content = html_file.read()

    def update_files(self):
        with open("style.css", "w") as css_file:
            css_file.write(self.css_content)

        updated_html = self.html_content
        for i, (link, img_path, alt_text) in enumerate(self.images, start=1):
            img_tag = f'<a href="{link}" target="_blank"><img src="{img_path}" alt="{alt_text}"></a>'
            updated_html = updated_html.replace(f'<!-- Image {i} -->', img_tag)

        with open("advertisement.html", "w") as html_file:
            html_file.write(updated_html)

class ImageManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionnaire d'Images")
        self.root.geometry("800x600")

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 12), padding=10)

        self.images_manager = AdvertisementManager()

        self.preview_label = tk.Label(self.frame, text="Aperçu des images")
        self.preview_label.grid(row=0, column=0, columnspan=3)

        self.canvas = tk.Canvas(self.frame, width=600, height=300)
        self.canvas.grid(row=1, column=0, columnspan=3)

        self.add_button = ttk.Button(self.frame, text="Ajouter une image", command=self.add_image)
        self.add_button.grid(row=2, column=0, padx=10, pady=10)

        self.remove_button = ttk.Button(self.frame, text="Supprimer une image", command=self.remove_image)
        self.remove_button.grid(row=2, column=1, padx=10, pady=10)

        self.replace_button = ttk.Button(self.frame, text="Remplacer une image", command=self.replace_image)
        self.replace_button.grid(row=2, column=2, padx=10, pady=10)

        self.load_css_button = ttk.Button(self.frame, text="Charger style.css", command=self.load_css)
        self.load_css_button.grid(row=3, column=0, padx=10, pady=10)

        self.load_html_button = ttk.Button(self.frame, text="Charger advertisement.html", command=self.load_html)
        self.load_html_button.grid(row=3, column=1, padx=10, pady=10)

        self.update_button = ttk.Button(self.frame, text="Mettre à jour les fichiers", command=self.update_files)
        self.update_button.grid(row=3, column=2, padx=10, pady=10)

        self.load_css()
        self.load_html()
        self.update_preview()

    def add_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if image_path:
            self.images_manager.add_advertisement("https://gpmailbox.github.io/", image_path, f"Image {len(self.images_manager.images)}")
            messagebox.showinfo("Information", f"Image ajoutée : {image_path}")
            self.update_preview()

    def remove_image(self):
        index = self.get_selected_index()
        if index is not None:
            self.images_manager.delete_advertisement(index)
            self.update_preview()

    def replace_image(self):
        index = self.get_selected_index()
        if index is not None:
            new_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
            if new_image_path:
                self.images_manager.edit_advertisement(index, "https://gpmailbox.github.io/", new_image_path, f"Image {index + 1}")
                messagebox.showinfo("Information", f"Image remplacée : {new_image_path}")
                self.update_preview()

    def get_selected_index(self):
        selection = self.canvas.find_withtag("current")
        if selection:
            return int(self.canvas.gettags(selection[0])[0]) - 1
        return None

    def load_css(self):
        self.images_manager.load_css()
        messagebox.showinfo("Information", f"style.css chargé")

    def load_html(self):
        self.images_manager.load_html()
        messagebox.showinfo("Information", f"advertisement.html chargé")

    def update_preview(self):
        self.canvas.delete("all")
        x, y = 10, 10
        for i, (link, img_path, alt_text) in enumerate(self.images_manager.images, start=1):
            image = tk.PhotoImage(file=img_path)
            self.canvas.create_image(x, y, anchor=tk.NW, image=image)
            self.canvas.addtag_withtag(str(i))
            x += 120

    def update_files(self):
        self.images_manager.update_files()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageManagerApp(root)
    root.mainloop()
