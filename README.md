# Serwis napraw komputerów


Wewnętrzny system do obsługi serwisu napraw komputerów.


## Technologie
- Python 3.12
- Django
- PostgreSQL
- Bootstrap


## Funkcje
- Zarządzanie klientami
- Urządzenia
- Zgłoszenia napraw
- Wielojęzyczność (PL / EN / DE)


## Uruchomienie lokalne
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver



---


## 📦 requirements.txt
```txt
Django>=5.0
psycopg2-binary
django-rest-framework
