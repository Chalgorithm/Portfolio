import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):
    def test_matrix_multiply_un(self):
        alpha = Matrix([
            [2,1],
            [3,2],
            [1,2]
        ])
        beta = Matrix([
            [2,3,4],
            [1,3,3],
        ])
        #matrix multiplcation go:
        #(0,0): 2*2 + 3*3 + 1*4 = 17
        #(0,1): 2*1 + 3*3 + 3*1 = 14
        #(1,0): 1*2 + 3*2 + 3*2 = 14
        #(1,1): 1*1 + 3*2 + 2*3 = 7
        #result = [[17,14],[14,7]]
        result = alpha*beta
        self.assertEqual(str(result),'[17,16]\n[14,13]')
    def test_matrix_multiply_duex(self):
        alpha = Matrix([
           [2,5,6,7],
           [4,3,4,4],
           [12,3,4,1],
           [1,2,1,3]
        ])
        beta = Matrix([
            [3,2,1],
            [1,2,2],
            [4,5,6],
            [3,2,2]
        ])
       
        result = alpha*beta
        self.assertEqual(str(result),'[56,58,62]\n[43,42,42]\n[58,52,44,18,17,17]')


if __name__ == "__main__":
    unittest.main()