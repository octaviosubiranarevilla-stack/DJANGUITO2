
# Sistema de Gestión de Tareas - Django

Proyecto desarrollado con Django que permite gestionar tareas con autenticación y control de roles.

---

## 🚀 Instalación

### 1. Clonar repositorio

git clone https://github.com/octavius0713/todolist-django.git
cd todolist-django

---

### 2. Crear entorno virtual

python -m venv venv

Activar:

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

---

### 3. Instalar dependencias

pip install -r requirements.txt

---

### 4. Migraciones

python manage.py migrate

---

### 5. Crear superusuario

python manage.py createsuperuser

---

### 6. Ejecutar servidor

python manage.py runserver

---

## 👤 Roles del sistema

- Invitado: solo puede ver tareas
- Usuario registrado: crear y editar
- Administrador: eliminar tareas

---

## 🌐 Acceso

http://127.0.0.1:8000/
