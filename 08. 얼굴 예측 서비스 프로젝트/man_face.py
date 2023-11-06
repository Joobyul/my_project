import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Sequential
from keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint

# 경로 지정
train_data_dir = './dataset/train_data1/'
validation_data_dir = './dataset/validation_data1/'

# 변수 지정
img_width, img_height = 32, 32
num_epochs = 7
batch_size = 32
num_classes = 2

# 증강
train_datagen = ImageDataGenerator(rescale=1./255,
        rotation_range=10,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=[0.2, 2.2],
        horizontal_flip=True,
        vertical_flip=True,
        fill_mode='nearest')


train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

# ImageDataGenerator를 사용하여 검증 데이터 부르기 설정
validation_datagen = ImageDataGenerator(rescale=1./255)

# 검증 데이터 생성기
validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
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
model.add(Dense(256, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# 모델 컴파일
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Model checkpoint callback (saves the best model weights)
checkpoint = ModelCheckpoint('best_model.h5', monitor='val_accuracy', mode='max', save_best_only=True)

# 모델 학습
history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=num_epochs,
    validation_data=validation_generator,  # Change here: use validation_data instead of validation_generator
    callbacks=[early_stopping, checkpoint]  # Add callbacks to the training process
)

# 모델 평가 (출력 accuracy)
loss, accuracy = model.evaluate(train_generator)
print('Accuracy:', accuracy)

from keras.preprocessing import image

# 훈련 데이터에 대한 손실과 정확도
train_loss, train_accuracy = model.evaluate(train_generator)
print('Train Loss:', train_loss)
print('Train Accuracy:', train_accuracy)

# 검증 데이터에 대한 손실과 정확도
validation_loss, validation_accuracy = model.evaluate(validation_generator)
print('Validation Loss:', validation_loss)
print('Validation Accuracy:', validation_accuracy)

# 이미지를 불러오고 전처리하기
img_path = "./dataset/me.jpg"  # 분류할 이미지의 경로
img = image.load_img(img_path, target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)  # 이미지를 모델에 입력하도록 전처리

# 모델을 사용하여 예측하기
predictions = model.predict(x)
# 예측값을 해석하여 쿨톤 또는 웜톤으로 분류
if predictions[0][0] > predictions[0][1]:
    print("쿨톤 이미지입니다.")
else:
    print("웜톤 이미지입니다.")


model.save('man_tone_model.h5')