import tensorflow as tf

def preprocess(file_path):
    #It will take a single file path and return a preprocessed image
    
    # Read in image from file path
    byte_img = tf.io.read_file(file_path)
    # Load in the image, i.e converting the jpeg into a tensor (np array)
    img = tf.io.decode_jpeg(byte_img)
    
    # Preprocessing steps - resizing the image to be 100x100x3
    img = tf.image.resize(img, (100,100))
    # Scale image to be between 0 and 1 
    img = img / 255.0
    
    # Return image
    return img

