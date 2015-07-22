FROM django:python2

ENV SECRET_KEY="please change how we handle the secret key"
COPY . /usr/src/app
WORKDIR /usr/src/app/fiubar
RUN pip install -r requirements.txt
RUN python manage.py syncdb
RUN python manage.py loaddata ../fiubar.json
CMD ["python", "manage.py", "runserver"]