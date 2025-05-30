import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

'''
1. 상수 텐서를 생성하는 constant_tensors 함수를 완성하세요.

   Step01. 5의 값을 가지는 (1,1) shape의 8-bit integer 텐서를 만드세요.
   
   Step02. 모든 원소의 값이 0인 (3,5) shape의 16-bit integer 텐서를 만드세요.
   
   Step03. 모든 원소의 값이 1인 (4,3) shape의 8-bit integer 텐서를 만드세요.
'''

def constant_tensors():
    
    t1 = tf.constant(5, dtype=tf.int8, shape=(1,1))
    
    t2 = tf.zeros(shape=(3,5), dtype=tf.int16)
    
    t3 = tf.ones(shape=(4,3), dtype=tf.int8)
    
    return t1, t2, t3

'''
2. 시퀀스 텐서를 생성하는 sequence_tensors 함수를 완성하세요. 

   Step01. 1.5에서 10.5까지 증가하는 3개의 텐서를 만드세요.
   
   Step02. 2.5에서 20.5까지 증가하는 5개의 텐서를 만드세요. 
'''

def sequence_tensors():
    
    seq_t1 = tf.range(1.5, 10.5, delta=3)
    
    seq_t2 = tf.range(2.5, 20.5, delta=5)
    
    return seq_t1, seq_t2

'''
3. 변수를 생성하는 variable_tensor 함수를 완성하세요.

   Step01. 값이 100인 변수 텐서를 만드세요.
   
   Step02. 모든 원소의 값이 1인 (2,2) shape의 변수 텐서를 만드세요.
           이름도 'W'로 지정합니다.
   
   Step03. 모든 원소의 값이 0인 (2,) shape의 변수 텐서를 만드세요.
           이름도 'b'로 지정합니다.
'''

def variable_tensor():
    
    var_tensor = tf.Variable(100)
    
    W = tf.Variable(tf.ones(shape=(2,2)), name='W')
    
    b = tf.Variable(tf.zeros(shape=(2,)), name='b')
    
    return var_tensor, W, b

def main():
    
    t1, t2, t3 = constant_tensors()
    
    seq_t1,seq_t2 = sequence_tensors()
    
    var_tensor, W, b = variable_tensor()
    
    constant_dict = {'t1':t1, 't2':t2, 't3':t3}
    
    sequence_dict = {'seq_t1':seq_t1, 'seq_t2':seq_t2}
    
    variable_dict = {'var_tensor':var_tensor, 'W':W, 'b':b}
    
    for key, value in constant_dict.items():
        print(key, ' :', value.numpy())
    
    print()
    
    for key, value in sequence_dict.items():
        print(key, ' :', value.numpy())
        
    print()
    
    for key, value in variable_dict.items():
        print(key, ' :', value.numpy())

if __name__ == "__main__":
    main()
