# agaya-kya

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3de08b1346d84652a7000f4116e3c0c2)](https://app.codacy.com/app/Jithinqw/agaya-kya?utm_source=github.com&utm_medium=referral&utm_content=Jithinqw/agaya-kya&utm_campaign=Badge_Grade_Dashboard)

Know which movies are showing in your city. Just pass the city name and ```agaya-kya``` can tell agaya-kya?. 
This uses Book_my_show to parse the data and show it.

## Requirements

- [x] Python3 
- [x] Flask
- [x] urllib
- [x] gunicorn (Not required, only for deployment)

## Installation 

Run ```python3 agayakya.py``` to run the server. 

## Configuration 

This server file runs on ```config.ini``` located at ```./lib``` folder. Change configurations accordingly. 

## Running Docker

### Running Docker Image
Build agaya image using ```docker build -t aagaya .``` in your terminal where your ```Dockerfile``` is located. 
Run the image using ```docker run -p 5000:5000 -t aagaya```.

### Running Docker Container using docker-compose

Run ```docker-compose up --build``` in your terminal.