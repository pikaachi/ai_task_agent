# 📌 AI Task Agent API
🚀 An **AI-powered Task Management API** built with **FastAPI, PostgreSQL, and Machine Learning** to automatically **categorize and prioritize tasks** based on their descriptions.

---

## 📖 Features
✅ **AI-Powered Categorization**: Automatically assigns a **category** (`Work`, `Personal`, `Errands`) to tasks.  
✅ **AI-Powered Prioritization**: Predicts **task priority** (`High`, `Medium`, `Low`) using NLP.  
✅ **CRUD Operations**: Supports **Create, Read, Update, and Delete** tasks.  
✅ **PostgreSQL Database**: Stores tasks persistently.  
✅ **Dockerized Deployment**: Ready for cloud hosting (deployed on Render).  
✅ **Swagger UI**: Interactive API documentation available at [`/docs`](https://your-api-url.onrender.com/docs).  

---

## 🚀 Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Machine Learning**: Scikit-learn, spaCy
- **Deployment**: Docker, Render
- **Authentication (Future)**: JWT

---

## 📌 API Endpoints

### 📝 Task Management
| Method   | Endpoint        | Description |
|----------|----------------|-------------|
| `POST`   | `/tasks/`       | Create a new task (AI auto-fills category & priority) |
| `GET`    | `/tasks/`       | Retrieve all tasks |
| `GET`    | `/tasks/{id}`   | Retrieve a task by ID |
| `PUT`    | `/tasks/{id}`   | Update a task |
| `DELETE` | `/tasks/{id}`   | Delete a task |

---

## 🤖 AI-Powered Categorization & Prioritization

When you create a task, AI automatically assigns:

- **Category**: `Work`, `Personal`, or `Errands`
- **Priority**: `High`, `Medium`, or `Low`

### **Example `POST /tasks/` Request:**
```json
{
  "title": "Submit financial report",
  "description": "Prepare and submit the Q2 financial report",
  "completed": false
}

## 📌 Future Enhancements
- 🔹 **Expand AI Model Training for better categorization.
- 🔹 **Add JWT Authentication for secure API access.
- 🔹 **Task Reminders (Email, Slack notifications).
- 🔹 **Frontend UI (React or Streamlit integration).
