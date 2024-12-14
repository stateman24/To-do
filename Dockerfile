FROM python:3.14-rc-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED = 1


# Set Working Directory
WORKDIR /Todo

# install dependencies
COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt

# Copy the Django Project
COPY . /Todo/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]



