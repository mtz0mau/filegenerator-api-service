from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import uuid
import os

def generate_xlsx(data):
    wb = Workbook()
    ws = wb.active
    
    # Adding headers
    headers = data[0]
    ws.append(headers)
    
    # Adding data
    for row in data[1:]:
        ws.append(row)
    
    filename = generate_uuid_filename()
    file_path = save_xlsx_to_file(wb, filename)
    
    return file_path

def save_xlsx_to_file(wb, filename):
    file_path = os.path.join("./", filename)
    wb.save(file_path)
    return file_path

def generate_uuid_filename():
    return f"{uuid.uuid4()}.xlsx"
