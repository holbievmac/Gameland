import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os

class ProjectTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Project Tracker')
        self.geometry('800x600')
        self.data_file = 'projects.json'
        self.projects = {}
        self.load_projects()
        self.setup_widgets()

    def setup_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(pady=20, padx=20, fill='both', expand=True)

        project_frame = ttk.LabelFrame(main_frame, text="Projects")
        project_frame.pack(fill='x', expand=True)

        self.project_name_entry = ttk.Entry(project_frame, width=30)
        self.project_name_entry.pack(side='left', padx=(0, 10))

        add_project_button = ttk.Button(project_frame, text='Add Project', command=self.add_project)
        add_project_button.pack(side='left', padx=(0, 10))

        remove_project_button = ttk.Button(project_frame, text='Remove Selected Project', command=self.remove_project)
        remove_project_button.pack(side='left')

        self.project_listbox = tk.Listbox(main_frame, height=10)
        self.project_listbox.pack(fill='x', padx=20, expand=True)
        self.update_project_listbox()

        task_frame = ttk.LabelFrame(main_frame, text="Tasks")
        task_frame.pack(fill='both', expand=True)

        self.task_name_entry = ttk.Entry(task_frame, width=30)
        self.task_name_entry.pack(side='left', padx=(0, 10))

        add_task_button = ttk.Button(task_frame, text='Add Task', command=self.add_task)
        add_task_button.pack(side='left', padx=(0, 10))

        remove_task_button = ttk.Button(task_frame, text='Remove Selected Tasks', command=self.remove_selected_tasks)
        remove_task_button.pack(side='right')

        self.project_listbox.bind('<<ListboxSelect>>', self.on_project_selected)
        self.task_frame = ttk.Frame(task_frame)
        self.task_frame.pack(fill='both', expand=True)
        self.task_vars = {}

    def add_project(self):
        project_name = self.project_name_entry.get()
        if project_name and project_name not in self.projects:
            self.projects[project_name] = []
            self.update_project_listbox()
            self.project_name_entry.delete(0, 'end')
            self.save_projects()
        else:
            messagebox.showerror('Error', 'Project already exists or invalid name.')

    def remove_project(self):
        selection = self.project_listbox.curselection()
        if selection:
            project = self.project_listbox.get(selection[0])
            del self.projects[project]
            self.update_project_listbox()
            self.save_projects()

    def add_task(self):
        task_name = self.task_name_entry.get()
        selection = self.project_listbox.curselection()
        if task_name and selection:
            project = self.project_listbox.get(selection[0])
            due_date = simpledialog.askstring("Input", "Enter due date for task (YYYY-MM-DD):")
            task_entry = {'task': task_name, 'due_date': due_date}
            self.projects[project].append(task_entry)
            self.task_name_entry.delete(0, 'end')
            self.update_task_listbox(project)
            self.save_projects()
        else:
            messagebox.showerror('Error', 'Invalid task name or no project selected.')

    def remove_selected_tasks(self):
        project = self.project_listbox.get(self.project_listbox.curselection()[0])
        self.projects[project] = [task for task in self.projects[project] if not self.task_vars[task['task']].get()]
        self.update_task_listbox(project)
        self.save_projects()

    def on_project_selected(self, event):
        if not self.project_listbox.curselection():
            return
        project = self.project_listbox.get(self.project_listbox.curselection())
        self.update_task_listbox(project)

    def update_task_listbox(self, project):
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        self.task_vars = {}
        for task in self.projects[project]:
            self.task_vars[task['task']] = tk.BooleanVar()
            chk = ttk.Checkbutton(self.task_frame, text=f"{task['task']} (Due: {task['due_date']})", variable=self.task_vars[task['task']])
            chk.pack(anchor='w')

    def save_projects(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.projects, file)

    def load_projects(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.projects = json.load(file)

    def update_project_listbox(self):
        self.project_listbox.delete(0, 'end')
        for project in self.projects:
            self.project_listbox.insert('end', project)

if __name__ == "__main__":
    app = ProjectTrackerApp()
    app.mainloop()
