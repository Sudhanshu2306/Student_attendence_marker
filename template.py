import os
from pathlib import Path as path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

project_name = 'Student_Attendence_Marker'

list_of_files =[
    f'src/ml/{project_name}/__init__.py',
    f'src/ml/{project_name}/components/__init__.py',
    f'src/ml/{project_name}/utils/__init__.py',
    f'src/ml/{project_name}/utils/common.py',
    f'src/ml/{project_name}/logging/__init__.py',
    f'src/ml/{project_name}/config/__init__.py',
    f'src/ml/{project_name}/config/configuration.py',
    f'src/ml/{project_name}/pipeline/__init__.py',
    f'src/ml/{project_name}/pipeline/configuration.py',
    f'src/ml/{project_name}/entities/__init__.py',
    f'src/ml/{project_name}/constants/__init__.py',
    f'config/config.yaml',
    'params.yaml',
    'Dockerfile',
    f"Public/Css/style.css",
    f"Public/Css/responsive.css",
    f"Public/JavaScript/index.js",
    f"Public/Images/trash.jpeg"
    "index.html"
    "app.js"
    f'reserch/trial.ipynb',
]

for file in list_of_files:
    filepath = path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory: {filedir} for file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating file: {filename}")

    else:
        logging.info(f"file {filename} already exists")