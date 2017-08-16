import tensorflow as tf
with tf.name_scope("MyAssissement"):
    with tf.name_scope("a"):
        a = 4
        x=tf.pow(a, 2, name="Square_of_a")

    with tf.name_scope("B"):
        b =6
        y=tf.pow(b, 2, name="Square_of_b")
   
    with tf.name_scope("C"):
        d = tf.multiply(2, a, name="2a")

    with tf.name_scope("Scope_D"):
        e = tf.multiply(d, b, name="2ab")

    with tf.name_scope("Scope_E"):
        f = tf.add(x, y)

    with tf.name_scope("Scope_F"):
        g = tf.subtract(f, e,)
        
with tf.Session() as sess:
        writer = tf.summary.FileWriter("/tmp/tboard/output3", sess.graph)
        print(sess.run(g))
        writer.close()
