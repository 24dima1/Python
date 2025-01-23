import tkinter as tk
from tkinter import ttk, messagebox
#import requests
import json
import pip._vendor.requests as requests


class GitHubUserInfoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GitHub User Info")
        self.geometry("600x300")
        self.create_widgets()

    def create_widgets(self):
        # Username label and entry
        tk.Label(self, text="Enter GitHub Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Fetch button
        fetch_button = tk.Button(self, text="Get User Info", command=self.fetch_user_info)
        fetch_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Status label
        self.status_label = tk.Label(self, text="")
        self.status_label.grid(row=2, column=0, columnspan=2, pady=5)

    def fetch_user_info(self):
        username = self.username_entry.get().strip()
        if not username:
            self.status_label.config(text="Please enter a GitHub username.")
            return

        user_data = self.get_user_data(username)

        if user_data:
            output_filename = f"{username}_user_info.json"
            self.write_user_info_to_file(user_data, output_filename)
            self.status_label.config(text=f"Information written to {output_filename}")
        else:
           self.status_label.config(text="User not found or data is not valid")

    def get_user_data(self, username):
        try:
            url = f"https://api.github.com/users/{username}"
            response = requests.get(url)
            response.raise_for_status()
            user_data = response.json()
            return self.extract_required_data(user_data)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Request error: {e}")
            return None
        except ValueError as e:
             messagebox.showerror("Error", f"Error decoding JSON: {e}")
             return None


    def extract_required_data(self, user_data):
      todos_by_user = {}
      for todo in user_data.keys():
        if todo in ['company', 'created_at', 'id', 'name', 'url', 'email']:
          todos_by_user.update({f'{todo}': f'{str(user_data[todo])}'})
      return todos_by_user

    def write_user_info_to_file(self, user_data, filename):
        try:
          with open(filename, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Error writing to file: {e}")



if __name__ == "__main__":
    app = GitHubUserInfoApp()
    app.mainloop()