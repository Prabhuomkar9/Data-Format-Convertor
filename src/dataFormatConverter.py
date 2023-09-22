import os
import pandas as pd
from enum import Enum


class FileType(Enum):
    csv = 1
    xlsx = 2
    json = 3


class FormatConvert:
    # define a function if same format
    @staticmethod
    def same_format(*pseudo: None) -> False:
        return False

    # define a function to convert CSV to JSON
    @staticmethod
    def csv_to_json(csv_path: str, json_path: str) -> True:
        # conversion code
        df = pd.read_csv(csv_path)
        df.to_json(json_path, orient="records")
        return True

    # define a function to convert JSON to CSV
    @staticmethod
    def json_to_csv(json_path: str, csv_path: str) -> True:
        # conversion code
        df = pd.read_json(json_path)
        df.to_csv(csv_path, index=False)
        return True

    # define a function to convert CSV to XLSX
    @staticmethod
    def csv_to_xlsx(csv_path: str, xlsx_path: str) -> True:
        # conversion code
        df = pd.read_csv(csv_path)
        df.to_excel(xlsx_path, index=False)
        return True

    # define a function to convert XLSX to CSV
    @staticmethod
    def xlsx_to_csv(xlsx_path: str, csv_path: str) -> True:
        # conversion code
        df = pd.read_excel(xlsx_path)
        df.to_csv(csv_path, index=False)
        return True

    # define a function to convert JSON to XLSX
    @staticmethod
    def json_to_xlsx(json_path: str, xlsx_path: str) -> True:
        # conversion code
        df = pd.read_json(json_path)
        df.to_excel(xlsx_path, index=False)
        return True

    # define a function to convert XLSX to JSON
    @staticmethod
    def xlsx_to_json(xlsx_path: str, json_path: str) -> True:
        # conversion code
        df = pd.read_excel(xlsx_path)
        df.to_json(json_path, orient="records")
        return True


def main() -> None:
    def success(booleanReturn) -> None:
        # indicating successful conversion
        if booleanReturn == True:
            print("Successfully converted!!!")
        elif booleanReturn == False:
            print(
                f"\nYou are trying to convert the file from '{os.path.splitext(input_path)[1]}' format to the same format!!!"
            )

    # get the file path and file extensions of input and output files
    input_path = input("\nEnter input file path : ")
    input_ext = os.path.splitext(input_path)[1][1:]
    output_path = input("\nEnter output file path : ")
    output_ext = os.path.splitext(output_path)[1][1:]

    # mapping of file types to conversion functions
    conversion_functions = {
        (FileType.csv, FileType.csv): FormatConvert.same_format,
        (FileType.csv, FileType.json): FormatConvert.csv_to_json,
        (FileType.csv, FileType.xlsx): FormatConvert.csv_to_xlsx,
        (FileType.json, FileType.json): FormatConvert.same_format,
        (FileType.json, FileType.csv): FormatConvert.json_to_csv,
        (FileType.json, FileType.xlsx): FormatConvert.json_to_xlsx,
        (FileType.xlsx, FileType.xlsx): FormatConvert.same_format,
        (FileType.xlsx, FileType.csv): FormatConvert.xlsx_to_csv,
        (FileType.xlsx, FileType.json): FormatConvert.xlsx_to_json,
    }

    # check if the file types are valid for conversion
    try:
        conversion_fn = conversion_functions[
            (FileType[input_ext], FileType[output_ext])
        ]
    except KeyError as ke:
        print(f"\nInvalid file type {ke}!!!")
        return 0

    # calling the appropriate function6
    booleanReturn = conversion_fn(input_path, output_path)
    success(booleanReturn)


# driver code
if __name__ == "__main__":
    main()
