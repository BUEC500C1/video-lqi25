# Threads
## Requirements
- Develop a queue system that can exercise your requirements with stub functions.
- Develop the twitter functionality with an API.
- Integrate them.
- Include tracking interface to show how many processes are going on and success of each.
## Achievements
- queue_mul.py uses queue to manage threads.
- Each process will call the tweet2image () and image2video () functions in Twitter2Video.py. They converted 20 tweets under the Twitter user's name into images and then videos.
- In order for Twitter2Video.py to run successfully, follow the instructions in [Twitter2Video](https://github.com/BUEC500C1/video-lqi25/tree/master/Twitter2Video), store the twitter keys in the keys.py file, and set the paths in the tweet2image () and image2video () functions.
- In queue_mul.py, set item_list and set the number of threads to 3.
```python
item_list = ['BU_Tweets','CNN','Nike','mfaboston']
```
- Open terminal.Run the following command:
```python
python queue_mul.py
```
- There are three threads running at the same time, and after one thread finishes running, the fourth thread is executed.
<p align="center">   
<img src="https://github.com/BUEC500C1/video-lqi25/blob/master/Threads/threads.png"/> 
</p>


