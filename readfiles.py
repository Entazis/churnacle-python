

def readFiles(data_path):
    import pandas as pd

    print("reading central...")
    central_users = pd.read_json(data_path+"users_central.json", lines=True)
    central_users.to_hdf(data_path+"store.hd5", "central", mode='w', table=True)

    print("reading orange...")
    orange_users = pd.read_json(data_path+"users_orange.json", lines=True)
    orange_users.to_hdf(data_path + "store.hd5", "orange", mode='a', table=True)

    return 0