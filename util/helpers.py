import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """
    Load data from CSV into a DataFrame.

    Args:
    - filepath (str): Path to the CSV file.

    Returns:
    - DataFrame: Loaded data.
    """
    return pd.read_csv(filepath)

def data_overview(df):
    """
    Provide a basic overview of the data.

    Args:
    - df (DataFrame): Data to overview.

    Returns:
    - None
    """
    print("Data Head:")
    print(df.head())
    print("\nData Info:")
    print(df.info())
    print("\nData Description:")
    print(df.describe())

def plot_distribution(df, column):
    """
    Plot the distribution of a specified column.

    Args:
    - df (DataFrame): Data to plot from.
    - column (str): Column name.

    Returns:
    - None
    """
    sns.histplot(df[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

def handle_missing_values(df, strategy="mean"):
    """
    Handle missing values in the DataFrame.

    Args:
    - df (DataFrame): Data with potential missing values.
    - strategy (str): Strategy to handle missing values. Supported values: "mean", "median", "drop".

    Returns:
    - DataFrame: Data after handling missing values.
    """
    if strategy == "mean":
        return df.fillna(df.mean())
    elif strategy == "median":
        return df.fillna(df.median())
    elif strategy == "drop":
        return df.dropna()
    else:
        raise ValueError("Unsupported strategy. Supported values are: 'mean', 'median', 'drop'.")

# You can add more helper functions as needed.
