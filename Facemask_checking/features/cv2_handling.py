import cv2
import torch
import numpy as np
from typing import Union

def cv2_handling(mode: Union[int, str], model: torch.nn.Module):

    
    cap = cv2.VideoCapture(mode)

    assert cap.isOpened()
    while(cap.isOpened()):
        ret, frame = cap.read()
        assert not isinstance(frame,type(None)), 'frame not found'
        results = model(frame)
        
        cv2.imshow('YOLO', np.squeeze(results.render()))
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()