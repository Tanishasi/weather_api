# **Weather API**

This project is a simple app for fetching Weather details using https://openweathermap.org/ api key with authentication functionality. It allows users to sign up, log in, and fetch weather information based on latitude and longitude.

---

## **Routes Overview**

### **1. Auth Routes**
   - Handles user signup and login functionalities.

### **2. Weather Route**
   - Fetches weather information based on the latitude and longitude provided in the API call.

---

## **Steps to Run Locally**

### **1. Clone the Repository**
Run the following command to clone this repository:
```bash
git clone https://github.com/Tanishasi/weather_api.git
```

### **2. Navigate to the Project Directory**
```bash
cd weather_api
```

### **3. Install Dependencies**
Install all required packages:
```bash
pip install -r requirements.txt
```

### **4. Set Up the Database**
   1. Create a **MySQL database** on your local machine.
   2. Create a `.env` file in the project directory and configure the following variables:
      ```
      DB_URL="mysql+pymysql://username:password@localhost:3306/database_name"
      API_KEY="your_openweather_api_key"
      SECRET_KEY="your_secret_key"
      ```
   - Replace `username`, `password`, `database_name`, and `API_KEY` with your credentials.
   - For the `SECRET_KEY`, you can generate a key by following the FastAPI documentation.

### **5. Run the Server**
Start the FastAPI server using Uvicorn:
```bash
uvicorn app.main:app --reload
```

The server will start running at `http://127.0.0.1:8000`.

---

## **API Endpoints**

### **Authentication Endpoints**
1. **Signup**
   - **Endpoint**: `POST /signup`
   - **Request Body** (JSON):
     ```json
     {
       "username": "str",
       "password": "str"
     }
     ```

2. **Login**
   - **Endpoint**: `POST /login`
   - **Request Body** (JSON):
     ```json
     {
       "username": "str",
       "password": "str"
     }
     ```

---

### **Weather Endpoint**
   - **Endpoint**: `GET /weather`
   - **Query Parameters**:
     - `latitude`: Latitude of the location (e.g., `51.5074` for London)
     - `longitude`: Longitude of the location (e.g., `-0.1278` for London)
   - **Example**:
     ```plaintext
     GET http://127.0.0.1:8000/weather?latitude=51.5074&longitude=-0.1278
     ```

---

## **Notes**
1. **Database Configuration**:
   - Use MySQL as the database.
   - Update the `.env` file with appropriate credentials.

2. **OpenWeather API Key**:
   - Obtain your API key from the [OpenWeather API](https://openweathermap.org/api) and add it to the `.env` file.

3. **Secret Key**:
   - The `SECRET_KEY` is required for JWT authentication.
   - Refer to the [FastAPI Documentation](https://fastapi.tiangolo.com/) for guidance on generating a secure key.

---

