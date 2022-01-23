from PIL import Image
import numpy as np

image = Image.open("middle.jpeg")
image = image.resize((600, 600), Image.ANTIALIAS)
image_array = np.array(image)

print(len(image_array))
print(len(image_array[0]))
print(image_array[0][0])
