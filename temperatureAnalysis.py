import numpy as np

tempArray = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

#region Task 01
avgTemp = np.average(tempArray)
print(f"Average temperature: {avgTemp:.2f}")
#endregion

#region Task 02
maxTemp = np.max(tempArray)
print(f"Maximum temperature: {maxTemp}")

minTemp = np.min(tempArray)
print(f"Minimum temperature: {minTemp}")
#endregion

#region Task 03
fahrenTemp = []
for celsiusTemp in tempArray:
    aTemp = celsiusTemp * 9/5 + 32
    fahrenTemp.append(aTemp)

print(f"Converted from Celsius to Fahrenheit: {fahrenTemp}", end=" ")
#endregion

#region Task 04
indexTemp = []
for i in range(0, len(tempArray)):
    indexPosition = 0
    if tempArray[i] >= 20:
        indexPosition = i
        indexTemp.append(indexPosition)

print(f"\nIndices where temperature exceeded 20°C: {indexTemp}", end=" ")
#endregion