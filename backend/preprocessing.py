import pandas as pd


def clean_dataset(data):

    data = data[~data["livingSpace"].str.contains(r".[A-Za-z]+.")]
    data = data[data["numberOfBedrooms"].str.contains(r"^\d{1,2}$")]
    data[["livingSpace"]] = data[["livingSpace"]].apply(lambda x: x.str.replace(',', '.'))
    data[["livingSpace", "numberOfBedrooms"]] = data[["livingSpace", "numberOfBedrooms"]].apply(pd.to_numeric)

    return data