import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

load_dotenv()

app = FastAPI()

client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("MONGODB_DB")]
collection = db[os.getenv("MONGODB_COLLECTION")]

class Employee(BaseModel):
    name: str
    age: int
    position: str
    salary: float

def employee_helper(employee) -> dict:
    return {
        "name": employee["name"],
        "age": employee["age"],
        "position": employee["position"],
        "salary": employee["salary"]
    }

@app.post("/employees")
async def create_employee(employee: Employee):
    result = await collection.insert_one(employee.dict())
    new_employee = await collection.find_one({"_id": result.inserted_id})
    return employee_helper(new_employee)


@app.get("/employees")
async def get_employees():
    employees = []
    async for employee in collection.find():
        employees.append(employee_helper(employee))
    return employees

@app.put("/employees/{employee_id}")
async def update_employee(employee_id: str, employee: Employee):
    result = await collection.update_one(
        {"_id": ObjectId(employee_id)},
        {"$set": employee.dict()}
    )
    if result.modified_count == 1:
        updated_employee = await collection.find_one({"_id": ObjectId(employee_id)})
        return employee_helper(updated_employee)
    return {"error": "Employee not found"}