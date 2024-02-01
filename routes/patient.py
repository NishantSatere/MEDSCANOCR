from fastapi import APIRouter, HTTPException
from models.patient import patient
from bson import ObjectId 
from config.db import conn
# from schemas.patient_details import patientDetails,allpatientDetails


app = APIRouter()

db = conn.patient
# @app.get("/", response_model=list)
# def allNotes():
#     try:
#         # Fetch all notes from the 'notes' collection
#         docs = db.patient.find({})
#         # Convert the MongoDB documents to the desired format using notesEntity
#         all_notes = patientDetails(docs)
#         return all_notes
    
#     except Exception as e:
#         # Handle any exceptions that might occur during the database query
#         print(f"Error retrieving notes: {e}")
#         return []


router = APIRouter()

db = conn.patient



# ONE
@router.get("/patient/{patient_id}", response_model=dict)
async def getsinglepatient(patient_id: str):
    try:
        # patient_id = ObjectId(patient_id)  # Uncomment this line if using ObjectId

        result = await db.patient.find_one({"_id": patient_id})
        
        if result:
            # Directly return the BSON document as a dictionary
            return result
        else:
            raise HTTPException(status_code=404, detail="Patient not found")

    except Exception as e:
        # Handle any exceptions that might occur during the database operations
        print(f"Error while finding patient: {e}")
        raise HTTPException(status_code=500, detail="Failed to find patient")
    
@router.get("/patient/name/{patient_name}", response_model=dict)
async def get_patient_by_name(patient_name: str):
    try:
        # Find the patient by name
        patient = db.patient.find_one({"Name": patient_name})

        if patient:
            return patient
        else:
            raise HTTPException(status_code=404, detail="Patient not found")

    except Exception as e:
        print(f"Error while finding patient: {e}")
        raise HTTPException(status_code=500, detail="Failed to find patient")






# PUSHHH
@router.post("/entry")
def insert_patient(patient_data: dict):
    try:
        # Insert a new patient into the 'patient' collection
        result = db.patient.insert_one(patient_data)

        # Retrieve the created patient from the 'patient' collection using its ObjectId
        created_patient = db.patient.find_one({"_id": result.inserted_id})

        if created_patient:
            return patientDetails(created_patient)
        else:
            raise HTTPException(status_code=500, detail="Failed to retrieve the created patient")

    except Exception as e:
        # Handle any exceptions that might occur during the database operations
        print(f"Error creating patient: {e}")
        raise HTTPException(status_code=500, detail="Failed to create patient")



# Getting specific test result for allpatients
    

def patientDetailswithTest(patient, test_name):
    test_results = patient.get("Test Results", [])
    result = next((test.get("Result", "") for test in test_results if test.get("Test Name") == test_name), "")
    
    return {
        "id": str(patient["_id"]),
        "name": patient.get("Name", ""),
        "Test Results": {
            "Test Name": test_name,
            "Result": result
        }
    }

def allpatientstestdetails(patientlist, test_name):
    return [{"patient": patientDetailswithTest(patient, test_name)} for patient in patientlist]

@router.get("/allpatients/{test_name}", response_model=list)
def allpatientstest(test_name: str):
    try:
        docs = db.patient.find({})
        formatted_patients = allpatientstestdetails(list(docs), test_name)  # Convert cursor to list
        return formatted_patients
    except Exception as e:
        # Handle any exceptions that might occur during the database query
        print(f"Error retrieving patients: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")












# Getting all patients

def patientDetails(patient):
    return {
        "id": str(patient["_id"]),
        "name": patient.get("Name", ""),
        "age": patient.get("Age", ""),
        "gender": patient.get("Gender", ""),
        "Test Results": patient.get("Test Results","")
        # Add other fields as needed
    }

def allpatientDetails(patients):
    return [patientDetails(patient) for patient in patients]

@router.get("/allpatients", response_model=list)
def allpatients():
    try:
        # Fetch all notes from the 'patient' collection (assuming it's correct)
        docs = db.patient.find({})  

        patients_list = list(docs)

        # Format patient details using allpatientDetails function
        formatted_patients = allpatientDetails(patients_list)

        return formatted_patients

    except Exception as e:
        # Handle any exceptions that might occur during the database query
        print(f"Error retrieving patients: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    


