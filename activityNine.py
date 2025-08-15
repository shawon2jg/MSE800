class FileProcessing:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        file = open(self.file_path, "r", encoding="utf-8", errors="ignore")
        data = file.read()
        file.close()
        return data

    def write_file(self, data):
        file = open(self.file_path, "w", encoding="utf-8", errors="ignore")
        file.write(data)
        file.close()
        print("Data written successfully.")


if __name__ == "__main__":
    obj_file_pro = FileProcessing(
        "F:\Master of Software Engineering (Level 9)\Trimester 01\MSE800 Professional Software Engineering\Week 03\Class_05_16082025\demo_file.txt")

    read_file = obj_file_pro.read_file(obj_file_pro)

    word_count = 0
    given_file = "F:\Master of Software Engineering (Level 9)\Trimester 01\MSE800 Professional Software Engineering\Week 03\Class_05_16082025\demo_file.txt"

    with open(given_file, "r", encoding="utf-8", errors="ignore") as givenfile:
        for fileline in givenfile:
            line = fileline.rstrip()
            word_count += len(line.split())

    print("Total number of words: ", word_count)