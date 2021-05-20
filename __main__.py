import os
from datetime import datetime

import pyarrow as pa
import pyarrow.csv as csv
from pandas.core.frame import DataFrame


def main():
    """Main entry point for the application"""

    # Iterate through directory
    for subdir, dirs, files in os.walk("TestData"):

        # If we don't have any files, keep going.
        if files == []:
            continue

        # If we do, iterate the files
        for file in files:
            # Open the file
            filepath = subdir + os.sep + file
            df = read_csv(filepath)

            # Decide if we need to open or close a position
            # If Opening...
            # Get current tick
            # Calc Greeks
            # Select Strike
            # Log the Put

            # If Closing
            # Scan the df for a suitable exit
            # If found, log it and go to next tick to open a position
            # If not, go to next day

            # Print the path
            print("{} - {} - {}".format(datetime.now(), df.size, filepath))


def read_csv(filepath: str) -> DataFrame:
    """Reads a given csv filepath to Pandas Dataframe using Apache Arrow

    Args:
        filepath (str): CSV Filepath

    Returns:
        DataFrame: Resulting Dataframe
    """
    return csv.read_csv(
        filepath,
        convert_options=pa.csv.ConvertOptions(
            include_columns=[
                "Date",
                "TimeBarStart",
                "CallPut",
                "Strike",
                "ExpirationDate",
                "CloseAskPrice",
                "CloseBidPrice",
                "UnderCloseBidPrice",
            ]
        ),
    ).to_pandas()


if __name__ == "__main__":
    main()
