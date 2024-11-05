# requests and pillow
import  requests
from PIL import Image



r = requests.get('https://api.github.com/events')

print("Статус код:", r.status_code)
print("Содержимое:", r.json())
print(r.url) # убедиться, что URL-адрес был правильно закодирован, распечатав URL-адрес
print(r.text) # прочитать содержимое ответа сервера

# pillow
with Image.open("/Users/user/PycharmProjects/Potok/hooper.jpg") as im:
    im.rotate(45).show() # загружает изображение, поворачивает его на 45 градусов
print("Размер изображения:")
print(im.format, im.size, im.mode)

im = im.resize((800, 800))
im.save("/Users/user/PycharmProjects/Potok/hooper.jpg", format="JPEG")
img = Image.open("/Users/user/PycharmProjects/Potok/hooper.jpg")




