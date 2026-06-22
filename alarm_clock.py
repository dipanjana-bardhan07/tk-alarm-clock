import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Alarm Clock")
        self.root.geometry("400x350")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        # Alarm active state tracking
        self.alarm_set_time = None
        self.is_alarm_active = False

        # Create UI Elements
        self.create_widgets()
        
        # Start the background clock loop
        self.update_clock()

    def create_widgets(self):
        # 1. Main Title
        title_label = tk.Label(
            self.root, text="CURRENT TIME", font=("Helvetica", 12, "bold"),
            bg="#1e1e2e", fg="#cba6f7"
        )
        title_label.pack(pady=(20, 5))

        # 2. Live Digital Clock Display
        self.clock_label = tk.Label(
            self.root, text="", font=("Helvetica", 32, "bold"),
            bg="#252538", fg="#cdd6f4", width=12, bd=0
        )
        self.clock_label.pack(pady=10)

        # 3. Inputs Frame Container
        input_frame = tk.Frame(self.root, bg="#1e1e2e")
        input_frame.pack(pady=20)

        # Labels for dropdown headings
        tk.Label(input_frame, text="Hour", font=("Helvetica", 10), bg="#1e1e2e", fg="#a6adc8").grid(row=0, column=0, padx=10)
        tk.Label(input_frame, text="Minute", font=("Helvetica", 10), bg="#1e1e2e", fg="#a6adc8").grid(row=0, column=1, padx=10)
        tk.Label(input_frame, text="Second", font=("Helvetica", 10), bg="#1e1e2e", fg="#a6adc8").grid(row=0, column=2, padx=10)

        # Dropdown lists (24-hour format logic)
        self.hour_box = ttk.Combobox(input_frame, values=[f"{i:02d}" for i in range(24)], width=5, font=("Helvetica", 12), state="readonly")
        self.hour_box.grid(row=1, column=0, padx=5, pady=5)
        self.hour_box.set("00")

        self.min_box = ttk.Combobox(input_frame, values=[f"{i:02d}" for i in range(60)], width=5, font=("Helvetica", 12), state="readonly")
        self.min_box.grid(row=1, column=1, padx=5, pady=5)
        self.min_box.set("00")

        self.sec_box = ttk.Combobox(input_frame, values=[f"{i:02d}" for i in range(60)], width=5, font=("Helvetica", 12), state="readonly")
        self.sec_box.grid(row=1, column=2, padx=5, pady=5)
        self.sec_box.set("00")

        # 4. Action Button
        self.action_btn = tk.Button(
            self.root, text="SET ALARM", font=("Helvetica", 12, "bold"),
            bg="#a6e3a1", fg="#11111b", activebackground="#94e2d5",
            bd=0, cursor="hand2", width=15, height=1, command=self.toggle_alarm
        )
        self.action_btn.pack(pady=10)

        # 5. Status text helper
        self.status_label = tk.Label(self.root, text="No active alarm set.", font=("Helvetica", 10, "italic"), bg="#1e1e2e", fg="#a6adc8")
        self.status_label.pack()

    def update_clock(self):
        # Read the local time in HH:MM:SS format
        current_time_str = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time_str)

        # Check if current time matches target alarm trigger state
        if self.is_alarm_active and current_time_str == self.alarm_set_time:
            self.trigger_alarm_alert()

        # Run again automatically in 1 second
        self.root.after(1000, self.update_clock)

    def toggle_alarm(self):
        if not self.is_alarm_active:
            # Capturing targets from choice matrices
            h = self.hour_box.get()
            m = self.min_box.get()
            s = self.sec_box.get()
            
            self.alarm_set_time = f"{h}:{m}:{s}"
            self.is_alarm_active = True
            
            # Visual State Swap
            self.action_btn.config(text="STOP/CANCEL", bg="#f38ba8")
            self.status_label.config(text=f"Alarm armed for: {self.alarm_set_time}", fg="#f9e2af")
        else:
            # Turn alarm off completely
            self.reset_alarm_state()

    def trigger_alarm_alert(self):
        # Flash visual indicators on window layout boundaries
        self.root.bell()  # Default operating system system bell ding
        messagebox.showinfo("Alarm Triggered", f"Wake Up!\nTime is exactly {self.alarm_set_time}!")
        self.reset_alarm_state()

    def reset_alarm_state(self):
        self.is_alarm_active = False
        self.alarm_set_time = None
        self.action_btn.config(text="SET ALARM", bg="#a6e3a1")
        self.status_label.config(text="No active alarm set.", fg="#a6adc8")


if __name__ == "__main__":
    # Customizing look of standard ttk combo widgets slightly
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use('clam')
    
    app = AlarmClock(root)
    root.mainloop()