import requests
import time

def predict_image(image_path):
    print(image_path)
    url = f"http://127.0.0.1:8080/?img={image_path}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Error: ", response.json())


s_time = time.time()
for i in range(100):
    predict_image('./label_0.png')
e_time = time.time()

print('걸린 시간: ', e_time - s_time)