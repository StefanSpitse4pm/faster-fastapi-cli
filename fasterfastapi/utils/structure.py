import os
from appdirs import user_data_dir

def does_project_data_exist(app_name):
    data_dir = user_data_dir(app_name)
    if os.path.exists(data_dir):
        return True
    else:
        return False

