import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import base64
import math
import os
import git

MODIFIER = 9824516953
SHIFT = 69540112799
KEY = 413276118390
MOD_VALUE = 65536
ROUNDS = 90000
BLOCK_SIZE = 16

languages = {
    "en": {
        "title": "Advanced Brute Cipher",
        "text_to_encrypt_decrypt": "Text to Encrypt/Decrypt:",
        "extra_key1": "Extra Key 1:",
        "extra_key2": "Extra Key 2:",
        "encrypt": "Encrypt",
        "decrypt": "Decrypt",
        "result": "Result:",
        "history": "History:",
        "error": "Error",
        "fill_all_fields": "Please fill in all fields.",
        "failed_to_decrypt": "Failed to decrypt. Please check the input and keys. Error: ",
        "version": "Beta Version 0.3.3.1 - July 2024\nGitHub: https://github.com/dogukansahil/BruteCipher",
        "update_available": "Update available! Please restart the application.",
        "no_update": "You are already up to date.",
        "not_a_git_repo": "The specified directory is not a git repository."
    },
    "tr": {
        "title": "Gelişmiş Brute Şifreleme",
        "text_to_encrypt_decrypt": "Şifrelenecek/Şifresi Çözülecek Metin:",
        "extra_key1": "Ek Anahtar 1:",
        "extra_key2": "Ek Anahtar 2:",
        "encrypt": "Şifrele",
        "decrypt": "Şifre Çöz",
        "result": "Sonuç:",
        "history": "Geçmiş:",
        "error": "Hata",
        "fill_all_fields": "Lütfen tüm alanları doldurun.",
        "failed_to_decrypt": "Şifre çözme başarısız oldu. Lütfen girişi ve anahtarları kontrol edin. Hata: ",
        "version": "Beta Sürüm 0.3.3.1 - Temmuz 2024\nGitHub: https://github.com/dogukansahil/BruteCipher",
        "update_available": "Güncelleme mevcut! Lütfen uygulamayı yeniden başlatın.",
        "no_update": "Zaten güncelsiniz.",
        "not_a_git_repo": "Belirtilen dizin bir git deposu değil."
    },
    "ru": {
        "title": "Продвинутое Брют Шифрование",
        "text_to_encrypt_decrypt": "Текст для Шифрования/Расшифровки:",
        "extra_key1": "Дополнительный Ключ 1:",
        "extra_key2": "Дополнительный Ключ 2:",
        "encrypt": "Зашифровать",
        "decrypt": "Расшифровать",
        "result": "Результат:",
        "history": "История:",
        "error": "Ошибка",
        "fill_all_fields": "Пожалуйста, заполните все поля.",
        "failed_to_decrypt": "Не удалось расшифровать. Пожалуйста, проверьте входные данные и ключи. Ошибка: ",
        "version": "Бета Версия 0.3.3.1 - Июль 2024\nGitHub: https://github.com/dogukansahil/BruteCipher",
        "update_available": "Доступно обновление! Пожалуйста, перезапустите приложение.",
        "no_update": "Вы уже обновлены."
    },
    "es": {
        "title": "Cifrado Avanzado de Fuerza Bruta",
        "text_to_encrypt_decrypt": "Texto para Cifrar/Descifrar:",
        "extra_key1": "Clave Extra 1:",
        "extra_key2": "Clave Extra 2:",
        "encrypt": "Cifrar",
        "decrypt": "Descifrar",
        "result": "Resultado:",
        "history": "Historia:",
        "error": "Error",
        "fill_all_fields": "Por favor, complete todos los campos.",
        "failed_to_decrypt": "No se pudo descifrar. Por favor, verifique la entrada y las claves. Error: ",
        "version": "Versión Beta 0.3.3.1 - Julio 2024\nGitHub: https://github.com/dogukansahil/BruteCipher",
        "update_available": "¡Actualización disponible! Por favor, reinicie la aplicación.",
        "no_update": "Ya estás actualizado."
    },
    "de": {
        "title": "Erweitertes Brute Cipher",
        "text_to_encrypt_decrypt": "Text zum Verschlüsseln/Entschlüsseln:",
        "extra_key1": "Zusatzschlüssel 1:",
        "extra_key2": "Zusatzschlüssel 2:",
        "encrypt": "Verschlüsseln",
        "decrypt": "Entschlüsseln",
        "result": "Ergebnis:",
        "history": "Geschichte:",
        "error": "Fehler",
        "fill_all_fields": "Bitte füllen Sie alle Felder aus.",
        "failed_to_decrypt": "Entschlüsselung fehlgeschlagen. Bitte überprüfen Sie die Eingabe und die Schlüssel. Fehler: ",
        "version": "Beta Version 0.3.3.1 - Juli 2024\nGitHub: https://github.com/dogukansahil/BruteCipher",
        "update_available": "Update verfügbar! Bitte starten Sie die Anwendung neu.",
        "no_update": "Sie sind bereits auf dem neuesten Stand."
    },
    "it": {
        "title": "Cifratura Avanzata Brute",
        "text_to_encrypt_decrypt": "Testo da Cifrare/Decifrare:",
        "extra_key1": "Chiave Extra 1:",
        "extra_key2": "Chiave Extra 2:",
        "encrypt": "Cifra",
        "decrypt": "Decifra",
        "result": "Risultato:",
        "history": "Storia:",
        "error": "Errore",
        "fill_all_fields": "Per favore, compila tutti i campi.",
        "failed_to_decrypt": "Impossibile decrittografare. Si prega di controllare l'input e le chiavi. Errore: ",
        "version": "Versione Beta 0.3.3.1 - Luglio 2024\nGitHub: https://github.com/dogukansahil/BruteCipher",
        "update_available": "Aggiornamento disponibile! Si prega di riavviare l'applicazione.",
        "no_update": "Sei già aggiornato."
    },
    "zh": {
        "title": "高级暴力密码",
        "text_to_encrypt_decrypt": "要加密/解密的文本：",
        "extra_key1": "额外密钥1：",
        "extra_key2": "额外密钥2：",
        "encrypt": "加密",
        "decrypt": "解密",
        "result": "结果：",
        "history": "历史：",
        "error": "错误",
        "fill_all_fields": "请填写所有字段。",
        "failed_to_decrypt": "解密失败。请检查输入和密钥。错误：",
        "version": "Beta版本 0.3.3.1 - 2024年7月\nGitHub: https://github.com/dogukansahil/BruteCipher",
        "update_available": "更新可用！请重新启动应用程序。",
        "no_update": "您已经是最新的。"
    }
}

current_language = "en"

def translate(key):
    return languages[current_language].get(key, key)

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
        messagebox.showerror(translate("error"), translate("fill_all_fields"))
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
        messagebox.showerror(translate("error"), translate("fill_all_fields"))
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
        messagebox.showerror(translate("error"), translate("failed_to_decrypt") + str(e))

def change_language(lang):
    global current_language
    current_language = lang
    root.title(translate("title"))
    input_label.config(text=translate("text_to_encrypt_decrypt"))
    key1_label.config(text=translate("extra_key1"))
    key2_label.config(text=translate("extra_key2"))
    encrypt_button.config(text=translate("encrypt"))
    decrypt_button.config(text=translate("decrypt"))
    output_label.config(text=translate("result"))
    history_label.config(text=translate("history"))
    footer.config(text=translate("version"))

def update_application():
    repo_path = os.path.abspath("/Users/sahil/Desktop/AdvancedBruteCipher")  # Git deposunun doğru yolunu belirtin
    try:
        repo = git.Repo(repo_path)
    except git.exc.InvalidGitRepositoryError:
        messagebox.showerror(translate("error"), translate("not_a_git_repo"))
        return
    
    current_commit = repo.head.commit
    repo.remote().pull()
    new_commit = repo.head.commit
    if current_commit != new_commit:
        messagebox.showinfo(translate("update_available"), translate("update_available"))
    else:
        messagebox.showinfo(translate("no_update"), translate("no_update"))

root = tk.Tk()
root.title(translate("title"))
root.geometry("1000x800")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

language_selector = ttk.Combobox(frame, values=["English", "Türkçe", "Русский", "Español", "Deutsch", "Italiano", "中文"], state="readonly")
language_selector.current(0)
language_selector.pack()
language_selector.bind("<<ComboboxSelected>>", lambda event: change_language(
    "tr" if language_selector.get() == "Türkçe" else 
    "ru" if language_selector.get() == "Русский" else 
    "es" if language_selector.get() == "Español" else 
    "de" if language_selector.get() == "Deutsch" else 
    "it" if language_selector.get() == "Italiano" else 
    "zh" if language_selector.get() == "中文" else "en"
))

input_label = tk.Label(frame, text=translate("text_to_encrypt_decrypt"))
input_label.pack()
input_text_entry = scrolledtext.ScrolledText(frame, height=5)
input_text_entry.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

key1_label = tk.Label(frame, text=translate("extra_key1"))
key1_label.pack()
key1_entry = tk.Entry(frame)
key1_entry.pack(fill=tk.X, padx=5, pady=5)

key2_label = tk.Label(frame, text=translate("extra_key2"))
key2_label.pack()
key2_entry = tk.Entry(frame)
key2_entry.pack(fill=tk.X, padx=5, pady=5)

encrypt_button = tk.Button(frame, text=translate("encrypt"), command=encrypt)
encrypt_button.pack(side=tk.LEFT, padx=10, pady=10)

decrypt_button = tk.Button(frame, text=translate("decrypt"), command=decrypt)
decrypt_button.pack(side=tk.RIGHT, padx=10, pady=10)

update_button = tk.Button(frame, text="Update Application", command=update_application)
update_button.pack(side=tk.BOTTOM, padx=10, pady=10)

output_label = tk.Label(frame, text=translate("result"))
output_label.pack()
output_text = scrolledtext.ScrolledText(frame, height=5)
output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

history_label = tk.Label(frame, text=translate("history"))
history_label.pack()
history_table = ttk.Treeview(frame, columns=("Action", "Input", "Result"), show="headings")
history_table.heading("Action", text="Action")
history_table.heading("Input", text="Input")
history_table.heading("Result", text="Result")
history_table.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

footer = tk.Label(frame, text=translate("version"), font=("Arial", 10))
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
