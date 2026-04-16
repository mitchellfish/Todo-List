## Developers:
Muperi Allan M250043
Hove Mitchell M251064

---

# 📝 Django To-Do List App


## 📌 Overview

This is a simple To-Do List web application built using Django. It allows users to create, view, update, and delete tasks in a clean and minimal interface.

The project is designed for beginners learning Django and demonstrates core concepts like models, views, templates, and basic CRUD operations.

---

## 🚀 Features

* Add new tasks
* View all tasks
* Mark tasks as complete/incomplete
* Delete tasks
* Optional task descriptions
* Simple and clean UI

---

## 🧱 Built With

* Python
* Django
* HTML & CSS
* SQLite (default Django database)

---

## 📂 Project Structure

```
project/
│── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── todo_list.html
│── manage.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

### 2. Create a virtual environment

```
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install django
```

### 5. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the development server

```
python manage.py runserver
```

### 7. Open in browser

```
http://127.0.0.1:8000/
```

