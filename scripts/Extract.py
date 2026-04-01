import pandas as pd

def extract_data(file_path, chunk_size=100000):
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        yield chunk