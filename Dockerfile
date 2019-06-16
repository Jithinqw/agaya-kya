FROM python:3.7
EXPOSE 7000
RUN mkdir agaya-kya
WORKDIR /agaya-kya
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR agaya-kya
CMD ["gunicorn", "-b", "0.0.0.0:5000", "aagaya:app", "-w", "3"]