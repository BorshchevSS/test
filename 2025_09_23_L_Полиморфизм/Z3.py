class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

class Patient(Person):
    def __init__(self, nane, age, disease):
        super().__init__(nane, age)
        self.disease = disease

    def __add__(self, other):
        return PatientGroup([self, other])

    def __str__(self):
        return f"Пациент {super().__str__()}. Заболевание: {self.disease}" #super().__str__() вызов метода родителя


class PatientGroup:
    def __init__(self, patients):
        self.patients = patients

    def __str__(self):
        return f"Группа пациентов: {'\n'.join([p.name for p in self.patients])}"

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization
        self.procedure_count = 0

    def perform_procedure(self, patient):
        raise NotImplementedError("Метод не был переопределён")

    def __gt__(self, other):
        return self.procedure_count > other.procedure_count

    def __str__(self):
        return f"Врач: {super().__str__()}, Специализация: {self.specialization}, Количество процедур: {self.procedure_count}"

class Procedure:
    def __init__(self, name, doctor, patient):
        self.name = name
        self.doctor = doctor #Хранится экземпляр класса доктора
        self.patient = patient #Хранится экземпляр класса пациент

    def __str__(self):
        return f"Процедура: {self.name}, Доктор: {self.doctor.name}, Пациент: {self.patient.name}"

# doctor_ex = Doctor("BSS", 34, "стоматолог")
# patient_ex = Patient("WAS", 77, "dd")
# pr = Procedure("Лечение", doctor_ex, patient_ex)

class Cardiologist(Doctor):
    def __init__(self, name, age):
        super().__init__(name, age, "Кардиолог")

    def perform_procedure(self, patient):
        print(f"{self.specialization} {self.name} проводит ЭКГ пациенту {patient.name}")
        self.procedure_count += 1
        return Procedure ("ЭКГ", self, patient)

cardiolog_1 = Cardiologist("Иавн Иваныч", 45)
cardiolog_2 = Cardiologist("Семён Семёныч", 55)

patient_1 = Patient("Алексй Иванович", 30, "Аретмия")
patient_2 = Patient("Владимер Владимирович", 50, "Тахикардия")

procedure1 = cardiolog_1.perform_procedure(patient_1)
procedure2 = cardiolog_2.perform_procedure(patient_1)
procedure3 = cardiolog_2.perform_procedure(patient_2)

group = patient_1 + patient_2
print(group)

print(cardiolog_1 > cardiolog_2)