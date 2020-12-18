"""
Heru Handika
16 December 2020
Match iTru with index sequence. 
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
        """
        Generate path for processing. 
        The function concat the folder name with the filename.
        """
        if new_path is not None:
            return new_path + '/' + filenames
        else:
            return self.path + '/' + filenames

    def read_csv(self) -> pd.DataFrame:
        """
        Read csv file from user defined path.
        Then, trim whitespace before returning
        the dataframe.
        """
        csv_file = self._get_path(self.filenames)
        df = pd.read_csv(csv_file)
        df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
        return df
    
    def _write_csv(self, df: pd.DataFrame, path: str) -> None:
        """
        Save to csv and print the filename and location
        on console.
        """
        df.to_csv(path, index=False)
        print(f'File is saved as {path}.') 

    def write_file(self,  df: pd.DataFrame, new_path: str=None) -> None:
        """
        Control writing files. It allows users to assign 
        new folder to write the file.
        """
        path = self._get_path(self.filenames)
        self._write_csv(df, path)

        if new_path is not None:
            try:
                path = self._get_path(self.filenames, new_path)
                self._write_csv(df, path)
            except FileNotFoundError:
                os.mkdir(new_path)
                print(f'A new folder is created. File path: {new_path}/')
                path = self._get_path(self.filenames, new_path)
                self._write_csv(df, path)
                 

class Matcher:
    def __init__(self, sample_df: pd.DataFrame, \
                itru5: pd.DataFrame, \
                itru7: pd.DataFrame) -> None:
        self.sample_df = sample_df
        self.itru5 = itru5
        self.itru7 = itru7

    def _split_df(self, column_names: List[str]) -> pd.DataFrame:
        """
        Split the input file to match each iTru index with its
        sequences.
        """
        sample_df = self.sample_df[column_names]
        return sample_df

    def _match_i5(self, sample_i5: pd.DataFrame) -> pd.DataFrame:
        return sample_i5.merge(self.itru5, on='i5', how='left')

    def _match_i7(self, sample_i7: pd.DataFrame) -> pd.DataFrame:
        return sample_i7.merge(self.itru7, on='i7', how='left')

    def match_all(self, i5_cols: List[str], i7_cols: List[str]) -> pd.DataFrame:
        """
        This function first splits the sample dataframe to each iTru index.
        Then, match each index with its sequence.
        Later, combined the two dataframe to generate the final dataframe.
        The write_file function in the IO class responsible for writing the
        final dataframe into a csv file.
        """
        sample_i5 = self._split_df(i5_cols)
        sample_i7 = self._split_df(i7_cols)
        matched_i5 = self._match_i5(sample_i5)
        matched_i7 = self._match_i7(sample_i7)
        return matched_i5.merge(matched_i7, on='TubeNo', how='left')

def main():
    fpath = 'data'
    sample = IO(fpath, 'sample.csv').read_csv()
    itru5 = IO(fpath, 'i5seq.csv').read_csv()
    itru7 = IO(fpath, 'i7seq.csv').read_csv()
    i5_cols = ['TubeNo', 'i5']
    i7_cols = ['TubeNo', 'i7']
    final_df = Matcher(sample, itru5, itru7)\
                    .match_all(i5_cols, i7_cols)
    IO(fpath, 'result_iTru_index.csv').write_file(final_df)

if __name__ == "__main__":
    main()
