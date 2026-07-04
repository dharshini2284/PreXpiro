# 🥗 PreXpiro - AI Based Food Waste Reduction & Recipe Recommendation System

PreXpiro is an AI-powered food management system designed to reduce food wastage by combining food freshness detection, expiry tracking, and intelligent recipe recommendations.

The system uses a CNN-based computer vision model to classify food items as Fresh or Rotten and a BM25-based recommendation engine to suggest recipes using available ingredients while prioritizing items nearing expiry.

## ✨ Features

- 🍎 AI Food Freshness Detection  
  - Detects fresh and rotten fruits/vegetables using CNN image classification

- 📦 Smart Inventory Management  
  - Tracks stored food items and expiry dates
  - Highlights items nearing expiration

- 🍳 Intelligent Recipe Recommendation  
  - Uses BM25 ranking algorithm
  - Suggests recipes based on available ingredients
  - Prioritizes near-expiry food items to reduce waste

- 📊 Analytics Dashboard  
  - Displays freshness insights and food utilization statistics


## 🛠️ Tech Stack

**Backend**
- FastAPI
- Python

**Machine Learning**
- CNN (Convolutional Neural Network)
- Computer Vision
- Image Processing

**Recommendation Engine**
- BM25 Ranking Algorithm
- Information Retrieval

**Database**
- MongoDB

**Frontend**
- Web Application Interface


## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/dharshini2284/PreXpiro.git
cd PreXpiro
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

For Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Download NLTK Resources

Run:

```bash
python req.py
```

---

### 5️⃣ Start MongoDB

Ensure MongoDB is running locally:

```text
mongodb://localhost:27017
```

---

### 6️⃣ Run Backend Server

```bash
uvicorn backend.main:app --reload
```

Open FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```


## 🧪 API Endpoints

| Endpoint | Description |
|---------|-------------|
| `/scan/packaged` | Scan packaged food using OCR |
| `/scan/fresh` | Detect fruit & vegetable freshness using CNN |
| `/inventory/{user_id}` | View user's food inventory |
| `/recipes/recommend/{user_id}` | Generate smart recipe recommendations |


## 🧠 Model Details

### Freshness Detection
- Model: Convolutional Neural Network (CNN)
- Task: Image Classification
- Classes:
  - Fresh
  - Rotten

### Recipe Recommendation
- Algorithm: BM25 Ranking
- Matches recipes based on available ingredients
- Applies expiry-aware priority scoring

## 📸 Output Screenshots

<img width="797" height="447" alt="image" src="https://github.com/user-attachments/assets/5d8adc50-0e61-476f-b890-66277db884fa" />
<img width="780" height="467" alt="image" src="https://github.com/user-attachments/assets/80c1ceed-70c9-43d2-8ee6-acd036d86103" />
<img width="801" height="457" alt="image" src="https://github.com/user-attachments/assets/fb91a7a8-913c-42a6-b7d4-adea51d091ee" />
<img width="795" height="446" alt="image" src="https://github.com/user-attachments/assets/e470e786-7b0a-4dff-b772-0b4af7f66b00" />
<img width="798" height="445" alt="image" src="https://github.com/user-attachments/assets/5d5124e8-862c-4484-b75f-79629931ef3e" />
<img width="790" height="463" alt="image" src="https://github.com/user-attachments/assets/8b03ff1d-1388-4817-bfb6-65a66c25174a" />
<img width="792" height="495" alt="image" src="https://github.com/user-attachments/assets/5316f3ae-5f16-4ca3-975c-e0991a15aadb" />

## 🎯 Objective

PreXpiro aims to promote sustainable food consumption by reducing unnecessary food disposal through AI-based freshness prediction and smart meal planning.


## 👩‍💻 Contributors

- Dharshini A S
- Prannetha N M
