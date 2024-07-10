import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import base64
import math

MODIFIER = 9824516953
SHIFT = 69540112799
KEY = 413276118390
MOD_VALUE = 65536
ROUNDS = 90000
BLOCK_SIZE = 16

def hash_function(value, round, key):
    key = KEY + ord(key[round % len(key)])
    return (value * MODIFIER + int(math.floor(math.sin(key + round) * 1000)) + SHIFT + round) % MOD_VALUE

def double_hash_function(value, round, key1, key2):
    value = hash_function(value, round, key1)
    return hash_function(value, round, key2)

def reverse_hash_function(value, round, key):
    key = KEY + ord(key[round % len(key)])
    inverse = pow(MODIFIER, -1, MOD_VALUE)
    adjusted_value = (value - SHIFT - int(math.floor(math.sin(key + round) * 1000)) - round + MOD_VALUE) * inverse
    return adjusted_value % MOD_VALUE

def reverse_double_hash_function(value, round, key2, key1):
    value = reverse_hash_function(value, round, key2)
    return reverse_hash_function(value, round, key1)

def update_history(action, text, result):
    history_table.insert("", "end", values=(action, text[:50] + '...' if len(text) > 50 else text, result[:50] + '...' if len(result) > 50 else result))

def encrypt():
    input_text = input_text_entry.get("1.0", "end-1c")
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    if not input_text or not key1 or not key2:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    padded_text = input_text + '\0' * (BLOCK_SIZE - len(input_text) % BLOCK_SIZE)
    encrypted = []

    for i in range(0, len(padded_text), BLOCK_SIZE):
        block = padded_text[i:i+BLOCK_SIZE]
        for char in block:
            char_code = ord(char)
            for round in range(ROUNDS):
                char_code = double_hash_function(char_code, round, key1, key2)
            encrypted.append(char_code)

    binary_data = bytearray()
    for code in encrypted:
        binary_data.append(code & 0xff)
        binary_data.append((code >> 8) & 0xff)

    encoded_data = base64.b64encode(binary_data).decode('utf-8')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, encoded_data)
    update_history("Encrypt", input_text, encoded_data)

def decrypt():
    input_data = output_text.get("1.0", "end-1c")
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    if not input_data or not key1 or not key2:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        encoded_bytes = base64.b64decode(input_data)
        encrypted = [encoded_bytes[i] + (encoded_bytes[i + 1] << 8) for i in range(0, len(encoded_bytes), 2)]
        decrypted_text = ''

        for code in encrypted:
            for round in range(ROUNDS - 1, -1, -1):
                code = reverse_double_hash_function(code, round, key2, key1)
            decrypted_text += chr(code if code < 256 else 0)
        decrypted_text = decrypted_text.replace('\0', '')

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, decrypted_text)
        update_history("Decrypt", input_data, decrypted_text)
    except Exception as e:
        messagebox.showerror("Error", "Failed to decrypt. Please check the input and keys. Error: {}".format(str(e)))

root = tk.Tk()
root.title("Advanced Brute Cipher")
root.geometry("1000x800")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

input_label = tk.Label(frame, text="Text to Encrypt/Decrypt:")
input_label.pack()
input_text_entry = scrolledtext.ScrolledText(frame, height=5)
input_text_entry.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

key1_label = tk.Label(frame, text="Extra Key 1:")
key1_label.pack()
key1_entry = tk.Entry(frame)
key1_entry.pack(fill=tk.X, padx=5, pady=5)

key2_label = tk.Label(frame, text="Extra Key 2:")
key2_label.pack()
key2_entry = tk.Entry(frame)
key2_entry.pack(fill=tk.X, padx=5, pady=5)

encrypt_button = tk.Button(frame, text="Encrypt", command=encrypt)
encrypt_button.pack(side=tk.LEFT, padx=10, pady=10)

decrypt_button = tk.Button(frame, text="Decrypt", command=decrypt)
decrypt_button.pack(side=tk.RIGHT, padx=10, pady=10)

output_label = tk.Label(frame, text="Result:")
output_label.pack()
output_text = scrolledtext.ScrolledText(frame, height=5)
output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

history_label = tk.Label(frame, text="History:")
history_label.pack()
history_table = ttk.Treeview(frame, columns=("Action", "Input", "Result"), show="headings")
history_table.heading("Action", text="Action")
history_table.heading("Input", text="Input")
history_table.heading("Result", text="Result")
history_table.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

footer = tk.Label(frame, text="Beta Version 0.3.1 - July 2024\nGitHub: https://github.com/dogukansahil/BruteCipher", font=("Arial", 10))
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
