"""
tensor means an array of data that has multiple dimension or we can say array of data 
so its indicate flow of data
"""
import tensorflow as tf
a =tf.constant([1,2,3,4])
b =tf.constant([3,5,6,7])
result =tf.multiply(a,b)
print(result)
""" ouptut 
Tensor("Mul_3:0", shape=(4,), dtype=int32)
min value=3
shape 4
dtype =int32
"""
