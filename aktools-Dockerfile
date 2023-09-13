FROM --platform=linux/amd64 python:3.11-slim as build
RUN pip install aktools
EXPOSE 80
CMD ["python3", "-m" ,"aktools" ,"--host", "0.0.0.0","--port" ,"80"]