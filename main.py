import kagglehub
import os
import pandas as pd



path = kagglehub.dataset_download("dhoogla/unswnb15")

print("Path to dataset files:", path)

print(os.listdir(path))
#Lokacioni datasetave
train_path = os.path.join(path, "UNSW_NB15_training-set.parquet")
test_path = os.path.join(path, "UNSW_NB15_testing-set.parquet")

train_df = pd.read_parquet(train_path)
test_df = pd.read_parquet(test_path)

print(train_df)
print(test_df)