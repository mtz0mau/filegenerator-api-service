# define a function for generate pdf file and save it in a directory: /app/tmp
# the function receives a entry_adapter.data_merge(json_data) as a parameter
from app.classes.pdf import PDF
from io import BytesIO
import uuid

def generate_pdf(data):
    pdf = PDF()
    pdf.add_page()
    pdf.create_table(data)
    pdf_buffer = BytesIO()
    pdf_buffer.write(pdf.output(dest='S').encode('latin1'))
    pdf_buffer.seek(0)
    return pdf_buffer

def generate_uuid_filename():
    return f"{uuid.uuid4()}.pdf"