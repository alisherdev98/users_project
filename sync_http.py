import requests
import time

urls = ["https://example.com", "https://httpbin.org/get", "https://httpbin.org/get"]

def fetch(url):
    response = requests.get(url)

    print(f"Загружена {url}, длина: {len(response.text)}")

def main():
    for url in urls:
        fetch(url)


start_time = time.time()
main()

print(f"Время выполнения: {time.time() - start_time}")