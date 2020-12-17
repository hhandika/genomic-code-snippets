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
import pandas as pd


class IO:
    def __init__(self, path, filenames) -> None:
        self.path = path
        self.filenames = filenames

    def _get_path(self, filenames, new_path=None):
        if new_path is not None:
            return new_path + '/' + filenames
        else:
            return self.path + '/' + filenames

    def read_csv(self):
        """
        
        """
        csv_file = self._get_path(self.filenames)
        df = pd.read_csv(csv_file)
        return df
    
    def _write_file(self, df, path) -> None:
        df.to_csv(path, index=False)
        print(f'File is saved as {path}.') 

    def write_csv(self,  df, new_path=None):
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
    def __init__(self, sample_i5, itru5, sample_i7, itru7):
        self.sample_i5 = sample_i5
        self.sample_i7 = sample_i7
        self.itru5 = itru5
        self.itru7 = itru7

    def _match_i5(self):
        return self.sample_i5.merge(self.itru5, on='i5', how='left')

    def _match_i7(self):
        return self.sample_i7.merge(self.itru7, on='i7', how='left')

    def match_all(self):
        matched_i5 = self._match_i5()
        matched_i7 = self._match_i7()
        return matched_i5.merge(matched_i7, on='TubeNo', how='left')

def main():
    fpath = 'data'
    sample_i5 = IO(fpath, 'samplei5.csv').read_csv()
    sample_i7 = IO(fpath, 'samplei7.csv').read_csv()
    itru5 = IO(fpath, 'i5Index.csv').read_csv()
    itru7 = IO(fpath, 'i7Index.csv').read_csv()
    final_df = Matcher(sample_i5, itru5, \
                        sample_i7, itru7)\
                        .match_all()
    IO(fpath, 'result_iTru_index.csv').write_csv(final_df)

if __name__ == "__main__":
    main()