## 📦 FastAPI + React Product Management App

A full-stack web application using **FastAPI (Python)** as the backend and **React.js** as the frontend to manage products with CRUD operations.

---

## 🚀 Features

* FastAPI REST API
* React Frontend UI
* PostgreSQL Database
* SQLAlchemy ORM
* Full CRUD operations
* API integration between frontend & backend

---

## 🛠️ Tech Stack

**Backend:**

* FastAPI
* Python
* SQLAlchemy
* PostgreSQL

**Frontend:**

* React.js
* Node.js
* npm

---

## 📁 Project Structure

```
fastapi-demo-products-with-ui/
├── backend/
│   ├── main.py
│   ├── database.py
│   └── database_models.py
├── frontend/
│   ├── package.json
│   └── src/
├── myenv/
└── README.md
```

---

## ⚙️ Backend Setup (FastAPI)

### 1. Create Virtual Environment

```bash
python -m venv myenv
```

### 2. Activate Virtual Environment

**Windows:**

```bash
myenv\Scripts\activate
```

---

### 3. Install Backend Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2
```

---

### 4. Configure PostgreSQL Database

In `database.py`, update your DB credentials:

```python
db_url = "postgresql://username:password@localhost:5432/dbname"
```

> If your password contains `@` or special characters, URL-encode it.

---

### 5. Run the Backend Server

```bash
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

## ⚙️ Frontend Setup (React)

### 1. Go to Frontend Folder

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

---

### 3. Start the React App

```bash
npm start
```

Frontend will run at:

```
http://localhost:3000
```

---

## 🔁 Connecting Frontend & Backend

In your React project’s `package.json`, make sure this proxy exists:

```json
"proxy": "http://localhost:8000"
```

This allows the frontend to call the FastAPI backend.

---

## ✅ How to Run Full Project

Open **two terminals**:

### Terminal 1 – Backend

```bash
uvicorn main:app --reload
```

### Terminal 2 – Frontend

```bash
cd frontend
npm start
```

---

## 📬 API Endpoints

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| GET    | /products | Get all products |
| POST   | /product  | Add new product  |
| PUT    | /product  | Update product   |
| DELETE | /product  | Delete product   |

---

## 👨‍💻 Author

**Varshith Sai Morla**
GitHub: [https://github.com/Varshith-2C0](https://github.com/Varshith-2C0)

