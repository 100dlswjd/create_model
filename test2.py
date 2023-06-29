# 이제 테스트 이미지 분류
import os
import matplotlib.pyplot as plt
import numpy as np
import keras.utils as image
import tensorflow as tf

model = tf.keras.models.load_model('test_model.h5')

# 테스트용 O 이미지 경로 설정
test_dir = 'src/test/'
test_o_dir = os.path.join(test_dir, 'cats/')
test_o_filenames = os.listdir(test_o_dir)
print(test_o_filenames)

# 테스트용 X 이미지 경로 설정
test_dir = 'src/test/'
test_x_dir = os.path.join(test_dir, 'dogs/')
test_x_filenames = os.listdir(test_x_dir)
print(test_x_filenames)
print(111111111)

# O,X를 key로, 이미지 파일 이름들을 value로 dictionary 생성
dic_ox_filenames = {}
dic_ox_filenames['cats'] = test_o_filenames
dic_ox_filenames['dogs'] = test_x_filenames

# O/X 분류 테스트
for ox, filenames in dic_ox_filenames.items():
    fig = plt.figure(figsize=(16,10))
    rows, cols = 1, 6
    for i, fn in enumerate(filenames):
        path = test_dir + ox + '/' + fn
        test_img = image.load_img(path, color_mode='grayscale', target_size=(150, 150), interpolation='bilinear')        
        x = image.img_to_array(test_img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])

        classes = model.predict(images, batch_size=10)
        
        fig.add_subplot(rows, cols, i+1)
        if classes[0]==0:
            plt.title(fn + " is cat")
            plt.axis('off')
            plt.imshow(test_img, cmap='gray')

        else:
            plt.title(fn + " is dog")
            plt.axis('off')
            plt.imshow(test_img, cmap='gray')
    plt.show()