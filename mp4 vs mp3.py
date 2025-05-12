import subprocess
import os
import time
from tkinter import Tk, filedialog, Button, Label, messagebox

def convert_mp4_to_mp3(file_path):
    output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not output_path:
        return  # User cancelled

    command = ['ffmpeg', '-i', file_path, '-q:a', '0', '-map', 'a', output_path]

    start_time = time.time()
    try:
        subprocess.run(command, check=True)
        elapsed = time.time() - start_time
        messagebox.showinfo("Success", f"Converted to:\n{output_path}\n\nTime: {elapsed:.2f} seconds")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to convert MP4 to MP3")

def convert_mp3_to_mp4(file_path):
    output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    if not output_path:
        return  # User cancelled

    # This creates a 5-second black video
    command = [
        'ffmpeg',
        '-loop', '1',
        '-f', 'lavfi',
        '-i', 'color=c=black:s=640x480:d=5',
        '-i', file_path,
        '-shortest',
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-pix_fmt', 'yuv420p',
        output_path
    ]

    start_time = time.time()
    try:
        subprocess.run(command, check=True)
        elapsed = time.time() - start_time
        messagebox.showinfo("Success", f"Converted to:\n{output_path}\n\nTime: {elapsed:.2f} seconds")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to convert MP3 to MP4")

def select_file_mp4():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        convert_mp4_to_mp3(file_path)

def select_file_mp3():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        convert_mp3_to_mp4(file_path)

# GUI Setup
app = Tk()
app.title("MP4 ↔ MP3 Converter")
app.geometry("300x200")

Label(app, text="Select a file to convert", font=("Arial", 14)).pack(pady=20)

Button(app, text="Convert MP4 to MP3", command=select_file_mp4, width=25).pack(pady=10)
Button(app, text="Convert MP3 to MP4", command=select_file_mp3, width=25).pack(pady=10)

app.mainloop()
