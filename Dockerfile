FROM python:3.9-alpine
ENV FLASK_APP=app.py
WORKDIR /flask-sqlite3-todo-crud
COPY ./ /flask-sqlite3-todo-crud
RUN pip install --no-cache-dir -r ./requirements/requirements.txt
RUN apk add --no-cache bash
EXPOSE 5000
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
