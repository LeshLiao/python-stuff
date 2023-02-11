import os
import pandas as pd
import glob
import time

# 訂單索引值名稱
indexColumnName = "甘仔店料號"

# 對照表檔名
tableExcelName = "出貨料號對照.xlsx"

# 訂單資料夾名稱
orderFolderName = "orders"

def combine_all_order():
    path = os.getcwd() + "\\" + orderFolderName
    files = glob.glob(os.path.join(path, "*.xlsx"))
    
    # create an Empty DataFrame object
    dataFrame = pd.DataFrame()  

    # loop over the list of excel files
    for f in files:
        print('Read excel:', f)
        one_order = pd.read_excel(f)
        dataFrame = pd.concat([dataFrame, one_order]) 

    dataFrame = dataFrame.reset_index()
    dataFrame.drop('index', inplace=True, axis=1)
    return dataFrame

def getMappingDataFrame(allOrders, columnName):
    # create an Empty DataFrame object
    df = pd.DataFrame()
    for index, row in allOrders.iterrows():
        rowData = tableExcel.loc[tableExcel[columnName] == row[columnName]]
        df = pd.concat([df,rowData])  

    df = df.reset_index()
    df.drop('index', inplace=True, axis=1)
    return df

def exportExcel(dataFrame):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    outputName = "output_" + timestr +".xlsx"
    dataFrame.to_excel(outputName)
    print("output:" + os.getcwd() + "\\" + outputName)

# 結合所有訂單
all_orders = combine_all_order()

# 讀取對照表
tableExcel = pd.read_excel(tableExcelName)

# 進行比對並產生結果
result = getMappingDataFrame(all_orders, indexColumnName)

# 將結果合併到"所有訂單"
all_orders = all_orders.join(result, lsuffix="", rsuffix="_new")

# 例出合併後的內容
print(all_orders)

# 匯出Excel檔案
exportExcel(all_orders)
