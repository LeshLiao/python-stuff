import os
import pandas as pd
import glob
import time

# in the folder
path = os.getcwd() + "\orders"
print(path)
files = glob.glob(os.path.join(path, "*.xlsx"))

# create an Empty DataFrame object
all_orders = pd.DataFrame()      
  
# loop over the list of csv files
for f in files:
    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])
    one_order = pd.read_excel(f)
    all_orders = pd.concat([all_orders,one_order]) 

print("all_orders===================================================")
all_orders = all_orders.reset_index()
all_orders.drop('index', inplace=True, axis=1)
print(all_orders)

mappingTable = pd.read_excel("出貨料號對照.xlsx")

print("===================================================")

# create an Empty DataFrame object
df = pd.DataFrame()


for index, row in all_orders.iterrows():
    #print(row['甘仔店料號'])
    newDf = mappingTable.loc[mappingTable['甘仔店料號'] == row['甘仔店料號']]

    df = pd.concat([df,newDf])  
    


print("===================================================")
df = df.reset_index()
print(df)
print("===================================================")



#df.drop('甘仔店料號', inplace=True, axis=1)
df.drop('index', inplace=True, axis=1)

print(df)
print("===================================================")
all_orders = all_orders.join(df, lsuffix="", rsuffix="_new")
print(all_orders)

print("===================================================")


timestr = time.strftime("%Y%m%d-%H%M%S")
outputName = "output_" + timestr +".xlsx"
all_orders.to_excel(outputName)
print("output:" + os.getcwd() + "\\" + outputName)
