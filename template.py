import os
from pathlib import Path
import logging
list_of_files = [

    # Root Files
    "README.md",
    "requirements.txt",
    ".gitignore",

    # Data
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/external/.gitkeep",

    # Notebooks
    "notebooks/01_Data_Collection.ipynb",
    "notebooks/02_Data_Preprocessing.ipynb",
    "notebooks/03_Exploratory_Data_Analysis.ipynb",
    "notebooks/04_Feature_Engineering.ipynb",
    "notebooks/05_Stationarity_Testing.ipynb",
    "notebooks/06_ARIMA_Model.ipynb",
    "notebooks/07_SARIMA_Model.ipynb",
    "notebooks/08_LSTM_Model.ipynb",
    "notebooks/09_Model_Evaluation.ipynb",
    "notebooks/10_Forecasting.ipynb",
    "notebooks/11_Streamlit_Dashboard.ipynb",

    # Source Code
    "src/__init__.py",
    "src/config.py",
    "src/data_loader.py",
    "src/preprocessing.py",
    "src/feature_engineering.py",
    "src/visualization.py",
    "src/stationarity.py",
    "src/arima_model.py",
    "src/sarima_model.py",
    "src/lstm_model.py",
    "src/evaluation.py",
    "src/forecast.py",
    "src/utils.py",
    "src/exception.py",
    "src/logger.py",

    # Models
    "models/.gitkeep",

    # Outputs
    "outputs/graphs/.gitkeep",
    "outputs/reports/.gitkeep",
    "outputs/predictions/.gitkeep",
    "outputs/metrics/.gitkeep",

    # Streamlit App
    "streamlit/app.py",
    "streamlit/pages/1_Historical_Data.py",
    "streamlit/pages/2_Forecasting.py",
    "streamlit/pages/3_Model_Comparison.py",

    # Tests
    "tests/__init__.py",
    "tests/test_preprocessing.py",
    "tests/test_models.py",
    "tests/test_forecast.py",

    # Documentation
    "docs/Project_Report.docx",
    "docs/Presentation.pptx",
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating file: {filename}")

    else:
        logging.info(f"File already exists: {filename}")