
import pandas as pd
from pandas import DataFrame

class update:
    def __init__(self, filepath: str)-> None:
        self.filepath = filepath
    def updating(self):
        try:
            dataframe = pd.read_csv(self.filepath)
            length_dataframe = len(dataframe)

            row_counter = length_dataframe + 1 # this will increase/update the dataframe
            for col in dataframe.columns:
                input_string : str = input(f'Enter {col}: ')
                # update the dataframe
                dataframe[col][row_counter] = input_string
                #dataframe[col][row_counter] = input_string
            # adding the sample
            dataframe.to_csv("updated_sample.csv", index=False, header=True)

        except Exception as e:
            raise e


# This should be used for updating the sample

if __name__ == "__main__":
    file_path = "job_oversikt.csv"
    up = update(filepath=file_path)
    up.updating()