import glob
import xml.etree.ElementTree as ET
from typing import Dict
import pandas as pd

def get_annotations(path: str, classes: list) -> Dict:
    dataset = {
                "file":[],
                "classnames":[],
                "class_id":[],
                "width":[],
                "height":[],
                "xmin":[],
                "ymin":[],
                "xmax":[],
                "ymax":[]
            }

    path_to_annotations= path + r"\Annotations\*.xml" 

    for item in glob.glob(path_to_annotations):
        tree = ET.parse(item)
        
        for elem in tree.iter():
            if 'filename' in elem.tag:
                filename=elem.text
            elif 'width' in elem.tag:
                width=int(elem.text)
            elif 'height' in elem.tag:
                height=int(elem.text)
            elif 'name' in elem.tag:
                classname=elem.text
            elif 'xmin' in elem.tag:
                xmin=int(elem.text)
            elif 'ymin' in elem.tag:
                ymin=int(elem.text)
            elif 'xmax' in elem.tag:
                xmax=int(elem.text)
            elif 'ymax' in elem.tag:
                ymax=int(elem.text)
                
                dataset['file'].append(filename)
                dataset['classnames'].append(classname)
                dataset['width'].append(width)
                dataset['height'].append(height)
                dataset['xmin'].append(xmin)
                dataset['ymin'].append(ymin)
                dataset['xmax'].append(xmax)
                dataset['ymax'].append(ymax)

    for i, v in enumerate(dataset['classnames']):
        dataset['class_id'].append(classes.index(dataset['classnames'][i]))

    return pd.DataFrame(dataset)