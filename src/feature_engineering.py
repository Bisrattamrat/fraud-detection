import pandas as pd


def create_time_features(df):

    df["signup_time"] = pd.to_datetime(
        df["signup_time"]
    )

    df["purchase_time"] = pd.to_datetime(
        df["purchase_time"]
    )

    df["time_since_signup"] = (
        df["purchase_time"]
        - df["signup_time"]
    ).dt.total_seconds()

    df["hour_of_day"] = (
        df["purchase_time"]
        .dt.hour
    )

    df["day_of_week"] = (
        df["purchase_time"]
        .dt.dayofweek
    )

    return df


def transaction_frequency(df):

    freq = (
        df.groupby("user_id")
        .size()
        .reset_index(name="transaction_count")
    )

    df = df.merge(
        freq,
        on="user_id",
        how="left"
    )

    return df