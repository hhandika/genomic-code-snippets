"""
Heru Handika
16 December 2020
Match iTru with index sequence.

You can run this code on VS code.
Run Below button will show up. Click it 
to run the code. Otherwise, run it just like 
any other python script. 
"""
# %%
import os
from typing import List

import pandas as pd


class IO:
    def __init__(self, path: str, filenames: str) -> None:
        self.path = path
        self.filenames = filenames

    def _get_path(self, filenames: str, new_path: str=None) -> str:
        if new_path is not None:
            return new_path + '/' + filenames
        else:
            return self.path + '/' + filenames

    def read_csv(self) -> pd.DataFrame:
        """
        
        """
        csv_file = self._get_path(self.filenames)
        df = pd.read_csv(csv_file)
        return df
    
    def _write_file(self, df: pd.DataFrame, path: str) -> None:
        df.to_csv(path, index=False)
        print(f'File is saved as {path}.') 

    def write_csv(self,  df: pd.DataFrame, new_path: str=None) -> None:
        """
        Save pandas's dataframe to csv.
        """
        path = self._get_path(self.filenames)
        self._write_file(df, path)

        if new_path is not None:
            try:
                path = self._get_path(self.filenames, new_path)
                self._write_file(df, path)
            except FileNotFoundError:
                os.mkdir(new_path)
                print(f'A new folder is created. File path: {new_path}/')
                path = self._get_path(self.filenames, new_path)
                self._write_file(df, path)
                 

class Matcher:
    def __init__(self, sample_df: pd.DataFrame, \
                itru5: pd.DataFrame, \
                itru7: pd.DataFrame) -> None:
        self.sample_df = sample_df
        self.itru5 = itru5
        self.itru7 = itru7

    def _split_df(self, column_names: List[str]) -> pd.DataFrame:
        sample_df = self.sample_df[column_names]
        return sample_df

    def _match_i5(self, sample_i5: pd.DataFrame) -> pd.DataFrame:
        return sample_i5.merge(self.itru5, on='i5', how='left')

    def _match_i7(self, sample_i7: pd.DataFrame) -> pd.DataFrame:
        return sample_i7.merge(self.itru7, on='i7', how='left')

    def match_all(self, i5_cols: List[str], i7_cols: List[str]) -> pd.DataFrame:
        sample_i5 = self._split_df(i5_cols)
        sample_i7 = self._split_df(i7_cols)
        matched_i5 = self._match_i5(sample_i5)
        matched_i7 = self._match_i7(sample_i7)
        return matched_i5.merge(matched_i7, on='TubeNo', how='left')

def main():
    fpath = 'data'
    sample_i5 = IO(fpath, 'sample.csv').read_csv()
    # sample_i7 = IO(fpath, 'samplei7.csv').read_csv()
    itru5 = IO(fpath, 'i5Index.csv').read_csv()
    itru7 = IO(fpath, 'i7Index.csv').read_csv()
    i5_cols = ['TubeNo', 'i5']
    i7_cols = ['TubeNo', 'i7']
    final_df = Matcher(sample_i5, itru5, itru7)\
                    .match_all(i5_cols, i7_cols)
    IO(fpath, 'test_iTru_index.csv').write_csv(final_df)

if __name__ == "__main__":
    main()