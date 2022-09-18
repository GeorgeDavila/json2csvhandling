import requests
import json
import pandas as pd
import numpy as np
import csv
#np.std(a)

csvDataFile = "carrierInfo2.csv"

df = pd.read_csv(csvDataFile)

#Test 
#print(df.iloc[0][0])
dataRow0 = str( df.iloc[0][0] ).replace("\'","\"").replace("None","0") #can't have single quotes or None's in there 
y = json.loads( dataRow0 )
print( y["allowedToOperate"] )

print(df["data"][1])

def getPropertyList(property2extract, turn2integer=False):
    #e.g. property2extract = "bipdInsuranceOnFile" or  property2extract = "allowedToOperate"
    #Make turn2integer=True to make the output an integer 
    propertyList = []

    for ii in range(len(df)):
        try: #Some datapoints (like those that include single quote in company name ) are hard to structure so we ignore those by passing them in except 
            #print(ii)
            dataRow_ii = str( df["data"][ii] ).replace("\'","\"").replace("None","0") #can't have single quotes or None's in there 
            y_ii = json.loads( dataRow_ii )
            
            property2extractVALUE = y_ii[property2extract]
            if turn2integer:
                property2extractVALUE = int( property2extractVALUE )
            
            propertyList.append( property2extractVALUE )
        except:
            pass

    return propertyList

def removeZeroesFromList(listInput):
    return [x for x in listInput if x != 0]

bipdInsuranceOnFile_DataList = getPropertyList(property2extract="bipdInsuranceOnFile", turn2integer=True)
print(bipdInsuranceOnFile_DataList)
print("Number of entries: ", len(bipdInsuranceOnFile_DataList), " Mean: ", np.average(bipdInsuranceOnFile_DataList), " Standard Deviation: ", np.std(bipdInsuranceOnFile_DataList))

bipdInsuranceOnFile_DataList_NoZeroes = removeZeroesFromList(bipdInsuranceOnFile_DataList)
print(bipdInsuranceOnFile_DataList_NoZeroes)
print("Number of entries: ", len(bipdInsuranceOnFile_DataList_NoZeroes), " Mean: ", np.average(bipdInsuranceOnFile_DataList_NoZeroes), " Standard Deviation: ", np.std(bipdInsuranceOnFile_DataList_NoZeroes))


'''
def rowLocationMethod_getPropertyList(property2extract):
    #This method parses the csv by raw locaation 
    #e.g. property2extract = "bipdInsuranceOnFile" or  property2extract = "allowedToOperate"
    propertyList = []

    for ii in range(len(df)):
        try:
            #print(ii)
            dataRow_ii = str( df.iloc[ii][0] ).replace("\'","\"").replace("None","0") #can't have single quotes or None's in there 
            y_ii = json.loads( dataRow_ii )

            propertyList.append( y_ii[property2extract] )
        except:
            pass

    return propertyList

print(rowLocationMethod_getPropertyList(property2extract="bipdInsuranceOnFile"))

#Check that both functions are equivalent (returns true, as expected )
#print( getPropertyList(property2extract="bipdInsuranceOnFile") == rowLocationMethod_getPropertyList(property2extract="bipdInsuranceOnFile") )
'''