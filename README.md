# FastAPI Data Upload with Database Storage README

This repository provides a simple FastAPI application that allows users to upload data with attachments, store it in a SQLite database, and retrieve the stored data. The uploaded attachments are saved in the `uploads` directory within the project.

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- databases
- uvicorn (for running the FastAPI server)
- SQLite (already bundled with Python)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/fastapi-data-upload.git
cd fastapi-data-upload
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

- The allowed origins for CORS are defined in the `origins` list inside `app.py`. You can update this list with the frontend URLs that are allowed to access your API.

## Starting the FastAPI Server

To start the FastAPI server, run the following command:

```bash
uvicorn app:app --reload
```

The `--reload` flag enables auto-reloading on code changes, which is helpful during development.

## API Endpoints

### Upload Data

- **URL:** `POST /data`
- **Description:** Uploads data with an attachment (if provided) and stores it in the SQLite database.
- **Parameters:**
  - `name` (string): Name of the data entry.
  - `phone` (string): Phone number associated with the data.
  - `email` (string): Email address associated with the data.
  - `category` (string): Category of the data entry.
  - `q1`, `q2`, `q3`, `q4`, `q5` (string, optional): Answers to additional questions.
  - `attachment` (file, optional): File attachment associated with the data entry.
- **Response:**
  - `message` (string): Success message if data is uploaded successfully.

### Database Schema

The database schema is defined as follows:

```python
class MyData(Base):
    __tablename__ = 'mydata'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(1000))
    phone = Column(String(1000))
    email = Column(String(1000))
    category = Column(String(1000))
    q1 = Column(String(1000))
    q2 = Column(String(1000))
    q3 = Column(String(1000))
    q4 = Column(String(1000))
    q5 = Column(String(1000))
    attachment = Column(String(100))
```

## Usage

1. Start the FastAPI server using `uvicorn`, as mentioned in the "Starting the FastAPI Server" section.

2. Use an API client (e.g., [Postman](https://www.postman.com/), [curl](https://curl.se/), etc.) or integrate the frontend application to interact with the API.

3. Upload data by sending a `POST` request to the `/data` endpoint with the required parameters. If the data entry includes an attachment, pass it along with the request.

4. Retrieve the stored data from the SQLite database through your application or API client, as needed.

## Notes

- This is a basic implementation meant for demonstration purposes and may require additional security measures and error handling for production use.

- For production deployment, consider using a more robust database like PostgreSQL or MySQL.

- Make sure to set appropriate permissions for the `uploads` directory to allow file uploads.

- Don't forget to update the allowed CORS origins in `app.py` with the correct frontend URLs.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and expand upon this FastAPI application to suit your specific needs. Happy coding! 🚀
