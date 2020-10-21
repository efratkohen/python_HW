import numpy as np
import pathlib

def load_data(fname: str):
    """ Load and return an '.npy' file """
    b=np.load(fname)
    return b

def find_in_range(data: np.ndarray, num_range: tuple=(0.3, 0.4)):
    """ Return an array containing the values of 'data' that are inside 'num_range' """
    data = data[ (data > 0.3) & (data < 0.4) ]
    return data

def first_after_val(data: np.ndarray, val: float=0.9) -> np.ndarray:
    """ Return the position of the first value larger than val """
    result = np.where(data > val)
    listOfCoordinates= list(zip(result[0], result[1], result[2], result[3]))
    return(listOfCoordinates[0])
