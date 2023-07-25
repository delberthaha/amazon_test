import os.path

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
folder_name = 'reports_folder'
folder_path = os.path.join(current_dir, folder_name)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
print(folder_path)