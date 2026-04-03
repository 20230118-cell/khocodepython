import tkinter as tk
from tkinter import filedialog, messagebox
import difflib

from normalizer_advanced import normalize_code_advanced
from ast_compare import compare_ast


# =========================
# ĐỌC FILE
# =========================
def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""


# =========================
# SO SÁNH
# =========================
def compare_texts(code1, code2):
    if not code1.strip() or not code2.strip():
        messagebox.showerror("Lỗi", "Thiếu code!")
        return

    # ✅ dùng normalize cho TEXT
    norm1 = normalize_code_advanced(code1)
    norm2 = normalize_code_advanced(code2)

    text_similarity = difflib.SequenceMatcher(None, norm1, norm2).ratio() * 100

    # ❗ AST dùng code GỐC (QUAN TRỌNG)
    ast_similarity = compare_ast(code1, code2)

    result_text.set(f"Text: {text_similarity:.2f}% | AST: {ast_similarity:.2f}%")


# =========================
# LOAD FILE
# =========================
def load_file1():
    path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if path:
        code = read_file(path)
        text1.delete("1.0", tk.END)
        text1.insert(tk.END, code)


def load_file2():
    path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if path:
        code = read_file(path)
        text2.delete("1.0", tk.END)
        text2.insert(tk.END, code)


# =========================
# SO SÁNH
# =========================
def compare_from_textbox():
    code1 = text1.get("1.0", tk.END)
    code2 = text2.get("1.0", tk.END)
    compare_texts(code1, code2)


# =========================
# GUI
# =========================
root = tk.Tk()
root.title("Tool So Sánh Code Python (FULL Nâng cao)")
root.geometry("950x550")

# Label
tk.Label(root, text="Code 1").grid(row=0, column=0)
tk.Label(root, text="Code 2").grid(row=0, column=1)

# Textbox
text1 = tk.Text(root, width=55, height=22)
text1.grid(row=1, column=0, padx=10)

text2 = tk.Text(root, width=55, height=22)
text2.grid(row=1, column=1, padx=10)

# Button load file
tk.Button(root, text="Load File 1", command=load_file1).grid(row=2, column=0, pady=5)
tk.Button(root, text="Load File 2", command=load_file2).grid(row=2, column=1, pady=5)

# Button compare
tk.Button(root, text="So sánh", command=compare_from_textbox, bg="lightblue").grid(
    row=3, column=0, columnspan=2, pady=10
)

# Result
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, fg="blue", font=("Arial", 14)).grid(
    row=4, column=0, columnspan=2
)

root.mainloop()