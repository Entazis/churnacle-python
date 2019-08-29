
def churnacle():

    data_path = "./"
    # data_path = "/usr/src/churnVolume/"

    import sklearn
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import statsmodels.formula.api as sm
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    import tables

    import readfiles
    import preparedata
    import trainmodel
    import predictchurn

    prog_start = datetime.now()

    read_start = datetime.now()
    #readfiles.readFiles(data_path)
    read_end = datetime.now()

    prepare_start = datetime.now()
    user_next_all = preparedata.prepareData(data_path)
    prepare_end = datetime.now()

    train_start = datetime.now()
    #trainModel()
    train_end = datetime.now()

    predict_start = datetime.now()
    #predictChurn()
    predict_end = datetime.now()

    prog_end = datetime.now()

    #churnlist
    #a_b_test grouping
    #slack

churnacle()