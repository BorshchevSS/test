from abc import ABC, abstractmethod
from fpdf import FPDF
import pandas
import os


class ReportGenerator(ABC):
    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def save(self, directory="reports"):
        pass

class PDFReport(ReportGenerator):
    def generate(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Report", align="C", ln=True)
        pdf.ln(10)
        for key, value in self.data.items():
            pdf.cell(200, 10, txt=f"{key}: {value}, ln = True")
        self.pdf = pdf #Создаем свойство pdf

    def save(self, directory="reports"):
        if  not os.path.exists(self.file_name): #Проверяем есть ли по заданному пути файл
            os.makedirs(directory)
        filepath = os.path.join(directory, f"{self.file_name}.pdf")
        self.pdf.output(filepath)
        print(f"Файл сохранен : {filepath}")


class ExcelReport(ReportGenerator):

    def generate(self):
        self.ef = pandas.DataFrame([self.data])

    def save(self, directory="reports"):
        if  not os.path.exists(self.file_name): #Проверяем есть ли по заданному пути файл
            os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, f"{self.file_name}.xlsx")
        self.ef.to_excel(filepath, index=False)
        print(f"Файл сохранен : {filepath}")

data = {"Name": "Ivan", "age": 34, "city": "Moskov"}
# pdf_report = PDFReport("report", data)
# pdf_report.generate()
# pdf_report.save()

excel_report = ExcelReport("report", data)
excel_report.generate()
excel_report.save()


