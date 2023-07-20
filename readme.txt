Image Classification (AI)

Languages: Python, Jupyter Notebook

Topics: Artificial intelligence, Machine learning, Machine vision, Deep learning, Tensorflow, Image processing, Image classification, Image validation, Jupyter, Keras, iPython notebook, Image recognition, Artificial neural networks

This mini project includes 2 modules:
“image-test.py” and “machine-vision.ipynb”
First file is our insurance to have a valid and correct type of files in images dataset which divides in two directories for training and testing. One is aluminum 7000 series and the other is aluminum 2000 series alloys.

Second file is the main file which does the main task on this program. The program main goal is to reach a high accuracy in image classification and prediction.
2 classes have been set to be classified. One is for aluminum 7000 series alloys and the other is for aluminum 2000 series alloys.
In order to specify the differences between aluminum 2000 series alloys and aluminum 7000 series alloys using Convolutional Neural Networks (CNNs), we would need a labeled dataset of images representing both types of alloys. The dataset should contain a sufficient number of images for each class, and the images should capture the characteristic features that differentiate the two series of alloys.
For this purpose we went through the following steps:
We used the Keras API with TensorFlow to build and train the CNN model. 
The code uses the ImageDataGenerator class to perform data augmentation and preprocessing on the training images.
The flow_from_directory function is used to load the training, validation, and testing data from the respective directories.
The CNN model architecture consists of several convolutional and pooling layers, followed by fully connected layers.
The model is compiled with the Adam optimizer and categorical cross-entropy loss function.
The model is then trained using the fit function, specifying the training and validation generators.
Finally, the trained model is evaluated on the testing set using the evaluate function, and the loss and accuracy metrics are printed.

Note: Codes documentation and descriptions are more obvious in comments among the codes on each file.
