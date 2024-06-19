from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, "Ejemplo de Tabla", 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def create_table(self, data):
        # Set the font and size for the table
        self.set_font("Arial","B" ,size=14)

        # Column width
        col_width = self.w / 4.5
        row_height = self.font_size * 1.5

        # Headers
        for header in data[0]:
            self.cell(col_width, row_height, header.upper(), border=1, align='C')
        self.ln(row_height)
        self.set_font("Arial","I" ,size=11)

        # Data
        for row in data[1:]:
            for item in row:
                self.cell(col_width, row_height, str(item), border=1, align='C')
            self.ln(row_height)