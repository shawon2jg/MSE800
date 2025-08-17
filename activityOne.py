import numpy as np

#region Task 01
def averageTemperature(anArray):
    avgTemp = np.average(anArray)
    print(f"Average temperature: {avgTemp:.2f}")
#endregion

#region Task 02
def maxMinTemperature(anArray):
    maxTemp = np.max(anArray)
    print(f"Maximum temperature: {maxTemp}")

    minTemp = np.min(anArray)
    print(f"Minimum temperature: {minTemp}")
#endregion

#region Task 03
def convertTemperature(anArray):
    fahrenTemp = (anArray * 9/5) + 32
    print(f"Converted from Celsius to Fahrenheit: {fahrenTemp}")
#endregion

#region Task 04
def indicesTemperature(anArray):
    indexTemp = np.where(anArray >= 20)[0]
    print(f"\nIndices where temperature exceeded 20°C: {indexTemp}", end=" ")
#endregion

if __name__ == "__main__":
    temperatureArray = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    averageTemperature(temperatureArray)
    maxMinTemperature(temperatureArray)
    convertTemperature(temperatureArray)
    indicesTemperature(temperatureArray)