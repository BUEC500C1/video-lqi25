import Twitter2Video
import queue
import threading
import multiprocessing

q = queue.Queue()
threads = []
def Mul_Threads(item_list,num):
  if item_list == []:
    return "No twitter names entered"
  if num == 0:
    return "The num should be bigger than 0"
  def Thread():
    while True:
      item = q.get()
      if item is None: break
      print("Thread {} is processing".format(item))
      Twitter2Video.tweet2image(item)
      Twitter2Video.image2video(item)
      print("Thread {} has completed".format(item))
      q.task_done()

  for i in range(num):
    t = threading.Thread(target = Thread)
    t.start()
    threads.append(t)
  for item in item_list:
    q.put(item)
  q.join()
  for i in range(num):
    q.put(None)
  for t in threads:
    t.join()
  print()
  print("All threads have completed")
  return "All threads have completed!"


