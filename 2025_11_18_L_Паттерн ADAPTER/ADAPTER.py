import json
from dataclasses import fields
from difflib import unified_diff
from xml.etree import ElementTree as ET
from abc import ABC, abstractmethod

#Целевой интерфейс (Target)
class DataSource(ABC):
    @abstractmethod
    def get_report(self, fields: list) -> list[dict]:
        pass

#Adaptees
class LegacyXmlService:
    def fetch_old_data(self) -> str:
        print("LegacyXmlService")
        xml_data = """<records>
            <record>
                <record_id>1001</record_id>
                <client_name>Иванов И.</client_name>
                <amount_val>4500.50</amount_val>
                <trans_date>2023-10-01</trans_date>
            </record>
            <record>
                <record_id>1002</record_id>
                <client_name>Петров П.</client_name>
                <amount_val>12000.00</amount_val>
                <trans_date>2023-10-05</trans_date>
            </record>
        </records>"""
        return xml_data


class ModernJsonAPI:
    def get_current_metrics(self) -> str:
        print("ModernJsonAPI")
        json_data = [
            {
                "entity_uuid": "e9a0f4b3",
                "user_handle": "sidorov_v",
                "metric_total": 77.8,
                "timestamp": "2023-11-10T14:30:00"
            },
            {
                "entity_uuid": "c2d1e0a9",
                "user_handle": "kozyrev_m",
                "metric_total": 150.1,
                "timestamp": "2023-11-10T15:00:00"
            }
        ] #Список словарей
        return json.dumps(json_data) #Преобразовываем в строку


class LocalFileReader:
    def read_records(self) -> list[dict]:
        print("LocalFileReader")
        return [{
                "record_identifier": 500,
                "full_name": "ООО Ромашка",
                "count": 25,
                "creation_time": "2023-01-15 08:00:00"
            }]


#Adapters
class LegacyXmlAdapter(DataSource):
    def __init__(self, adaptee: LegacyXmlService):
        self._adaptee = adaptee

    def get_report(self, fields: list) -> list[dict]:
        xml_string = self._adaptee.fetch_old_data()

        root = ET.fromstring(xml_string)
        unified_data = []
        field_map = {
            "record_id": "id",
            "client_name": "name",
            "amount_val": "value",
            "trans_date": "date",
        }

        for rec_el in root.findall("record"):
            record = {}
            for old_field, new_field in field_map.items():
                element = rec_el.find(old_field)
                if element is not None:
                    value = float(element.text) if new_field == "value" else element.text
                    record[new_field] = value

            if record:
                unified_data.append(record)
        print("XML успешно преобразован")
        return unified_data


class ModernJsonAdapter(DataSource):
    def __init__(self, adaptee: ModernJsonAPI):
        self._adaptee = adaptee

    def get_report(self, fields: list) -> list[dict]:
        json_string = self._adaptee.get_current_metrics()
        raw_data = json.loads(json_string) #список словарей
        print(raw_data)
        unified_data =[]
        field_map = {
            "entity_uuid": "id",
            "user_handle": "name",
            "metric_total": "value",
            "timestamp": "date",
        }
            #Пройтись циклом и добавить ключи
        for record in raw_data:
            new_record = {}
            for old_field, new_field in field_map.items():
                if old_field in record:
                    new_record[new_field] = record[old_field]
            unified_data.append(new_record)
            print(new_record)
        print("JSON успешно преобразован")
        return unified_data

class LocalFileAdapter(DataSource):
    def __init__(self, adaptee: LocalFileReader):
        self._adaptee = adaptee

    def get_report(self, fields: list) -> list[dict]:
        data = self._adaptee.read_records()

        unified_data =[]
        field_map = {
            "record_identifier": "id",
            "full_name": "name",
            "count": "value",
            "creation_time": "date",
        }

        for record in data:
            new_record = {}
            for old_field, new_field in field_map.items():
                if old_field is record:
                    new_record[new_field] = record[old_field]
            unified_data.append(new_record)

        print("LocalFile успешно преобразован")
        return unified_data

#Client
class ReportingSystem:
    @staticmethod
    def generate_report(data_source: DataSource) ->None:
        print("генерация отчета")
        report_data = data_source.get_report(
            fields=["id", "name", "value", "date"])
        if not report_data:
            print("отчет пуст")
            return
        print("Унифицированный формат данных")
        for item in report_data:
            print(f"ID: {item.get("id", "N/A")}, Name: {item.get("name", "N/A")}, Value: {item.get("value", "N/A")}, Date: {item.get("date", "N/A")}")

if __name__=="__main__":
    print("демонстрация")
    legacy_service = LegacyXmlService()
    xml = LegacyXmlAdapter(legacy_service)
    ReportingSystem.generate_report(xml)

    modern_api = ModernJsonAPI()
    json_a = ModernJsonAdapter(modern_api)
    ReportingSystem.generate_report(json_a)

    local_file = LocalFileReader()
    local_a = LocalFileAdapter(local_file)
    ReportingSystem.generate_report(local_a)





