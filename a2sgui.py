import tkinter as tk
from tkinter import filedialog
import os
import json

def select_input_folder():
    input_dir = filedialog.askdirectory()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_dir)

def select_output_folder():
    output_dir = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_dir)

def run_script():
    input_dir = input_entry.get()
    output_dir = output_entry.get()
    load_size = scale.get()
    os.system(f'python test.py --dataroot {input_dir} --load_size {load_size} --output_dir {output_dir}')

def on_closing():
    data = {
        'input_dir': input_entry.get(),
        'output_dir': output_entry.get()
    }
    with open('config.json', 'w') as f:
        json.dump(data, f)
    root.destroy()

root = tk.Tk()
root.title("A2SKETCH")

font = ('TkDefaultFont', 16)

input_label = tk.Label(root, text="Input Folder", font=font)
input_label.pack()

input_entry = tk.Entry(root, font=font)
input_entry.pack()

input_button = tk.Button(root, text="Select Input Folder", command=select_input_folder, font=font)
input_button.pack()

output_label = tk.Label(root, text="Output Folder", font=font)
output_label.pack()

output_entry = tk.Entry(root, font=font)
output_entry.pack()

output_button = tk.Button(root, text="Select Output Folder", command=select_output_folder, font=font)
output_button.pack()

scale_label = tk.Label(root, text="Load Size", font=font)
scale_label.pack()

scale = tk.Scale(root, from_=512, to=2048, orient=tk.HORIZONTAL, resolution=64)
scale.set(1024)
scale.config(font=font)
scale.pack()

run_button = tk.Button(root, text="Run Script", command=run_script, font=font)
run_button.pack()

try:
    with open('config.json', 'r') as f:
        data = json.load(f)
        input_entry.insert(0, data['input_dir'])
        output_entry.insert(0, data['output_dir'])
except:
    input_entry.insert(0, './in')
    output_entry.insert(0, './out')

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()