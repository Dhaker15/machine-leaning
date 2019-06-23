
#loading digit data
from sklearn.datasets import load_digits

digit_data=load_digits()

dir(digit_data)

#output that we want...
digit_data.target_names

#dercription digit data
digit_data.DESCR

#traning data
feature=digit_data.data

#shape
feature.shape

#label
label=digit_data.target

label.shape

# actual images
images=digit_data.images

images[0]

#visual of Zeros
import matplotlib.pyplot as plt

plt.imshow(images[9])
plt.show

