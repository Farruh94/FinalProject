FROM python:3.11
LABEL authors="farruh"

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt && playwright install && playwright install-deps
RUN apt install -y allure
COPY . .
CMD ["make","serve_results_chrome"]
VOLUME ["/FinalProject"]
