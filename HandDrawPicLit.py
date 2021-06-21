
from PIL import Image
import numpy as np

a = np.asarray(Image.open('./beijing.jpg').convert('L')).astype('float')


depth = 10. 						# (0-100)
grad = np.gradient(a)				#取图像灰度的梯度值
grad_x, grad_y = grad 				#分别取横纵图像梯度值
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 ) + 0.0000000001
uni_x = grad_x/A
uni_y = grad_y/A
#uni_z = 1./A

b = 255*(uni_x + uni_y ) 	#光源归一化
b = b.clip(0,255)

im = Image.fromarray(b.astype('uint8')) 	#重构图像
im.save('./beijingHD2.jpg')