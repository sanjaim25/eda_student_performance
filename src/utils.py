"""Utility functions for EDA"""

def check_nulls(df):
    """Check for null values in dataframe"""
    return df.isnull().sum()

def basic_stats(df):
    """Get basic statistics of dataframe"""
    return df.describe()
