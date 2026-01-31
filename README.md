
## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Download NLTK Resources (one-time)

Run:

```bash
python req.py
```

---

### 4️⃣ Start MongoDB

Ensure MongoDB service is running locally:

```
mongodb://localhost:27017
```

---

### 5️⃣ Run Server

From project root:

```bash
uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Endpoints

| Endpoint                       | Purpose                        |
| ------------------------------ | ------------------------------ |
| `/scan/packaged`               | Scan packaged food (OCR)       |
| `/scan/fresh`                  | Scan fruits & vegetables (CNN) |
| `/inventory/{user_id}`         | View inventory                 |
| `/recipes/recommend/{user_id}` | Get recipe recommendations     |


---

## 👩‍💻 Author

Dharshini
