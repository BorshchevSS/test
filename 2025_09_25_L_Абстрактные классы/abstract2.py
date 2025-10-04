#startsoft
#424242
# pip install pandas fpdf
# pip list
# pip install openpyxl

from abc import ABC, abstractmethod
from fpdf import FPDF
import pandas
import os

class ReportGenerator(ABC):
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def save(self, directory='reports'):
        pass

class PDFReport(ReportGenerator):

    def generate(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.cell(200, 10, txt='Report', ln=True, align='C')
        pdf.ln(10)
        for key, value in self.data.items():
            pdf.cell(200, 10, txt=f'{key}: {value}', ln=True)

        self.pdf = pdf #создаем свойство pdf

    def save(self, directory='reports'):
        if not os.path.exists(self.filename):
            os.makedirs(directory)
        filepath = os.path.join(directory, f'{self.filename}.pdf')
        self.pdf.output(filepath)
        print(f'PDF saved to {filepath}')

class ExcelReport(ReportGenerator):

    def generate(self):
        self.ef = pandas.DataFrame([self.data])

    def save(self, directory='reports'):
        if not os.path.exists(self.filename, ):
            os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, f'{self.filename}.xlsx')
        self.ef.to_excel(filepath, index=False)
        print(f'Excel saved to {filepath}')







data = {'Name': 'Ivan',
        'Surname': 'Petrov',
        'Age': 30,
        'City': 'Moscow'}

# pdf_report = PDFReport('report', data)
# pdf_report.generate()
# pdf_report.save()

excel_report = ExcelReport('report', data)
excel_report.generate()
excel_report.save()

