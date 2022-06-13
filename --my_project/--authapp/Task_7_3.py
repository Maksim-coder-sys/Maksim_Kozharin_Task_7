if __name__ == "__main__":

    import os
    import sys
    import shutil

    project7_path = 'C:\\Users\\Катя-Ноут\\PycharmProjects\\pythonProject7'
    f = [os.path.relpath(os.path.join(root, file), project7_path) for root, _, files in os.walk(
        project7_path) for file in files if file.endswith(".html")]
    for rel_path in f:
        path, file = os.path.split(rel_path)
        t_path = os.path.join(project7_path, "templates", path)
        if not os.path.exists(t_path):
            os.makedirs(t_path)
        shutil.copyfile(os.path.join(project7_path,rel_path), os.path.join(t_path, file))