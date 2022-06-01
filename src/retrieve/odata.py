from utils.get_raw_data import retrieve_table

# names of tables to retrieve
odata_tables = [

    'KNS_MkSiteCode',
    'KNS_Faction',
    'KNS_Person',
    'KNS_Position',
    'KNS_PersonToPosition',
    'KNS_KnessetDates',
    'KNS_Status',
    'KNS_Bill',
    'KNS_BillInitiator',
    'KNS_BillHistoryInitiator',
    'KNS_ItemType',
]

def retrieve_raw_data():
    """
    Retrieve raw data from OData.
    """
    for i in range(len(odata_tables)):
        retrieve_table(odata_tables[i])