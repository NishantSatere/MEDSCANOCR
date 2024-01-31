from fastapi import APIRouter, HTTPException
from models.patient import patient
from bson import ObjectId 
from config.db import conn
from schemas.patient_details import patientDetails,allpatientDetails


app = APIRouter()

db = conn.patient
@app.get("/", response_model=list)
def allNotes():
    try:
        # Fetch all notes from the 'notes' collection
        docs = db.patient.find({})
        # Convert the MongoDB documents to the desired format using notesEntity
        all_notes = patientDetails(docs)
        return all_notes
    
    except Exception as e:
        # Handle any exceptions that might occur during the database query
        print(f"Error retrieving notes: {e}")
        return []
