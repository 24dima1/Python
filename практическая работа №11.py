import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gubin Dmitrii")  # Записать свое имя
        self.geometry("600x400")
        self.create_tabs()
        self.create_menu()

    def create_menu(self):
         menubar = tk.Menu(self)
         filemenu = tk.Menu(menubar, tearoff=0)
         filemenu.add_command(label="Загрузить текст", command=self.load_text_from_file)
         menubar.add_cascade(label="Файл", menu=filemenu)
         self.config(menu=menubar)


    def create_tabs(self):
        tabControl = ttk.Notebook(self)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)

        tabControl.add(tab1, text='Калькулятор')
        tabControl.add(tab2, text='Чекбокс')
        tabControl.add(tab3, text='Поле для ввода текста')

        tabControl.pack(expand=1, fill="both", padx=10, pady=10)


        self.create_calculator_tab(tab1)
        self.create_checkboxes_tab(tab2)
        self.create_text_tab(tab3)

    def create_calculator_tab(self, tab):
        # Поля ввода
        tk.Label(tab, text="Введите число 1:").grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = tk.Entry(tab)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(tab, text="Введите число 2:").grid(row=1, column=0, padx=5, pady=5)
        self.num2_entry = tk.Entry(tab)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        # Выпадающий список
        operations = ["+", "-", "*", "/"]
        self.operation_combo = ttk.Combobox(tab, values=operations, state="readonly")
        self.operation_combo.current(0)
        self.operation_combo.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Калькулятор, кнопки
        calculate_button = tk.Button(tab, text="Калькулятор", command=self.calculate)
        calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(tab, text="Результат: ")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_combo.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    self.result_label.config(text="Нельзя делить на ноль")
                    return
                else:
                  result = num1 / num2
            self.result_label.config(text="Результат: " + str(result))
        except ValueError:
            self.result_label.config(text="Неверный ввод")


    def create_checkboxes_tab(self, tab):
      self.checkbox_vars = [tk.BooleanVar() for _ in range(3)]

      checkbox_texts = ["Первый", "Второй", "Третий"]
      for i, text in enumerate(checkbox_texts):
        checkbox = tk.Checkbutton(tab, text=text, variable=self.checkbox_vars[i])
        checkbox.grid(row=i, column=0, padx=5, pady=5, sticky="w")


      button = tk.Button(tab, text="Проверьте выбор", command=self.show_checkbox_selection)
      button.grid(row=len(checkbox_texts), column=0, padx=5, pady=5)


    def show_checkbox_selection(self):
      selected_options = [text for var, text in zip(self.checkbox_vars, ["Первый", "Второй", "Третий"]) if var.get()]

      if selected_options:
          messagebox.showinfo("Выберите", "Вы выбрали: " + ", ".join(selected_options))
      else:
          messagebox.showinfo("Выбор", "Никакие параметры не были выбраны")


    def create_text_tab(self, tab):
      self.text_area = tk.Text(tab, wrap="word")
      self.text_area.pack(expand=True, fill="both", padx=5, pady=5)


    def load_text_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    text = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, text)
            except Exception as e:
                messagebox.showerror("Error", f"Could not load the file.\nError: {e}")


if __name__ == "__main__":
    app = App()
    app.mainloop()