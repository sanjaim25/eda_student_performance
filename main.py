"""Main script to load and preview student data"""
import pandas as pd

df = pd.read_csv('data/student_data.csv')
print("Dataset Preview:")
print(df.head())
print("\nDataset Info:")
print(df.info())
