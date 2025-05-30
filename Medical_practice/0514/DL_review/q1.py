from PIL import Image

def crop(img, coordinates):
    # [지시사항 1] 이미지를 자르는 코드를 완성하세요.
    img_crop = img.crop(coordinates)
    
    return img_crop
    
def rotate(img, angle, expand=False):
    # [지시사항 2] 이미지를 회전하는 코드를 완성하세요.
    img_rotate = img.rotate(angle, expand=expand)
    
    return img_rotate
    
def resize(img, new_size):
    # [지시사항 3] 이미지 크기를 변경하는 코드를 완성하세요.
    img_resize = img.resize(new_size)
    
    return img_resize
    
def shearing(img, shear_factor):
    # [지시사항 4] 이미지를 전단 변환하는 코드를 완성하세요.
    img_shearing = img.transform((int(img.size[0] * (1 + shear_factor)), img.size[1]),
                            None, (1, shear_factor, 0, 0, 1, 0))
                                 
    return img_shearing
    
def show_image(img, name):
    img.save(name)


def main():
    img = Image.open("MNIST_512.png")
    
    # [지시사항 5] 지시사항에 따라 적절한 이미지 변환을 수행하세요.
    
    # 이미지 자르기
    img_crop = crop(img, (150, 200, 450, 300))
    
    # 이미지 회전하기
    img_rotate = rotate(img, 160, expand=True)
    
    # 이미지 크기 바꾸기
    img_resize = None
    
    # 이미지 전단 변환
    img_shearing = None
    
    print("=" * 5, "Crop 결과", "=" * 5)
    show_image(img_crop, "crop.png")
    
    print("=" * 5, "Rotate 결과", "=" * 5)
    show_image(img_rotate, "rotate.png")
    
    print("=" * 5, "Resize 결과", "=" * 5)
    show_image(img_resize, "resize.png")
    
    print("=" * 5, "Shearing 결과", "=" * 5)
    show_image(img_shearing, "shearing.png")
    
    return img_crop, img_rotate, img_resize, img_shearing

if __name__ == "__main__":
    main()
