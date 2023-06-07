import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "HateSpeech"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/configuration/gclud_syncer.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/ml/__init__.py",
    f"src/{project_name}/ml/model.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/pipeline/train_pipeline.py",
    f"src/{project_name}/constants/__init__.py",
    "Dockerfile",
    "app.py",
    "demo.py",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")