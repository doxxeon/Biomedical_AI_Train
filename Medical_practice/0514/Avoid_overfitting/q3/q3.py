import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras import layers, Sequential

IMG_SIZE = 256

def main():
    dog = tf.keras.utils.load_img("/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/Medical_practice/0514/Avoid_overfitting/q3/dog.jpg")
    cat = tf.keras.utils.load_img("/Users/kimdohyeon/건양대학교병원_바이오헬스/Biomedical_AI_Train/Medical_practice/0514/Avoid_overfitting/q3/cat.jpg")
    
    dog_array = tf.keras.utils.img_to_array(dog)
    cat_array = tf.keras.utils.img_to_array(cat)
    
    # TODO: [지시사항 1번] 개 사진에 전처리를 수행하는 모델을 완성하세요.
    dog_augmentation = Sequential([
        layers.Resizing(IMG_SIZE, IMG_SIZE),
        layers.Rescaling(1./255),
        layers.RandomCrop(150, 200)
    ])
    
    # TODO: [지시사항 2번] 고양이 사진에 전처리를 수행하는 모델을 완성하세요.
    cat_augmentation = Sequential([
        layers.Resizing(IMG_SIZE, IMG_SIZE),
        layers.Rescaling(1./255),
        layers.RandomFlip(),
        layers.RandomRotation(0.5),
    ])
    
    dog_augmented_tensor = dog_augmentation(dog_array)
    dog_augmented = tf.keras.utils.array_to_img(dog_augmented_tensor.numpy())
    dog_augmented.save("./dog_augmented.jpg")
    print("=" * 25, "전처리된 개", "=" * 25)
    
    print()
    
    cat_augmented_tensor = cat_augmentation(cat_array)
    cat_augmented = tf.keras.utils.array_to_img(cat_augmented_tensor.numpy())
    cat_augmented.save("./cat_augmented.jpg")
    print("=" * 25, "전처리된 고양이", "=" * 25)
    
    return dog_augmentation, cat_augmentation

if __name__ == "__main__":
    main()
