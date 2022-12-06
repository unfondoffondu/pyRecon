FROM python:3
ADD ./clr.py /clr.py
ADD ./pymap.py /pymap.py
ADD ./pybuster.py /pybuster.py
ADD ./pydiscover.py /pydiscover.py
ADD ./pymap.py /pymap.py
ADD ./pyRecon.py /pyRecon.py
RUN pip install requests
RUN pip install bs4
CMD [ "apt update && apt install fping" ]
CMD [ "python3", "./pyRecon.py" ]
