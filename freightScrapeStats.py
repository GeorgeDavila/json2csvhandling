import requests
import json
import pandas as pd
import numpy as np
import csv


def getPropertyList(SourcecsvDataFileName, property2extract, turn2integer=False):
    #e.g. property2extract = "bipdInsuranceOnFile" or  property2extract = "allowedToOperate"
    #Make turn2integer=True to make the output an integer 
    csvDataFile = SourcecsvDataFileName

    df = pd.read_csv(csvDataFile)
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

bipdInsuranceOnFile_DataList = getPropertyList(SourcecsvDataFileName= "carrierInfo2.csv", property2extract="bipdInsuranceOnFile", turn2integer=True)
print(bipdInsuranceOnFile_DataList)
print("Number of entries: ", len(bipdInsuranceOnFile_DataList), " Mean: ", np.average(bipdInsuranceOnFile_DataList), " Standard Deviation: ", np.std(bipdInsuranceOnFile_DataList))

bipdInsuranceOnFile_DataList_NoZeroes = removeZeroesFromList(bipdInsuranceOnFile_DataList)
print(bipdInsuranceOnFile_DataList_NoZeroes)
print("Number of entries: ", len(bipdInsuranceOnFile_DataList_NoZeroes), " Mean: ", np.average(bipdInsuranceOnFile_DataList_NoZeroes), " Standard Deviation: ", np.std(bipdInsuranceOnFile_DataList_NoZeroes))



def convertLists2CSVcolumns():
    import csv

    source_csvDataFile = "carrierInfo2.csv"
    target_csvDataFile = "carrierInfo2-cleaned.csv"

    colsOfPropertyNames = [
        "dotNumber", 
        "legalName", 
        "allowedToOperate", 
        "phyStreet", 
        "phyCity", 
        "phyState", 
        "phyZipcode", 
        "vehicleOosRate", 
        "cargoInsuranceOnFile", 
        "bipdInsuranceOnFile"
        ]

    
    #https://appdividend.com/2020/12/10/how-to-convert-python-list-to-csv-file/
    dataArray = []
    
    for jj in colsOfPropertyNames:
        dataArray.append( getPropertyList(SourcecsvDataFileName= source_csvDataFile, property2extract=jj) )

        #rows[jj][kk] = getPropertyList(SourcecsvDataFileName= source_csvDataFile, property2extract=jj)[kk]

    '''rows = []
    for jj in colsOfPropertyNames:
        for kk in range(len(dataArray[jj])):
            rows[jj][kk] = dataArray[jj][kk]'''

    '''
    rows = [ 
        [getPropertyList(0)[0], getPropertyList(1)[0], ....],
        [getPropertyList(0)[1], getPropertyList(1)[1], ....],
        ...., 
        [getPropertyList(0)[kk], getPropertyList(1)[kk], ....] 
    ]
    '''

    with open(target_csvDataFile, 'w', newline='') as f:

        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerow(colsOfPropertyNames)
        #write.writerows(rows)

        #for jj in range(len(colsOfPropertyNames)): 
        #    row2add = [ dataArray[jj][kk] for jj in range(len(colsOfPropertyNames)) ]

        for jj in range(len(colsOfPropertyNames)):

            #row2add = [ dataArray[0][kk] ] 
            for kk in range(len(dataArray[0])):
                write.writerow( 
                    [   
                        dataArray[0][kk] ,
                        dataArray[1][kk] ,
                        dataArray[2][kk] ,
                        dataArray[3][kk] ,
                        dataArray[4][kk] ,
                        dataArray[5][kk] ,
                        dataArray[6][kk] ,
                        dataArray[7][kk] ,
                        dataArray[8][kk] ,
                        dataArray[9][kk]
                        ] )
    
    '''for jj in colsOfPropertyNames:
        dict = {jj: getPropertyList(SourcecsvDataFileName= source_csvDataFile, property2extract=jj)}

    df = pd.DataFrame(dict)

    df.to_csv('shows.csv')'''

convertLists2CSVcolumns()

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