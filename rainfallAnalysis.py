import numpy as np

#region Task 01
def convertNumpyArray(aList):
    numpyArray = np.array2string(np.array(aList), separator=",")
    print(f"Convert List to NumPy Array: {numpyArray}")
#endregion

#region Task 02
def totalRainfall(anArray):
    sum = np.sum(anArray)
    print(f"Total rainfall for the week: {sum:.2f}")
#endregion

#region Task 03
def averageRainfall(anArray):
    avg = np.average(anArray)
    print(f"Average rainfall for the week: {avg:.2f}")
#endregion

#region Task 04
def countRainfall(anArray):
    count = np.count_nonzero(anArray == 0)
    print(f"Days had no rain: {count}")
#endregion

#region Task 05
def indicesRainfall(anArray):
    indexRain = np.where(anArray > 5)[0]
    print(f"Days where the rainfall was more than 5 mm: {indexRain}", end=" ")
#endregion

#region Task 06
def percentileRainfall(anArray):
    percentile75 = np.percentile(anArray, 75)
    print(f"\n75th percentile of rainfall data: {percentile75:.2f}")

    avobe75 = anArray[anArray > percentile75]
    print(f"More than 75th percentile rainfall data: {avobe75}")
#endregion

if __name__ == "__main__":
    rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
    convertNumpyArray(rainfall)



    rainfallArray = np.array(rainfall)
    totalRainfall(rainfallArray)
    averageRainfall(rainfallArray)
    countRainfall(rainfallArray)
    indicesRainfall(rainfallArray)
    percentileRainfall(rainfallArray)