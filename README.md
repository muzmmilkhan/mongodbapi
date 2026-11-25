# MongoDB Employee API

A small REST API for creating and listing employees. It’s built with [FastAPI](https://fastapi.tiangolo.com/) and stores employee records in MongoDB.

## Features

- Create an employee record
- List all employee records
- Interactive API documentation at `/docs`

## Requirements

- Python 3.12 or newer
- A MongoDB deployment and connection URI
- [uv](https://docs.astral.sh/uv/) or `pip`

## Setup

1. **Get the project**

   Clone the repository, then open a terminal in the project directory.

2. **Configure MongoDB**

   Create a `.env` file in the project root:

   ```env
   MONGODB_URI=mongodb://localhost:27017
   MONGODB_DB=employee_database
   MONGODB_COLLECTION=employees