FROM django:1.7-python2

ENV SECRET_KEY="please change how we handle the secret key"

WORKDIR /usr/src/app/fiubar
ADD fiubar/requirements.txt /usr/src/app/fiubar/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ADD . /usr/src/app
RUN python manage.py migrate
RUN python manage.py loaddata ../fiubar.json
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]