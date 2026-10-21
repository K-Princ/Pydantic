from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Patient Name", description="Give the name of the patient in 50 characters or less")]
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: bool = False
    allergies: Annotated[Optional[List[str]], Field(max_length=5)] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Patient data inserted successfully.")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Patient data updated successfully.")

patient_data = {'name' : "prince", 'age' : 24, 'weight' : 70.5, 'married' : False, 'allergies' : ['dust', 'pollen'], 'contact_details' : {'phone' : '123-456-7890'}}

patient1 = Patient(**patient_data)

insert_patient_data(patient1)