import tkinter as tk
from tkinter import messagebox
import base64
import math

MODIFIER = 982451653
SHIFT = 6954011279
KEY = 43723116108
MOD_VALUE = 65536
ROUNDS = 6231

def hash_function(value, round, extra_key):
    key = KEY + ord(extra_key[round % len(extra_key)])
    return (value * MODIFIER + int(math.floor(math.sin(key + round) * 1000)) + SHIFT + round) % MOD_VALUE

def double_hash_function(value, round, extra_key1, extra_key2):
    hashed_value = hash_function(value, round, extra_key1)
    return hash_function(hashed_value, round, extra_key2)

def encrypt():
    input_text = input_text_entry.get()
    extra_key1 = extra_key1_entry.get()
    extra_key2 = extra_key2_entry.get()
    if not input_text or not extra_key1 or not extra_key2:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    char_codes = []
    for char in input_text:
        char_code = ord(char)
        for round in range(ROUNDS):
            char_code = double_hash_function(char_code, round, extra_key1, extra_key2)
        char_codes.append(char_code)
    uint16array = bytearray()
    for code in char_codes:
        uint16array.append(code & 0xFF)
        uint16array.append((code >> 8) & 0xFF)
    encrypted_text = base64.b64encode(uint16array).decode('utf-8')
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, encrypted_text)

def decrypt():
    input_text = input_text_entry.get()
    extra_key1 = extra_key1_entry.get()
    extra_key2 = extra_key2_entry.get()
    if not input_text or not extra_key1 or not extra_key2:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    encoded_text = base64.b64decode(input_text)
    char_codes = []
    for i in range(0, len(encoded_text), 2):
        char_code = encoded_text[i] + (encoded_text[i + 1] << 8)
        for round in range(ROUNDS - 1, -1, -1):
            char_code = reverse_double_hash_function(char_code, round, extra_key1, extra_key2)
        char_codes.append(char_code)
    result = ''.join(chr(code) for code in char_codes)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

def reverse_double_hash_function(value, round, extra_key1, extra_key2):
    hashed_value = reverse_hash_function(value, round, extra_key2)
    return reverse_hash_function(hashed_value, round, extra_key1)

def reverse_hash_function(value, round, extra_key):
    key = KEY + ord(extra_key[round % len(extra_key)])
    return (value - SHIFT - int(math.floor(math.sin(key + round) * 1000)) - round + MOD_VALUE) * pow(MODIFIER, -1, MOD_VALUE) % MOD_VALUE

app = tk.Tk()
app.title("BruteCipher")
app.geometry("600x450")

input_frame = tk.Frame(app, padx=10, pady=10)
input_frame.pack(pady=20)

result_frame = tk.Frame(app, padx=10, pady=10)
result_frame.pack(pady=10)

input_text_label = tk.Label(input_frame, text="Text to Encrypt/Decrypt:", font=("Arial", 12))
input_text_label.grid(row=0, column=0, sticky="w")
input_text_entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
input_text_entry.grid(row=0, column=1, pady=5)

extra_key1_label = tk.Label(input_frame, text="Extra Key 1:", font=("Arial", 12))
extra_key1_label.grid(row=1, column=0, sticky="w")
extra_key1_entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
extra_key1_entry.grid(row=1, column=1, pady=5)

extra_key2_label = tk.Label(input_frame, text="Extra Key 2:", font=("Arial", 12))
extra_key2_label.grid(row=2, column=0, sticky="w")
extra_key2_entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
extra_key2_entry.grid(row=2, column=1, pady=5)

button_frame = tk.Frame(app, padx=10, pady=10)
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt", command=encrypt, font=("Arial", 12), bg="#4CAF50", fg="black")
encrypt_button.grid(row=0, column=0, padx=5)

decrypt_button = tk.Button(button_frame, text="Decrypt", command=decrypt, font=("Arial", 12), bg="#2196F3", fg="black")
decrypt_button.grid(row=0, column=1, padx=5)

result_text = tk.Text(result_frame, height=5, width=50, font=("Arial", 12))
result_text.pack()

# Versiyon ve GitHub bağlantısı
footer_frame = tk.Frame(app, padx=10, pady=10)
footer_frame.pack(pady=10)

footer_label = tk.Label(footer_frame, text="Beta Version 0.1.1 - July 2024\nGitHub: https://github.com/dogukansahil/BruteCipher", font=("Arial", 8))
footer_label.pack()

app.mainloop()
