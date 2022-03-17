import pickle
from google.cloud import storage
import sklearn
import numpy as np
import math

client = storage.Client()
bucket = client.get_bucket('ml-esme-real-estate-data')

blob = bucket.blob('model_bucket/model.pkl')
pickle_in = blob.download_as_string()
model = pickle.loads(pickle_in)

def get_prediction(nbr_pieces, surface, arrondissement):
    X = [[nbr_pieces,surface,arrondissement]]
    y = model.predict(X)
    y = np.expm1(y)
    y = math.ceil(y / 1000.0) * 1000
    return y


