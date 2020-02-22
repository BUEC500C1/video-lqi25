# Main Exercise
## Requirements
- Convert text into an image in a frame.
- Do a sequence of all texts and images in chronological order.
- Display each video frame for 3 seconds.
## Twitter to Image
- Open [Twitter Developer](https://developer.twitter.com/) and apply for a developer account.Once done, create your own app and get consumer_key, consumer_secret, access_token, access_token_secret.
- Open Twitter2Video.py,call the tweet2image function, and pass the tweet account name you want to get into the function.
- In the tweet2image function, set the background image name and the path to save the image.
```python
image = Image.open('Boston.jpg')
```
```python
filename = "C:/Users/18367/Desktop/hw4/" + str(num) + ".png"
```
- Open Terminal,run the following command,you will see images with text in the path set.
```python
python Twitter2Video.py
```
<p align="center">   
<img src="https://github.com/BUEC500C1/video-lqi25/blob/master/Twitter2Video/img/image.png"/> 
</p>   
