import pandas as pd


def load_data(file_path):
    """
    Load dataset safely.
    """

    try:
        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError(
                "Dataset is empty."
            )

        return df

    except FileNotFoundError:
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )


def remove_duplicates(df):
    """
    Remove duplicate rows.
    """

    return df.drop_duplicates()


def handle_missing_values(df):
    """
    Fill missing values.
    """

    for column in df.columns:

        if df[column].dtype == "object":
            df[column] = df[column].fillna(
                df[column].mode()[0]
            )

        else:
            df[column] = df[column].fillna(
                df[column].median()
            )

    return df