initiate_db:
	dropdb m2agro --if-exists
	createdb m2agro
	python manage.py migrate

update_db:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver

install_hook:
	pip install flake8
	flake8 --install-hook
	git config flake8.strict true
