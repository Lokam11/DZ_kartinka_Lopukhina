import cv2
image = cv2.imread('images/i.jpg')

print(f'image shape = {image.shape}')
height = image.shape[0]
width = image.shape[1]
depth = image.shape[2]

#окончателньый вариант 3.1
# rol = image[:,:,0]
# image = rol

#окончательный вариант 3.3 :
# rol = image[:height // 2,:,]
# image[height // 2:, :] = cv2.flip(rol, 0)



# cv2.imshow('Sliced Image', sliced_region)
cv2.imshow('Sliced Image', image)
#cv2.imshow('Sliced Image', rol)
cv2.waitKey(0)
cv2.destroyAllWindows()