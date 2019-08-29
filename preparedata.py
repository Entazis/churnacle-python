
def prepareData(data_path):
    import processcentral
    import processorange
    import pandas as pd

    central_users = pd.read_hdf(data_path+"store.hd5", "central")
    orange_users = pd.read_hdf(data_path+"store.hd5", "orange")

    user_next = pd.DataFrame()

    print("central preparing...")
    for index, user in central_users.iterrows():
        if (index % 100 == 0):
            print("central processing index: "+ str(index))
        user_next = user_next.append(processcentral.processCentral(user))
    user_next.to_hdf(data_path + "store.hd5", "user_next", mode='a', table=True)

    #TODO: remove admin, isadmin
    #TODO: keep: personalData.email, badges, grepl "submissions"
    #TODO: join user_next with orange_users_p
    #TODO: remove duplicated ("email", "period")
    #TODO: collect assignment names, lessonHashes, lessonCnt, assignmentCnt

    #TODO
    print("orange preparing...")


    return 0
