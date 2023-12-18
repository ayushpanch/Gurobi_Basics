FROM gurobi/python:latest
COPY . /docker_basic
WORKDIR /docker_basic
RUN pip install -r requirements.txt
CMD ["python","solution_v4.py"]