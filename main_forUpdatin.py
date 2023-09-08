
import pandas as pd
from pandas import DataFrame
from logger import logging
from datetime import datetime

class update:
    def __init__(self, filepath: str)-> None:
        self.filepath = filepath
        self.dict_ = {'Company_name': [], 'Cover_letter': [], 'Type':[], 'Resume':[], 'Date':[], 'Place':[], 'Announcement_found':[], 'Attest_added' : []}

    def updating(self):
        try:
            dataframe = pd.read_csv(self.filepath)
            print("<<<"*10)
            print("Last records of the dataframe looks as follows: ")
            if len(dataframe) > 0:
                print(dataframe.tail(1))
            print(">>>"*10)
            
            
            for num, col in enumerate(dataframe.columns):
                user_input : str = input(f"Enter {col}: ")
                if user_input == "DropLastRow":
                    dataframe.drop(dataframe.tail(1).index,inplace=True)
                    dataframe.to_csv(self.filepath, index=False, header=True)
                    if len(dataframe) > 0:
                        dataframe.tail(1)
                    print(f"No any records in the file path {self.filepath}")
                    break
                list(self.dict_.values())[num].append(user_input)
            # concat the old and new dataframe
            new_dataframe = pd.DataFrame(self.dict_)
            finla_dataframe = pd.concat([dataframe, new_dataframe])
            finla_dataframe.to_csv(self.filepath, index=False, header=True)
            logging.info(f"Updating the job database {datetime.now().date()}")

            # show user the added/updated rows
            updated_dataframe = pd.read_csv(self.filepath)
            print("\n")
            print("<<<"*10)
            print("The following recordes add to the dataframe")
            print(updated_dataframe.tail(1))
            print(">>>"*10)
        except Exception as e:
            raise e

# This should be used for updating the sample

if __name__ == "__main__":
    print("Infor: \n For deleting the last row, enter : 'DropLastRow' \n Otherwise just enter the job list that needed to be added")
    file_path = "job_oversikt.csv"
    up = update(filepath=file_path)
    up.updating()
