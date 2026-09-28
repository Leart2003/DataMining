import kagglehub
import os



path = kagglehub.dataset_download("dhoogla/unswnb15")

print("Path to dataset files:", path)

print(os.listdir(path))