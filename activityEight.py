
def data_processing(self):
    infile = open("F:\Master of Software Engineering (Level 9)\Trimester 01\MSE800 Professional Software Engineering\Week 03\Class_05_16082025\demo_file.txt")

    mean_temps = []
    for line in infile:
        data = line.split(",")
        mean_temp = float(data[3])
        mean_temps.append(mean_temp)
    print(max(mean_temps))
    infile.close()

if __name__ == "__main__":
    # data_processing()
    word_count = 0
    given_file = "F:\Master of Software Engineering (Level 9)\Trimester 01\MSE800 Professional Software Engineering\Week 03\Class_05_16082025\demo_file.txt"

    with open(open(given_file, "r", encoding="utf-8", errors="ignore") as givenfile:
        for fileline in givenfile:
            word_count += len(fileline.split())

    print("Total number of words: ", word_count)