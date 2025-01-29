Development
export DJANGO_ENV=development
python manage.py runserver


Production
export DJANGO_ENV=production
gunicorn project_backend.wsgi:application --bind 0.0.0.0:8000



Optional: Enable HTTPS
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your_domain

Gunicorn Service
[Unit]
Description=gunicorn daemon for pg_solar_api
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/root/pg/pg_solar_api
ExecStart=/root/pg/pg_solar_api/env/bin/gunicorn \
          --workers 3 \
          --bind unix:/run/pg_solar_api.sock \
          pg_solar_api.wsgi:application

[Install]
WantedBy=multi-user.target


DJANGO_SECRET_KEY=dev-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_DB_BACKEND=sqlite

# Production Environment Variables
POSTGRES_USER=prod_database_user
POSTGRES_PASSWORD=6tEmi05PGv6PGW
POSTGRES_DB=prod_database_name
POSTGRES_HOST=postgres-db-prod
POSTGRES_PORT=5432

DJANGO_SECRET_KEY=django-insecure-prodsecretkey
DJANGO_ALLOWED_HOSTS=35.77.24.169,example.com
DJANGO_CORS_ALLOWED_ORIGINS=https://example.com