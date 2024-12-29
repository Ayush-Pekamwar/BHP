import json , pickle
import numpy as np
import os

__data_columns = None
__locations = None
__model = None

def load_saved_artifacts():
    print('loading saved artifacts...')

    global __data_columns
    global __locations
    global __model

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'artifacts', 'columns.json')

    with open(file_path,'r') as f:
       __data_columns =  json.load(f)['data_columns']
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'artifacts', 'banglore_home_prices_model.pickle')
    with open(file_path,'rb') as f:
        __model = pickle.load(f)

    __locations = __data_columns[3:]

    print('loading artifacts done...')


def get_location_names():
    # print(__name__)
    return __locations


def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_idx = __locations.index(location.lower())
    except:
        loc_idx = -1
    
    X = np.zeros(len(__data_columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_idx >= 3:
        X[loc_idx] = 1

    predicted_price = __model.predict([X])[0]
    predicted_price = round(predicted_price,2)

    return predicted_price



if __name__ == '__main__' or 'util':
    load_saved_artifacts()
    #------------testing------------
    # print(get_location_names())
    # print(get_estimated_price('1st phase jp nagar' , 1000 , 1,1))
    # print(get_estimated_price('1st phase jp nagar' , 1000 , 2,2))
    # print(get_estimated_price('1st phase jp nagar' , 2000 , 4,4))



