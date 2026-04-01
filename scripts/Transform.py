import pandas as pd
import re

INVALID_DATA = {"", "???", "??", "###", None, "N/A", "n/a"}
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    df["user_id"] = pd.to_numeric(df["user_id"].astype(str).str.replace(",", "").str.strip(), errors="coerce")
    df["transaction_id"] = pd.to_numeric(df["transaction_id"].astype(str).str.replace(",", "").str.strip(), errors="coerce")
    df = df.dropna(subset=["user_id", "transaction_id"])
    df = df.drop_duplicates(subset=["user_id", "transaction_id"])

    df["first_name"] = df["first_name"].fillna("").replace(INVALID_DATA, "")
    df["last_name"] = df["last_name"].fillna("").replace(INVALID_DATA, "")
    df["name"] = (df["first_name"].str.strip() + " " + df["last_name"].str.strip()).str.strip().str.lower()
    df = df[df["name"] != ""]

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df = df[df["age"] > 0]

    df["email"] = df["email"].astype(str).str.strip().str.lower()
    df = df[df["email"].str.match(EMAIL_REGEX, na=False)]

    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
    df["last_login"] = pd.to_datetime(df["last_login"], errors="coerce")
    df = df.dropna(subset=["signup_date", "last_login"])

    df["purchase_amount"] = pd.to_numeric(df["purchase_amount"], errors="coerce")
    df = df[df["purchase_amount"] > 0]

    df["country"] = df["country"].astype(str).str.lower().replace(INVALID_DATA, "unknown")
    df["city"] = df["city"].astype(str).str.lower().replace(INVALID_DATA, "unknown")

    df["is_active"] = df["is_active"].astype(str).str.strip().str.title()
    df = df[~df["is_active"].isin(INVALID_DATA)]
    df["is_active"] = df["is_active"].map({"True": True, "False": False})


    df["device"] = df["device"].astype(str).str.lower()
    df["device"] = df["device"].replace(INVALID_DATA, "unknown")

    df = df.drop(columns=["first_name", "last_name"])

    return df