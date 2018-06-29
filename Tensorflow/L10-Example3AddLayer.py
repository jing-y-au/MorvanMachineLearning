import tensorflow as tf

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# Weights.shape=(n_features, n_outputs), inputs.shape = (n_samples, n_features)
# 所以, i*W = (n_samples, n_outputs)

# Weights.shape=(n_features, n_outputs) 也可以理解为(in_size, out_size)