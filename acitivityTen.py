import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

class FileProcessing:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        content = pd.read_csv(self.file_path, sep=";")
        return content

    def write_file(self, data):
        table = pa.Table.from_pandas(data)
        parquet_file_path = "../data/AirQualityUCI.parquet"
        pq.write_table(table, parquet_file_path)
        print("Generate parquet file successfully.")

    def read_parquet_file(self):
        parquet_file_path = "../data/AirQualityUCI.parquet"
        content = pd.read_parquet(parquet_file_path)
        return content

if __name__ == "__main__":
    obj_file_process = FileProcessing("../data/AirQualityUCI.csv")
    content = obj_file_process.read_file()
    obj_file_process.write_file(content)

    pq_content =obj_file_process.read_parquet_file()
    # print(pq_content)
    s = pq_content.max().compute()
    print(s)