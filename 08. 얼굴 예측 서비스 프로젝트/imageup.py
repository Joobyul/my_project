import numpy as np
import os
import cv2
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Sequential
from keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint

# 경로 지정
train_data_dir = './dataset/train_data/'
validation_data_dir = './dataset/validation_data/'

# 변수 지정
img_width, img_height = 32, 32
num_epochs = 10
batch_size = 32
num_classes = 2

# ImageDataGenerator를 사용하여 이미지 부풀리기 설정
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)


train_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

# VGG16 모델 설정
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(img_width, img_height, 3))

# 모델 구현
model = Sequential()
model.add(base_model)
model.add(Flatten())
model.add(Dense(10, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# 모델 컴파일
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Model checkpoint callback (saves the best model weights)
checkpoint = ModelCheckpoint('best_model.h5', monitor='val_accuracy', mode='max', save_best_only=True)

# 가정한 변수들의 값
folder_dir_ = "./dataset/man/"
img_dirs = ["cool_tone_manfaces", "warm_tone_manfaces"]
gen_dir = ["./dataset/train_data1/gen_dir3/", "./dataset/train_data1/gen_dir4/"]

# 이미지를 부풀리고 저장
for i in range(2):
    file_list = os.listdir(folder_dir_ + img_dirs[i])
    for file_name in file_list:
        if file_name.endswith('.png') or file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
            image_path = os.path.join(folder_dir_ + img_dirs[i], file_name)
            image = cv2.imread(image_path)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            resized_image = cv2.resize(rgb_image, (img_width, img_height))
            x = resized_image.reshape((1,) + resized_image.shape)
            
            # flow() 메서드를 이용하여 부풀리기된 이미지를 생성
            for j, batch in enumerate(datagen.flow(x, 
                                                   batch_size=1, 
                                                   save_to_dir=gen_dir[i], 
                                                   save_prefix='aug', 
                                                   save_format='jpg')):
                if j > 999:  # 각 원본 이미지당 새로운 이미지를 생성하는 개수 설정 
                    break



# # 모델 학습
# history = model.fit_generator(
#     datagen.flow(train_generator, batch_size=batch_size),
#     steps_per_epoch=len(train_generator) // batch_size,
#     epochs=num_epochs,
#     callbacks=[early_stopping, checkpoint]
# )