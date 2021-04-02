import pandas as pds


def read_from_excel() -> pds.DataFrame:
    excel_name = "SOC平台梳理"
    excel_location = "./" \
                     + excel_name \
                     + ".xlsx"
    excel_data = pds.read_excel(excel_location)
    print(excel_data)
    return excel_data


def main():
    read_from_excel()


if __name__ == '__main__':
    main()