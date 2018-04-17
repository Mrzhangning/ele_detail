#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pandas as pd

def get_shopid_list():
    df = pd.read_excel("/Users/apple/Desktop/ele_detail/pc_ele_20180326.xlsx",sheet_name="工作表1",header=None)
    return df.iloc[:,0].tolist()

