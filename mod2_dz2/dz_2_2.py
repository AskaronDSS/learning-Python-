from PIL import Image
import numpy as np

image = Image.open('image.jpg')
image = image.convert('RGB')

img_array = np.array(image)

print("Розмір зображення:", img_array.shape)
print("Тип даних:", img_array.dtype)


for i, color in enumerate(['R', 'G', 'B']):
    print(f"{color}: mean={np.mean(img_array[:,:,i]):.2f}, min={np.min(img_array[:,:,i])}, max={np.max(img_array[:,:,i])}")


# 3_2
total = np.sum(img_array)
print("Общая сумма:", total)

# 3_3
normal_img = img_array / 255.0
print("Нормализация изображения — min:", np.min(normal_img), "max:", np.max(normal_img))


rescaled_img = (normal_img * 255).astype(np.uint8)
normalized_image = Image.fromarray(rescaled_img)
normalized_image.show()