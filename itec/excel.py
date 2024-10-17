import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from datetime import datetime


def exportToExcel(items: list[dict], serializer, directory=None):
    if not isinstance(items, list) or not all(isinstance(item, dict) for item in items):
        raise ValueError('Input must be a list of dictionaries')

    fields = serializer.Meta.fields

    filtered_items = []
    for item in items:
        filtered_item = {field: item[field] for field in fields if field in item}
        for key, value in filtered_item.items():
            if isinstance(value, datetime):
                filtered_item[key] = value.replace(tzinfo=None)
        filtered_items.append(filtered_item)

    df = pd.DataFrame(filtered_items)
    df.columns = df.columns.str.replace('_', ' ').str.title()

    file_name = 'exported_data.xlsx'

    if directory:
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, file_name)
    else:
        file_path = file_name

    df.to_excel(file_path, index=False)

    wb = load_workbook(file_path)
    ws = wb.active

    header_font = Font(bold=True, color='FFFFFF')
    header_fill = PatternFill(
        start_color='0000FF', end_color='0000FF', fill_type='solid'
    )

    for cell in ws[1]:
        cell.font = header_font
        cell.fill = header_fill

    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=1):
        for cell in row:
            cell.font = Font(bold=True)

    wb.save(file_path)

    return file_path
