import tkinter as tk
from datetime import datetime
import pytz

class WorldClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reloj Mundial")
        self.clocks = {
            "China": "Asia/Shanghai",
            "Perú": "America/Lima",
            "EE.UU.": "America/New_York",
            "Argentina": "America/Argentina/Buenos_Aires",
            "Irlanda": "Europe/Dublin"
        }
        self.labels = {}
        self.setup_ui()
        self.update_clock()

    def setup_ui(self):
        for i, (country, timezone) in enumerate(self.clocks.items()):
            frame = tk.Frame(self.root)
            frame.pack(pady=10)
            label_country = tk.Label(frame, text=f"{country}:", font=('Arial', 14))
            label_country.pack(side=tk.LEFT)
            label_time = tk.Label(frame, text="", font=('Arial', 14))
            label_time.pack(side=tk.LEFT)
            self.labels[country] = label_time

    def update_clock(self):
        # Actualiza solo la hora en cada label
        for country, label in self.labels.items():
            tz = pytz.timezone(self.clocks[country])
            time_now = datetime.now(tz)
            label.config(text=time_now.strftime("%H:%M:%S"))  # Formato HH:MM:SS
        # Vuelve a llamar a la función cada 1000 ms (1 segundo)
        self.root.after(1000, self.update_clock)

def main():
    root = tk.Tk()
    app = WorldClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
