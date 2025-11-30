import tkinter as tk
from tkinter import messagebox, ttk
from entry import WeatherEntry
from log import WeatherLog
from statistics import WeatherStatisticsTP
from PIL import Image, ImageTk

class WeatherAPP:
    def __init__(self, root):
        self.root = root
        self.root.title("Időjárás Napló")
        self.root.geometry("600x500")

        self.log = WeatherLog()


        img = Image.open("C:/Users/topol/Desktop/beadando1/logo1.png")
        img = img.resize((100, 100))
        tk_img = ImageTk.PhotoImage(img)
        lbl = tk.Label(root, image=tk_img)
        lbl.image = tk_img
        lbl.pack(pady=20)

        title = tk.Label(root, text="Időjárás Napló", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        btn_add = tk.Button(root, text="Új bejegyzés", width=25, command=self.new_entry_window)
        btn_show = tk.Button(root, text="Bejegyzések listázása", width=25, command=self.show_entries_window)
        btn_search = tk.Button(root, text="Keresés dátum szerint", width=25, command=self.search_window)
        btn_max = tk.Button(root, text="Legmagasabb hőmérséklet", width=25, command=self.show_maximum)
        btn_min = tk.Button(root, text="Legalacsonyabb hőmérséklet", width=25, command=self.show_minimum)
        btn_save = tk.Button(root, text="Mentés", width=10, command=self.save_to_fileTP, bg="grey")

        btn_add.pack(pady=10)
        btn_show.pack(pady=10)
        btn_search.pack(pady=10)
        btn_max.pack(pady=10)
        btn_min.pack(pady=10)
        btn_save.pack(pady=15)

    def save_to_fileTP(self):
        if not self.log.entries:
            messagebox.showinfo("Mentés", "Nincs mit elmenteni.")
            return

        try:
            with open("weather_log.txt", "w", encoding="utf-8") as file:
                for e in self.log.entries:
                    file.write(f"{e.date} | {e.min_temp}°C / {e.max_temp}°C")

            messagebox.showinfo("Mentés", "Sikeresen elmentve a weather_log.txt fájlba!")
        except Exception as ex:
            messagebox.showerror("Hiba", f"Nem sikerült menteni!\n{ex}")


    def new_entry_window(self):
        win = tk.Toplevel(self.root)
        win.title("Új bejegyzés")
        win.geometry("350x300")

        tk.Label(win, text="Dátum (YYYY-MM-DD):").pack()
        entry_date = tk.Entry(win)
        entry_date.pack(pady=5)

        tk.Label(win, text="Min. hőmérséklet:").pack()
        entry_min = tk.Entry(win)
        entry_min.pack(pady=5)

        tk.Label(win, text="Max. hőmérséklet:").pack()
        entry_max = tk.Entry(win)
        entry_max.pack(pady=5)


        def save():
            try:
                entry = WeatherEntry(
                    entry_date.get(),
                    float(entry_min.get()),
                    float(entry_max.get())
                )
                self.log.add_entry(entry)
                messagebox.showinfo("Siker", "Bejegyzés elmentve!")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Hiba", str(e))

        tk.Button(win, text="Mentés", command=save).pack(pady=20)


    def show_entries_window(self):
        win = tk.Toplevel(self.root)
        win.title("Bejegyzések")
        win.geometry("600x400")

        tree = ttk.Treeview(win, columns=("date", "min", "max"), show="headings")
        tree.heading("date", text="Dátum")
        tree.heading("min", text="Min (°C)")
        tree.heading("max", text="Max (°C)")
        tree.pack(fill=tk.BOTH, expand=True)

        for e in self.log.entries:
            tree.insert("", tk.END, values=(e.date, e.min_temp, e.max_temp))


    def search_window(self):
        win = tk.Toplevel(self.root)
        win.title("Keresés")
        win.geometry("600x400")

        tk.Label(win, text="Dátum:").pack()
        entry_date = tk.Entry(win)
        entry_date.pack(pady=15)

        tree = ttk.Treeview(win, columns=("date","min","max"), show="headings")
        tree.heading("date", text="Dátum")
        tree.heading("min", text="Min (°C)")
        tree.heading("max", text="Max (°C)")
        tree.pack(fill=tk.BOTH, expand=True)

        def search():
            for row in tree.get_children():
                tree.delete(row)

            results = self.log.find_by_date(entry_date.get())
            if not results:
                messagebox.showinfo("Nincs találat", "Nem található ilyen dátum.")
                return

            for e in results:
                tree.insert("", tk.END, values=(e.date, e.min_temp, e.max_temp))

        tk.Button(win, text="Keresés", command=search).pack(pady=5)


    def show_maximum(self):
        max = WeatherStatisticsTP.maximum_temperature(self.log.entries)
        if max is None:
            messagebox.showinfo("Maximum", "Nincs elég adat.")
        else:
            messagebox.showinfo("Maximum", f"Legmagasabb hőmérséklet: {max:} °C")

    def show_minimum(self):
        min = WeatherStatisticsTP.minimum_temperature(self.log.entries)
        if min is None:
            messagebox.showinfo("Minimum", "Nincs elég adat.")
        else:
            messagebox.showinfo("Minimum", f"Legalacsonyabb hőmérséklet: {min:} °C")

if __name__ == "__main__":
    root = tk.Tk()
    gui = WeatherAPP(root)
    root.mainloop()