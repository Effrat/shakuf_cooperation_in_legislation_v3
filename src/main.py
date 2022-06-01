# TODO: user feedbacks (printouts) for for all modules: conformity, coherence.

from folders_structure.create_folders import create_required_folders
from retrieve.odata import retrieve_raw_data
from format.csv_to_json import csv_to_writable_json


def update_data():
    """
    Updates the raw source data and transforms it as necessary, to create tables for the front-end data model.
    """
    # # ----- step 0 -----
    # create_required_folders()
    # retrieve_raw_data()
    
    # # ----- step 1 -----
    # PowerBI - manual export to CSVs

    # # ----- step 2 -----
    # csv_to_writable_json()

    # # ----- step 3 -----
    # manual copy + paste from both jsons to writables data stores



 


if __name__ == '__main__':
    update_data()
   
    # print('Data update complete.')