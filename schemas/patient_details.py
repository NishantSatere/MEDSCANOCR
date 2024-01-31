def patientDetails(patient) -> dict:
    return {
        "id" : str(patient["_id"]),
        "name": patient["name"],
        "age":patient["age"],
        "gender":patient["gender"],
        "collecte_date":patient["collected_date"],
        "bg": patient["bg"],
        "rbc": patient["rbc"],
        "hb": patient["hb"]
    }

def allpatientDetails(patients) -> list:
    return [patientDetails(patient) for patient in patients]