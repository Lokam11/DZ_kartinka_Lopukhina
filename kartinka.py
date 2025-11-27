def save_image(image):
    while True:
        filename = input("Введите имя для сохранения: ")

        try:
            cv2.imwrite(filename, image)
            print(f"Изображение сохранено как '{filename}'")
            break

        except Exception as e:
            print(f"Ошибка. Попробуйте другое имя\n")

import cv2
image = cv2.imread('images/i.jpg')
print(f'image shape = {image.shape}')
height = image.shape[0]
width = image.shape[1]
depth = image.shape[2]
print("Выберите что хотите сделать:")
enter = input('''применить эффект (1); сохранить (2)
Ввод:''')

if "2" == enter:
    save_image(image)
elif "1" == enter:
    print("выберите эффект:")
    enter = input("""
    отобразить изображение по горизонтали(3.3)
    сделать изображение черно-белым (3.1)
    Ввод:""")
    if enter == "3.3":
        rol = image[:height // 2,:,]
        image[height // 2:, :] = cv2.flip(rol, 0)
    elif enter == "3.1":
        rol = image[:,:,0]
        image = rol

cv2.imshow('Результат', image)
cv2.waitKey(0)
cv2.destroyAllWindows()