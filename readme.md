# CAPTCHA Recognition Based on the CNN

This is a simple captcha recognition project based on the CNN model. It can read 4-character captcha one by one and predict them, respectively.

## Generate Captchas

I used the "captcha" library in python to generate captchas. Single character captcha for training and 4-character captcha for testing and evaluation.

## Preprocess and Generate Dataset

Firstly, I converted RGB images into grey images and then transferred them into binary images. After that, I eliminated noises and segmented images into 4 sub images each of which contained exactly 1 character. Thirdly, I normalised such data and generated the dataset eventually. The link of final trainable dataset is: 

[DataSet](https://www.dropbox.com/s/wqg9zmn11xa0rjf/dataset.zip?dl=0)

## CNN Model

![cnn](/Users/nickit/image/cnn.jpg)

## Evaluation

The single character captcha recognition accuracy is more than 97% and overall accuracy of 4-character captcha recognition is more than 96%!

## Limitation

This model can only recognise captcha of length 4 and cannot figure out captcha images containing connected or overlapped characters, which is an important part to be improved in my further research!

