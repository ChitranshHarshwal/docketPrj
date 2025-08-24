## Docker101

This repository is a **step-by-step guide** for running a simple Python Flask application inside a Docker container.

---

## 📂 Project Structure

- **`app.py`** → A basic Flask application written in Python.  
- **`requirements.txt`** → Contains the Python libraries required to run the app.  
- **`Dockerfile`** → Instructions to build a Docker image for the Flask app.  

---

host="0.0.0.0" → Makes the Flask app accessible to the outside world (not just inside the container). Without this, it would only be reachable from within the container itself.

port=5000 → Ensures the app listens on port 5000, which is mapped in Docker (-p 5000:5000). This allows you to access it via http://localhost:5000.
