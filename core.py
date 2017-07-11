"""
@author lmiguelmh
@since 2017/07/09
"""
import pandas as pd


def read_volcano_csv():
    tdf = pd.read_csv("volerup.min.csv", sep=";",
                      # index_col="ID",
                      na_values=[""],
                      usecols=["ID", "DATE", "COUNTRY"])
    tdf = tdf.dropna()
    tdf['DATE'] = pd.to_datetime(tdf['DATE'], format='%Y/%m/%d', errors='coerce')
    return tdf


def read_tsunami_csv():
    tdf = pd.read_csv("tsevent.min.csv", sep=";",
                      # index_col="ID",
                      na_values=[""],
                      usecols=["ID", "DATE", "COUNTRY"])
    tdf = tdf.dropna()
    tdf['DATE'] = pd.to_datetime(tdf['DATE'], format='%Y/%m/%d', errors='coerce')
    return tdf


def read_country_csv():
    tdf = pd.read_csv("countries.csv", sep=";")
    tdf = tdf.dropna()
    return tdf
