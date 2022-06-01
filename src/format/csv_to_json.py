import pandas as pd


def csv_to_json():
    """
    Converts the CSV files to a writable JSON file.
    """
    bill_sponsors = pd.read_csv('../../data/exported from PBI/bill_sponsors.csv')
    bill_sponsors.to_json('../../data/json/bill_sponsors.json', orient='records')

    faction = pd.read_csv('../../data/exported from PBI/faction.csv')
    faction.to_json('../../data/json/faction.json', orient='records')