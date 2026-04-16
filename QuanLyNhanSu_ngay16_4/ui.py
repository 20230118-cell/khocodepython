import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import *

def run_app():

    root = tk.Tk()
    root.title("PHẦN MỀM QUẢN LÝ NHÂN SỰ")
    root.geometry("1000x550")
    root.configure(bg="#f0f0f0")

    # ========================
    # TITLE
    # ========================
    tk.Label(
        root,
        text="QUẢN LÝ NHÂN SỰ",
        font=("Times New Roman",18,"bold"),
        bg="#f0f0f0",
        fg="blue"
    ).pack(pady=10)

    # ========================
    # FRAME FORM
    # ========================
    frame_form = tk.LabelFrame(
        root,
        text="Thông tin nhân sự",
        font=("Times New Roman",12,"bold"),
        padx=10,
        pady=10
    )
    frame_form.place(x=20,y=60,width=300,height=280)

    tk.Label(frame_form,text="CCCD").grid(row=0,column=0,sticky="w",pady=5)
    entry_cccd = tk.Entry(frame_form,width=25)
    entry_cccd.grid(row=0,column=1)

    tk.Label(frame_form,text="Họ tên").grid(row=1,column=0,sticky="w",pady=5)
    entry_hoten = tk.Entry(frame_form,width=25)
    entry_hoten.grid(row=1,column=1)

    tk.Label(frame_form,text="Ngày sinh").grid(row=2,column=0,sticky="w",pady=5)
    entry_ngaysinh = tk.Entry(frame_form,width=25)
    entry_ngaysinh.grid(row=2,column=1)

    tk.Label(frame_form,text="Giới tính").grid(row=3,column=0,sticky="w",pady=5)
    combo = ttk.Combobox(frame_form,values=["Nam","Nữ"],width=22)
    combo.grid(row=3,column=1)

    tk.Label(frame_form,text="Địa chỉ").grid(row=4,column=0,sticky="w",pady=5)
    entry_diachi = tk.Entry(frame_form,width=25)
    entry_diachi.grid(row=4,column=1)

    # ========================
    # BUTTON FRAME
    # ========================
    frame_btn = tk.Frame(root,bg="#f0f0f0")
    frame_btn.place(x=20,y=350)

    tk.Button(frame_btn,text="Thêm",width=10,bg="#4CAF50",fg="white",command=lambda:add()).grid(row=0,column=0,padx=5)
    tk.Button(frame_btn,text="Sửa",width=10,bg="#2196F3",fg="white",command=lambda:edit()).grid(row=0,column=1,padx=5)
    tk.Button(frame_btn,text="Xóa",width=10,bg="#f44336",fg="white",command=lambda:remove()).grid(row=0,column=2,padx=5)
    tk.Button(frame_btn,text="Hiển thị",width=10,bg="#9C27B0",fg="white",command=lambda:show()).grid(row=0,column=3,padx=5)

    # ========================
    # SEARCH
    # ========================
    tk.Label(root,text="Tìm kiếm:",bg="#f0f0f0").place(x=350,y=65)

    entry_search = tk.Entry(root,width=30)
    entry_search.place(x=420,y=65)

    tk.Button(root,text="Tìm",bg="#FF9800",fg="white",command=lambda:find()).place(x=650,y=62)

    # ========================
    # TABLE FRAME
    # ========================
    frame_table = tk.Frame(root)
    frame_table.place(x=350,y=100,width=620,height=400)

    cols=("CCCD","Họ tên","Ngày sinh","Giới tính","Địa chỉ")

    tree=ttk.Treeview(frame_table,columns=cols,show="headings")

    # Scrollbar
    scroll_y = ttk.Scrollbar(frame_table,orient="vertical",command=tree.yview)
    scroll_x = ttk.Scrollbar(frame_table,orient="horizontal",command=tree.xview)

    tree.configure(yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

    tree.pack(side="left",fill="both",expand=True)
    scroll_y.pack(side="right",fill="y")
    scroll_x.pack(side="bottom",fill="x")

    for col in cols:
        tree.heading(col,text=col)
        tree.column(col,width=120,anchor="center")

    # ========================
    # FUNCTIONS
    # ========================
    def show():
        for i in tree.get_children():
            tree.delete(i)

        data = get_all()

        for row in data:
            tree.insert("",tk.END,values=row)

    def add():
        insert(
            entry_cccd.get(),
            entry_hoten.get(),
            entry_ngaysinh.get(),
            combo.get(),
            entry_diachi.get()
        )
        show()

    def remove():
        selected = tree.focus()
        if selected == "":
            return

        data = tree.item(selected)["values"]
        delete(data[0])
        show()

    def edit():
        update(
            entry_cccd.get(),
            entry_hoten.get(),
            entry_ngaysinh.get(),
            combo.get(),
            entry_diachi.get()
        )
        show()

    def find():
        keyword = entry_search.get()

        for i in tree.get_children():
            tree.delete(i)

        for row in search(keyword):
            tree.insert("",tk.END,values=row)

    def click(event):
        selected = tree.focus()
        if selected == "":
            return

        data = tree.item(selected)["values"]

        entry_cccd.delete(0,tk.END)
        entry_cccd.insert(0,data[0])

        entry_hoten.delete(0,tk.END)
        entry_hoten.insert(0,data[1])

        entry_ngaysinh.delete(0,tk.END)
        entry_ngaysinh.insert(0,data[2])

        combo.set(data[3])

        entry_diachi.delete(0,tk.END)
        entry_diachi.insert(0,data[4])

    tree.bind("<<TreeviewSelect>>",click)

    show()
    root.mainloop()