from pandas.io.parsers import TextFileReader
import pandas as pd

from .config import settings


def fetch_phish_data() -> TextFileReader:
    return pd.read_csv(
        settings.data_source,
        storage_options={"User-Agent": f"phishtank/{settings.phishtank_username}"},
        usecols=["phish_id", "url", "phish_detail_url", "submission_time"],
        parse_dates=["submission_time"],
        skip_blank_lines=True,
        iterator=True,
        chunksize=500,
    )


def get_data_source():
    use_local_file = False
    if use_local_file:
        path = "./verified_online.csv"
        headers = {}
    else:
        path = "http://data.phishtank.com/data/online-valid.csv"
        headers = {"User-Agent": "y2k"}
    return path, headers
