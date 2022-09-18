import requests
import json
import pandas as pd
import numpy as np
import csv


allKeys = ['allowedToOperate', 'bipdInsuranceOnFile', 'bipdInsuranceRequired', 'bipdRequiredAmount', 'bondInsuranceOnFile', 'bondInsuranceRequired', 'brokerAuthorityStatus', 'cargoInsuranceOnFile', 'cargoInsuranceRequired', 'censusTypeId', 'commonAuthorityStatus', 'contractAuthorityStatus', 'crashTotal', 'dbaName', 'dotNumber', 'driverInsp', 'driverOosInsp', 'driverOosRate', 'driverOosRateNationalAverage', 'ein', 'fatalCrash', 'hazmatInsp', 'hazmatOosInsp', 'hazmatOosRate', 'hazmatOosRateNationalAverage', 'injCrash', 'isPassengerCarrier', 'issScore', 'legalName', 'mcs150Outdated', 'oosDate', 'oosRateNationalAverageYear', 'phyCity', 'phyCountry', 'phyState', 'phyStreet', 'phyZipcode', 'reviewDate', 'reviewType', 'safetyRating', 'safetyRatingDate', 'safetyReviewDate', 'safetyReviewType', 'snapshotDate', 'statusCode', 'totalDrivers', 'totalPowerUnits', 'towawayCrash', 'vehicleInsp', 'vehicleOosInsp', 'vehicleOosRate', 'vehicleOosRateNationalAverage', 'carrierOperation.carrierOperationCode', 'carrierOperation.carrierOperationDesc']

source_csvDataFile = "carrierInfo2.csv"
target_csvDataFile = "carrierInfo2-cleaned2.csv"

#Erase previous data in this file before running script
#And add labels 
with open(target_csvDataFile, 'w', newline='') as f:
    writer = csv.writer(f)  # Note: writes lists, not dicts.
    writer.writerow( allKeys )


def saveDictDataAsCSV(dataDict):
    import csv

    with open(target_csvDataFile, 'a', newline='') as f:
        writer = csv.writer(f)  # Note: writes lists, not dicts.
        writer.writerow( [dataDict[jj] for jj in allKeys] )

def getRowDataAsDict(SourcecsvDataFileName, save2CSVoption=False, turn2integer=False):
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
            
            print(y_ii)
            #print(y_ii.keys())

            if save2CSVoption:
                saveDictDataAsCSV(y_ii)

        except:
            pass

    return propertyList


getRowDataAsDict(source_csvDataFile, save2CSVoption=True, turn2integer=False)


