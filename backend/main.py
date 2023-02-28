import openpyxl
import json
import gdown

# add conf.json
XLSX_URL: str = r'https://docs.google.com/spreadsheets/d/1W5znKQixeRJeg_IwiLoUFN8cqcStC44L/export?format=xlsx'
XLSX_FILENAME: str = 'schedule.xlsx'
OUTPUT_FILE: str = "frontend/dist/schedule.json"
TABLE_START: str = 'A5'
DATE_CELL: str = "A3"


def download_xlsx(url: str) -> None:
    gdown.download(url=XLSX_URL, output=XLSX_FILENAME, fuzzy=True)
    print(f'{XLSX_FILENAME} saved.')


def get_col(worksheet, starting_cell):
    return [cell.value for cell in list(worksheet[starting_cell.column_letter]) if cell.row > starting_cell.row]


def get_row(worksheet, starting_cell):
    return {cell.value: cell for cell in list(worksheet[starting_cell.row]) if cell.column > starting_cell.column}


def main():
    download_xlsx(XLSX_URL)
    ws = openpyxl.load_workbook(filename=XLSX_FILENAME).worksheets[0]
    classes = get_row(worksheet=ws, starting_cell=ws[TABLE_START])

    hours = get_col(worksheet=ws, starting_cell=ws[TABLE_START])

    schedule = {"date": ws[DATE_CELL].value}
    for cur_class in classes:
        class_schedule = get_col(
            worksheet=ws, starting_cell=classes[cur_class])
        schedule[cur_class] = [[hour, lesson]
                               for hour, lesson in zip(hours, class_schedule)]

    with open(OUTPUT_FILE, "w") as outputFile:
        json.dump(schedule, outputFile)


if __name__ == "__main__":
    main()
