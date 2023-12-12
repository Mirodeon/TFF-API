set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py auth --run-syncdb
python manage.py migrate --run-syncdb
python manage.py createsu