import pytest
from Twitter2Video import image2video,tweet2image
from queue_mul import Mul_Threads
def test_result():
    item_list = ['BU_Tweets','CNN','Nike','mfaboston']
    item_list_2 = ['BU_Tweets', 'CNN', 'Nike', 'mfaboston', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME']
    assert Mul_Threads([],2) == "No twitter names entered"
    assert Mul_Threads(item_list,0) == "The num should be bigger than 0"
    # No twitter keys, can't test.
    '''
    assert Mul_Threads(item_list,3) == "All threads have completed!"
    assert Mul_Threads(item_list, 4) == "All threads have completed!"
    assert Mul_Threads(item_list, 5) == "All threads have completed!"
    assert Mul_Threads(item_list_2, 6) == "All threads have completed!"
    assert Mul_Threads(item_list_2, 10) == "All threads have completed!"
    '''