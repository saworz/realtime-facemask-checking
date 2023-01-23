import torch
from pathlib import Path
from PIL import Image
import numpy as np

def image_mode(image_path: str, model: torch.nn.Module):
    
    results = model(Path(image_path))
    image = Image.fromarray(np.uint8(np.squeeze(results.render())))
    image.show()
