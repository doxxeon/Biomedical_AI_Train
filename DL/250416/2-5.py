import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

'''
1. 이항 연산자를 사용해 사칙 연산을 수행하여 각 변수에 저장하세요.

   Step01. 텐서 'a'와 'b'를 더해 'add'에 저장하세요.
   
   Step02. 텐서 'a'에서 'b'를 빼 'sub'에 저장하세요.
   
   Step03. 텐서 'a'와 'b'를 곱해 'mul'에 저장하세요.
   
   Step04. 텐서 'a'에서 'b'를 나눠 'div'에 저장하세요.
'''

def main():
    
    a = tf.constant(10, dtype = tf.int32)
    b = tf.constant(3, dtype = tf.int32)
    
    add = tf.add(a, b)
    sub = tf.subtract(a, b)
    mul = tf.multiply(a, b)
    div = tf.divide(a, b)
    
    tensor_dict = {'add':add, 'sub':sub, 'mul':mul, 'div':div}
    
    for key, value in tensor_dict.items():
        print(key, ' :', value.numpy(), '\n')
    
    return add, sub, mul, div

if __name__ == "__main__":
    main()
