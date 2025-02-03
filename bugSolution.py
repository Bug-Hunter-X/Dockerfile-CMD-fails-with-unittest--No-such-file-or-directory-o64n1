FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN chmod +x *.py # Make test files executable
CMD ["python3", "-m", "unittest", "discover"]