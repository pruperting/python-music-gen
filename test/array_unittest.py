import sys
sys.path.append("../")

import unittest
from midiutil.TrackGen import LoopingArray, StaticIterator, LoopingIndexedArray,\
    LoopingIncrementalIndexedArray


class Test(unittest.TestCase):
    def testLoopingArray(self):
        l = LoopingArray([1, 2, 3, 4, 5])
        
        assert l.next() == 1
        assert l.next() == 2
        assert l.next() == 3
        assert l.next() == 4
        assert l.next() == 5
        assert l.next() == 1
        
        l = LoopingArray([1, 2, 3, 4, 5], [('add', StaticIterator(value=2))])
        
        assert l.next() == 1
        assert l.next() == 3
        assert l.next() == 5
        assert l.next() == 2
        
        l = LoopingArray([1, 2, 3, 4, 5], [('add', StaticIterator(value=2)), ('dec', StaticIterator(value=1))])
        
        assert l.next() == 1
        assert l.next() == 2
        assert l.next() == 3
        assert l.next() == 4
        assert l.next() == 5
        assert l.next() == 1

        l = LoopingArray([1, 2, 3, 4, 5], [('add', StaticIterator(value=1)), ('dec', StaticIterator(value=2))])
        
        assert l.next() == 1
        assert l.next() == 5
        assert l.next() == 4
        assert l.next() == 3
        assert l.next() == 2
        assert l.next() == 1
        assert l.next() == 5

    def testLoopingIndexedArray(self):
        l = LoopingIndexedArray([1,2,3,4,5],[0])
        
        assert l.next() == 1
        assert l.next() == 1
        assert l.next() == 1
        
        l = LoopingIndexedArray([1,2,3,4,5],[0,1])
        
        assert l.next() == 1
        assert l.next() == 2
        assert l.next() == 1
        
        l = LoopingIndexedArray([1,2,3,4,5],[0,5])
        
        assert l.next() == 1
        assert l.next() == 1
        assert l.next() == 1
        
        l = LoopingIndexedArray([1,2,3,4,5],[0,2,3])
        
        assert l.next() == 1
        assert l.next() == 3
        assert l.next() == 4
            
        l = LoopingIndexedArray([1,2,3,4,5],[0,2,3], [('add', StaticIterator(value=2))])
        
        assert l.next() == 1
        assert l.next() == 4
        assert l.next() == 3
        assert l.next() == 1
        
    def testLoopingIncrementalIndexedArray(self):
        l = LoopingIncrementalIndexedArray([1,2,3,4,5],[1,0,1,2])
        
        assert l.next() == 1
        assert l.next() == 2
        assert l.next() == 2
        assert l.next() == 3
        assert l.next() == 5
        assert l.next() == 1
        assert l.next() == 1
        assert l.next() == 2
        assert l.next() == 4
        
        l = LoopingIncrementalIndexedArray([1,2,3,4,5],[1,-1,0,1])
        
        assert l.next() == 1
        assert l.next() == 2
        assert l.next() == 1
        assert l.next() == 1
        assert l.next() == 2
        assert l.next() == 3
        assert l.next() == 2
        assert l.next() == 2
        
if __name__ == "__main__":
    unittest.main()

