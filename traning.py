# lst = [1, 3, 4 ,2, 0, 123,321,222]
#for aaa in lst:
    #print(aaa)

#for i, letter in enumerate ('это строка.'):
    #print(i, letter, end='<')
#enumerate -индуксация при обходе

#генерируемый полуоткрытый интервал (начало входит, конец нет)
#for j in range(30, 10, -3):
    #print(j)

#for j in range (11):
#print(j**3)
# lst = [1, 2, 3 ,4 ,5, 6, 7 ,8, 9 ,10]
# lst = [k for k in range(1,100 + 1)]
# print(f'{list=}')

# string = 'А роза упала на лапу Азора'
# def is_palindrome(string: str) -> bool:
#     spaceless = [k.upper() for k in string if k != ' ']
#     print(spaceless)
#
#     return None
# ret = is_palindrome(string)

# string = 'А роза упала на лапу Азора'
# def is_palindrome(string: str) -> bool:
#     spaceless1 = [k.upper() for k in string if k != ' ']
#     spaceless2 = [k.upper() for k in string if k != ' ']
#     spaceless2.reverse()
#     return spaceless1 == spaceless2
#     return None
# ret = is_palindrome(string)

# import cv2
# image = cv2.imread('images/i.jpg')
#
# print(f'image shape = {image.shape}')
# height = image.shape[0]
# width = image.shape[1]
# depth = image.shape[2]

#первым идет высота
# sliced_region = image_np[:, 50:150]
#image[:, :, ] = ( 246, 254, 255)
#image[height // 2:height, 110:140] = (48, 45, 155)
#image[150:200, 1:320] = (48, 45, 155)

# отображение по горизонтали
#flipped_vertical = cv2.flip(image, 0)
#cv2.imshow('Vertical Flip', flipped_vertical)

#image[height // 2:, :] = image[height // 2:, :]

#окончательный вариант 3.3 :
# rol = image[:height // 2,:,]
# image[height // 2:, :] = cv2.flip(rol, 0)

# image[:,:, ] =20
# image[:,:,0]=0
# image[:,:,1]=0
# image[:,:,2]=0
#окончателньый вариант 3.1
# rol = image[:,:,0]
# image = rol

# # cv2.imshow('Sliced Image', sliced_region)
# cv2.imshow('Sliced Image', image)
# #cv2.imshow('Sliced Image', rol)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# from PIL import Image
#
# im = Image.open("images/i.png")
# box = (0, 0, 1000, 1000)
# region = im.crop(box)
# #region.show()
#
# #первая кордина x
# for x in range (im.size[0] // 2):
#     for y in range(im.size[1] // 2):
#         pix = m.getpixel((x,y))
#         avg = (pix[0] + pix[1] + pix[2]) // 3
#         im.putpixel((x,y), (avg,avg,avg))
# im.show()
# im.save('i.jpg')
# im = Image.open('.i.png')

print("Выберите что хотите сделать")