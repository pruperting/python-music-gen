import sys
sys.path.append("../")

from midiutil.TrackGen import LoopingArray

if __name__ == '__main__':
    arr = LoopingArray(
                       [x for x in range(128)],
                       functioniterator=[
                                         ('add', LoopingArray([1, 2, 3], functioniterator=[
                                                                                         ('add', LoopingArray([1, 2, 3], functioniterator=[
                                                                                                                                           ('add', LoopingArray([1,2,3], id='      array4', debug=True))
                                                                                                                                           ],
                                                                                                              id='    array3', debug=True)
                                                                                          )
                                                                                         ],
                                                              id='  array2', debug=True)
                                          )
                                         ],
                       id='array1', debug=True
                       )
    
    for _ in range(20):
        arr.next()
