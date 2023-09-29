Facemask detection
==============================

YOLOv5 model trained on a custom dataset to detect human faces and label them according to the face masks: mask on, off or weared incorrectly.

Project Organization
==============================

   
    ├── README.md                    <- The top-level README for developers using this project.
    │
    ├── GETTING_STARTED.rst          <- About startin app
    │
    ├── requirements.txt             <- The requirements file for reproducing the analysis environment, e.g.
    │                                  generated with `pip freeze > requirements.txt`
    │
    ├── setup.py                     <- makes project pip installable (pip install -e .) so src can be imported
    │
    ├── Facemask_checking            <- Source code for use in this project.
    │   ├── __init__.py              <- Makes src a Python module
    │   │
    │   ├── data                     <- Scripts to handle data
    │   │   └── create_yaml.py       <- Creates .yaml file required for yolo training 
    │   │   └── get_annotations.py   <- Read annotations as dataframe
    │   │   └── get_labels.py        <- Read labels and add to dataframe
    │   │   └── parse_data.py        <- Data parser
    │   │   └── split_data.py        <- Splits data into training and validation dirs
    │   │
    │   ├── features                     <- Scripts to turn raw data into features for modeling
    │   │   └── choose_loading.py        <- Used to choose between training and loading model
    │   │   └── choose_mode.py           <- Choose mode to use
    │   │   └── cv2_handling.py          <- Cv2 script to detect masks on a video/camera
    │   │   └── get_latest_weights.py    <- Load latest weights
    │   │   └── image_mode.py            <- Script to detect masks on an image
    │   │  
    │   │
    │   ├── model                  <- Scripts to train/load model
    │   │   │── train_model.py     <- Train new model               
    │   │   ├── load_model.py      <- Load existing weights to the model
    │   │
    └── tox.ini            <- tox file with settings for running tox


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
