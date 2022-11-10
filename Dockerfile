FROM python
WORKDIR /app
RUN pip install cherrypy
COPY ws.py /app
COPY myprocessor.py /app
EXPOSE 8081
CMD ["python", "ws.py"]
