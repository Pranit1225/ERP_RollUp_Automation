from openpyxl import load_workbook

def read_part_numbers(file_path):

    workbook = load_workbook(file_path, data_only=True)

    sheet = workbook.active

    part_numbers = []

    for cell in sheet["A"]:
        if cell.value is not None:
            value = str(cell.value).strip()
            if value != "":
                part_numbers.append(value)

    workbook.close()

    return part_numbers
