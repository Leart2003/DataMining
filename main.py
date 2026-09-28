import kagglehub
import os
import pandas as pd



path = kagglehub.dataset_download("dhoogla/unswnb15")

print("Path to dataset files:", path)

print(os.listdir(path))

train_path = os.path.join(path, "UNSW_NB15_training-set.parquet")
test_path = os.path.join(path, "UNSW_NB15_testing-set.parquet")
