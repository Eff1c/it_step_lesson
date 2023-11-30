FROM python:3.9 as app

WORKDIR /app

FROM app as install_requirements
COPY requirements.txt .

RUN pip install -r requirements.txt

FROM install_requirements as copy_project
COPY . .

FROM copy_project as run_app
EXPOSE 5000

CMD ["python3", "-u", "server.py"]
