#!/bin/bash
set -e

# CONFIGURATION - set to your Django project directory (where manage.py is)
DJANGO_DIR="django" # your django project directory

echo "== Cleaning up old virtual environments =="

# Remove venvs from root and Django project directory
for d in venv .venv; do
  if [ -d "$d" ]; then
    echo "Removing $d from root..."
    rm -rf "$d"
  fi
  if [ -d "$DJANGO_DIR/$d" ]; then
    echo "Removing $d from $DJANGO_DIR/..."
    rm -rf "$DJANGO_DIR/$d"
  fi
done

# Remove any directory in root or Django dir starting with venv
find . -maxdepth 1 -type d -name "venv*" ! -name "." -exec rm -rf {} +
find "$DJANGO_DIR" -maxdepth 1 -type d -name "venv*" -exec rm -rf {} +

echo "== Creating fresh virtual environment in root =="
python3 -m venv venv

echo "== Activating virtual environment =="
source venv/bin/activate

echo "== Changing to Django directory: $DJANGO_DIR =="
cd "$DJANGO_DIR"

echo "== Installing requirements =="
if [ -f "requirements.txt" ]; then
  pip install --upgrade pip
  pip install -r requirements.txt
else
  echo "requirements.txt not found in $DJANGO_DIR!"
  exit 1
fi

echo "== Running Django migrations =="
python manage.py migrate

echo "== Clearing order history =="
python manage.py shell <<EOF
from bicycle_app.models import Order, Order_Item
Order_Item.objects.all().delete()
Order.objects.all().delete()
EOF

echo "== Collecting static files =="
python manage.py collectstatic --noinput

read -p "Do you want to create a Django superuser now? (y/n): " createsu
if [ "\$createsu" = "y" ]; then
  python manage.py createsuperuser
fi

echo
echo "== Setup complete! =="
echo "To start your Django server, run:"
echo "cd \"$DJANGO_DIR\""
echo "source ../venv/bin/activate"
echo "python manage.py runserver"