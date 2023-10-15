
from Atividade02.vectorized.Mat4 import Mat4
from Atividade02.vectorized.Vec4 import Vec4
import numpy as np


class TestMat3:

    def test_init(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))

        assert m[0,0] == 1
        assert m[0,1] == 2
        assert m[0,2] == 3
        assert m[0,3] == 4
        assert m[1,0] == 5
        assert m[1,1] == 6
        assert m[1,2] == 7
        assert m[1,3] == 8
        assert m[2,0] == 9
        assert m[2,1] == 10
        assert m[2,2] == 11
        assert m[2,3] == 12
        assert m[3,0] == 13
        assert m[3,1] == 14
        assert m[3,2] == 15
        assert m[3,3] == 16
    
    def test_atribuition(self):
        m = Mat4()

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[0,3] == 0
        assert m[1,0] == 0
        assert m[1,1] == 0
        assert m[1,2] == 0
        assert m[1,3] == 0
        assert m[2,0] == 0
        assert m[2,1] == 0
        assert m[2,2] == 0
        assert m[2,3] == 0
        assert m[3,0] == 0
        assert m[3,1] == 0
        assert m[3,2] == 0
        assert m[3,3] == 0

        m[0,0] = 1
        m[0,1] = 2
        m[0,2] = 3
        m[0,3] = 4
        m[1,0] = 5
        m[1,1] = 6
        m[1,2] = 7
        m[1,3] = 8
        m[2,0] = 9
        m[2,1] = 10
        m[2,2] = 11
        m[2,3] = 12
        m[3,0] = 13
        m[3,1] = 14
        m[3,2] = 15
        m[3,3] = 16
        
        
        assert m[0,0] == 1
        assert m[0,1] == 2
        assert m[0,2] == 3
        assert m[0,3] == 4
        assert m[1,0] == 5
        assert m[1,1] == 6
        assert m[1,2] == 7
        assert m[1,3] == 8
        assert m[2,0] == 9
        assert m[2,1] == 10
        assert m[2,2] == 11
        assert m[2,3] == 12
        assert m[3,0] == 13
        assert m[3,1] == 14
        assert m[3,2] == 15
        assert m[3,3] == 16
    
    def test_multiple_indexing(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))

        assert np.all(m[0] == np.array([1, 2, 3, 4]))
        assert np.all(m[1] == np.array([5, 6, 7, 8]))
        assert np.all(m[2] == np.array([9, 10, 11, 12]))
        assert np.all(m[3] == np.array([13, 14, 15, 16]))

        assert np.all(m[:,0] == np.array([1, 5, 9, 13]))
        assert np.all(m[:,1] == np.array([2, 6, 10, 14]))
        assert np.all(m[:,2] == np.array([3, 7, 11, 15]))
        assert np.all(m[:,3] == np.array([4, 8, 12, 16]))

    def test_negation(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m = -m

        assert m[0,0] == -1
        assert m[0,1] == -2
        assert m[0,2] == -3
        assert m[0,3] == -4
        assert m[1,0] == -5
        assert m[1,1] == -6
        assert m[1,2] == -7
        assert m[1,3] == -8
        assert m[2,0] == -9
        assert m[2,1] == -10
        assert m[2,2] == -11
        assert m[2,3] == -12
        assert m[3,0] == -13
        assert m[3,1] == -14
        assert m[3,2] == -15
        assert m[3,3] == -16


    
    def test_add_number(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m = m + 1

        assert m[0,0] == 2
        assert m[0,1] == 3
        assert m[0,2] == 4
        assert m[0,3] == 5
        assert m[1,0] == 6
        assert m[1,1] == 7
        assert m[1,2] == 8
        assert m[1,3] == 9
        assert m[2,0] == 10
        assert m[2,1] == 11
        assert m[2,2] == 12
        assert m[2,3] == 13
        assert m[3,0] == 14
        assert m[3,1] == 15
        assert m[3,2] == 16
        assert m[3,3] == 17

    def test_add_vec4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([1, 2, 3, 4])
        m = m1 + v1

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[0,3] == 8
        assert m[1,0] == 6
        assert m[1,1] == 8
        assert m[1,2] == 10
        assert m[1,3] == 12
        assert m[2,0] == 10
        assert m[2,1] == 12
        assert m[2,2] == 14
        assert m[2,3] == 16
        assert m[3,0] == 14
        assert m[3,1] == 16
        assert m[3,2] == 18
        assert m[3,3] == 20
    
    def test_add_negative_vec4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([-1, -2, -3, -4])
        m = m1 + v1

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[0,3] == 0
        assert m[1,0] == 4
        assert m[1,1] == 4
        assert m[1,2] == 4
        assert m[1,3] == 4
        assert m[2,0] == 8
        assert m[2,1] == 8
        assert m[2,2] == 8
        assert m[2,3] == 8
        assert m[3,0] == 12
        assert m[3,1] == 12
        assert m[3,2] == 12
        assert m[3,3] == 12
    
    def test_add_mat4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m = m1 + m2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[0,3] == 8
        assert m[1,0] == 10
        assert m[1,1] == 12
        assert m[1,2] == 14
        assert m[1,3] == 16
        assert m[2,0] == 18
        assert m[2,1] == 20
        assert m[2,2] == 22
        assert m[2,3] == 24
        assert m[3,0] == 26
        assert m[3,1] == 28
        assert m[3,2] == 30
        assert m[3,3] == 32
        
    def test_add_negative_mat4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]))
        m = m1 + m2

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[0,3] == 0
        assert m[1,0] == 0
        assert m[1,1] == 0
        assert m[1,2] == 0
        assert m[1,3] == 0
        assert m[2,0] == 0
        assert m[2,1] == 0
        assert m[2,2] == 0
        assert m[2,3] == 0
        assert m[3,0] == 0
        assert m[3,1] == 0
        assert m[3,2] == 0
        assert m[3,3] == 0

    def test_sub_number(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m = m - 1

        assert m[0,0] == 0
        assert m[0,1] == 1
        assert m[0,2] == 2
        assert m[0,3] == 3
        assert m[1,0] == 4
        assert m[1,1] == 5
        assert m[1,2] == 6
        assert m[1,3] == 7
        assert m[2,0] == 8
        assert m[2,1] == 9
        assert m[2,2] == 10
        assert m[2,3] == 11
        assert m[3,0] == 12
        assert m[3,1] == 13
        assert m[3,2] == 14
        assert m[3,3] == 15
    
    def test_sub_vec4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([1, 2, 3, 4])
        m = m1 - v1

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[0,3] == 0
        assert m[1,0] == 4
        assert m[1,1] == 4
        assert m[1,2] == 4
        assert m[1,3] == 4
        assert m[2,0] == 8
        assert m[2,1] == 8
        assert m[2,2] == 8
        assert m[2,3] == 8
        assert m[3,0] == 12
        assert m[3,1] == 12
        assert m[3,2] == 12
        assert m[3,3] == 12

    def test_sub_negative_vec4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([-1, -2, -3, -4])
        m = m1 - v1

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[0,3] == 8
        assert m[1,0] == 6
        assert m[1,1] == 8
        assert m[1,2] == 10
        assert m[1,3] == 12
        assert m[2,0] == 10
        assert m[2,1] == 12
        assert m[2,2] == 14
        assert m[2,3] == 16
        assert m[3,0] == 14
        assert m[3,1] == 16
        assert m[3,2] == 18
        assert m[3,3] == 20
    
    def test_sub_mat4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m = m1 - m2

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[0,3] == 0
        assert m[1,0] == 0
        assert m[1,1] == 0
        assert m[1,2] == 0
        assert m[1,3] == 0
        assert m[2,0] == 0
        assert m[2,1] == 0
        assert m[2,2] == 0
        assert m[2,3] == 0
        assert m[3,0] == 0
        assert m[3,1] == 0
        assert m[3,2] == 0
        assert m[3,3] == 0
    
    def test_sub_negative_mat4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]))
        m = m1 - m2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[0,3] == 8
        assert m[1,0] == 10
        assert m[1,1] == 12
        assert m[1,2] == 14
        assert m[1,3] == 16
        assert m[2,0] == 18
        assert m[2,1] == 20
        assert m[2,2] == 22
        assert m[2,3] == 24
        assert m[3,0] == 26
        assert m[3,1] == 28
        assert m[3,2] == 30
        assert m[3,3] == 32
    
    def test_mul_number(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m = m * 2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[0,3] == 8
        assert m[1,0] == 10
        assert m[1,1] == 12
        assert m[1,2] == 14
        assert m[1,3] == 16
        assert m[2,0] == 18
        assert m[2,1] == 20
        assert m[2,2] == 22
        assert m[2,3] == 24
        assert m[3,0] == 26
        assert m[3,1] == 28
        assert m[3,2] == 30
        assert m[3,3] == 32
    
    def test_mul_vec4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([1, 2, 3, 4])
        m = m1 * v1

        assert m[0,0] == 1
        assert m[0,1] == 4
        assert m[0,2] == 9
        assert m[0,3] == 16
        assert m[1,0] == 5
        assert m[1,1] == 12
        assert m[1,2] == 21
        assert m[1,3] == 32
        assert m[2,0] == 9
        assert m[2,1] == 20
        assert m[2,2] == 33
        assert m[2,3] == 48
        assert m[3,0] == 13
        assert m[3,1] == 28
        assert m[3,2] == 45
        assert m[3,3] == 64

    
    def test_mul_negative_vec4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([-1, -2, -3, -4])
        m = m1 * v1

        assert m[0,0] == -1
        assert m[0,1] == -4
        assert m[0,2] == -9
        assert m[0,3] == -16
        assert m[1,0] == -5
        assert m[1,1] == -12
        assert m[1,2] == -21
        assert m[1,3] == -32
        assert m[2,0] == -9
        assert m[2,1] == -20
        assert m[2,2] == -33
        assert m[2,3] == -48
        assert m[3,0] == -13
        assert m[3,1] == -28
        assert m[3,2] == -45
        assert m[3,3] == -64
    
    def test_mul_mat4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m = m1 * m2

        assert m[0,0] == 1
        assert m[0,1] == 4
        assert m[0,2] == 9
        assert m[0,3] == 16
        assert m[1,0] == 25
        assert m[1,1] == 36
        assert m[1,2] == 49
        assert m[1,3] == 64
        assert m[2,0] == 81
        assert m[2,1] == 100
        assert m[2,2] == 121
        assert m[2,3] == 144
        assert m[3,0] == 169
        assert m[3,1] == 196
        assert m[3,2] == 225
        assert m[3,3] == 256
    
    def test_mul_negative_mat4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]))
        m = m1 * m2

        assert m[0,0] == -1
        assert m[0,1] == -4
        assert m[0,2] == -9
        assert m[0,3] == -16
        assert m[1,0] == -25
        assert m[1,1] == -36
        assert m[1,2] == -49
        assert m[1,3] == -64
        assert m[2,0] == -81
        assert m[2,1] == -100
        assert m[2,2] == -121
        assert m[2,3] == -144
        assert m[3,0] == -169
        assert m[3,1] == -196
        assert m[3,2] == -225
        assert m[3,3] == -256

    
    def test_div_number(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m = m / 2

        assert m[0,0] == 0.5
        assert m[0,1] == 1
        assert m[0,2] == 1.5
        assert m[0,3] == 2
        assert m[1,0] == 2.5
        assert m[1,1] == 3
        assert m[1,2] == 3.5
        assert m[1,3] == 4
        assert m[2,0] == 4.5
        assert m[2,1] == 5
        assert m[2,2] == 5.5
        assert m[2,3] == 6
        assert m[3,0] == 6.5
        assert m[3,1] == 7
        assert m[3,2] == 7.5
        assert m[3,3] == 8
    
    def test_div_vec4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([1, 2, 3, 4])
        m = m1 / v1

        assert m[0,0] == 1
        assert m[0,1] == 1
        assert m[0,2] == 1
        assert m[0,3] == 1
        assert m[1,0] == 5
        assert m[1,1] == 3
        assert m[1,2] == 7 / 3
        assert m[1,3] == 2
        assert m[2,0] == 9
        assert m[2,1] == 5
        assert m[2,2] == 11 / 3
        assert m[2,3] == 3
        assert m[3,0] == 13
        assert m[3,1] == 7
        assert m[3,2] == 5
        assert m[3,3] == 4

    def test_div_negative_vec4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([-1, -2, -3, -4])
        m = m1 / v1

        assert m[0,0] == -1
        assert m[0,1] == -1
        assert m[0,2] == -1
        assert m[0,3] == -1
        assert m[1,0] == -5
        assert m[1,1] == -3
        assert m[1,2] == -7 / 3
        assert m[1,3] == -2
        assert m[2,0] == -9
        assert m[2,1] == -5
        assert m[2,2] == -11 / 3
        assert m[2,3] == -3
        assert m[3,0] == -13
        assert m[3,1] == -7
        assert m[3,2] == -5
        assert m[3,3] == -4
    
    def test_div_mat4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m = m1 / m2

        assert m[0,0] == 1
        assert m[0,1] == 1
        assert m[0,2] == 1
        assert m[0,3] == 1
        assert m[1,0] == 1
        assert m[1,1] == 1
        assert m[1,2] == 1
        assert m[1,3] == 1
        assert m[2,0] == 1
        assert m[2,1] == 1
        assert m[2,2] == 1
        assert m[2,3] == 1
        assert m[3,0] == 1
        assert m[3,1] == 1
        assert m[3,2] == 1
        assert m[3,3] == 1
    
    def test_div_negative_mat4(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]))
        m = m1 / m2

        assert m[0,0] == -1
        assert m[0,1] == -1
        assert m[0,2] == -1
        assert m[0,3] == -1
        assert m[1,0] == -1
        assert m[1,1] == -1
        assert m[1,2] == -1
        assert m[1,3] == -1
        assert m[2,0] == -1
        assert m[2,1] == -1
        assert m[2,2] == -1
        assert m[2,3] == -1
        assert m[3,0] == -1
        assert m[3,1] == -1
        assert m[3,2] == -1
        assert m[3,3] == -1
    
    def test_iadd_number(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m += 1

        assert m[0,0] == 2
        assert m[0,1] == 3
        assert m[0,2] == 4
        assert m[0,3] == 5
        assert m[1,0] == 6
        assert m[1,1] == 7
        assert m[1,2] == 8
        assert m[1,3] == 9
        assert m[2,0] == 10
        assert m[2,1] == 11
        assert m[2,2] == 12
        assert m[2,3] == 13
        assert m[3,0] == 14
        assert m[3,1] == 15
        assert m[3,2] == 16
        assert m[3,3] == 17
    
    def test_iadd_vec4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([1, 2, 3, 4])
        m += v1

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[0,3] == 8
        assert m[1,0] == 6
        assert m[1,1] == 8
        assert m[1,2] == 10
        assert m[1,3] == 12
        assert m[2,0] == 10
        assert m[2,1] == 12
        assert m[2,2] == 14
        assert m[2,3] == 16
        assert m[3,0] == 14
        assert m[3,1] == 16
        assert m[3,2] == 18
        assert m[3,3] == 20
    
    def test_iadd_negative_vec4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([-1, -2, -3, -4])
        m += v1

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[0,3] == 0
        assert m[1,0] == 4
        assert m[1,1] == 4
        assert m[1,2] == 4
        assert m[1,3] == 4
        assert m[2,0] == 8
        assert m[2,1] == 8
        assert m[2,2] == 8
        assert m[2,3] == 8
        assert m[3,0] == 12
        assert m[3,1] == 12
        assert m[3,2] == 12
        assert m[3,3] == 12
    
    def test_iadd_mat4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m += m2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[0,3] == 8
        assert m[1,0] == 10
        assert m[1,1] == 12
        assert m[1,2] == 14
        assert m[1,3] == 16
        assert m[2,0] == 18
        assert m[2,1] == 20
        assert m[2,2] == 22
        assert m[2,3] == 24
        assert m[3,0] == 26
        assert m[3,1] == 28
        assert m[3,2] == 30
        assert m[3,3] == 32
    
    def test_iadd_negative_mat4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]))
        m += m2

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[0,3] == 0
        assert m[1,0] == 0
        assert m[1,1] == 0
        assert m[1,2] == 0
        assert m[1,3] == 0
        assert m[2,0] == 0
        assert m[2,1] == 0
        assert m[2,2] == 0
        assert m[2,3] == 0
        assert m[3,0] == 0
        assert m[3,1] == 0
        assert m[3,2] == 0
        assert m[3,3] == 0
    
    def test_isub_number(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m -= 1

        assert m[0,0] == 0
        assert m[0,1] == 1
        assert m[0,2] == 2
        assert m[0,3] == 3
        assert m[1,0] == 4
        assert m[1,1] == 5
        assert m[1,2] == 6
        assert m[1,3] == 7
        assert m[2,0] == 8
        assert m[2,1] == 9
        assert m[2,2] == 10
        assert m[2,3] == 11
        assert m[3,0] == 12
        assert m[3,1] == 13
        assert m[3,2] == 14
        assert m[3,3] == 15
    
    def test_isub_vec4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([1, 2, 3, 4])
        m -= v1

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[0,3] == 0
        assert m[1,0] == 4
        assert m[1,1] == 4
        assert m[1,2] == 4
        assert m[1,3] == 4
        assert m[2,0] == 8
        assert m[2,1] == 8
        assert m[2,2] == 8
        assert m[2,3] == 8
        assert m[3,0] == 12
        assert m[3,1] == 12
        assert m[3,2] == 12
        assert m[3,3] == 12
    
    def test_isub_negative_vec4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([-1, -2, -3, -4])
        m -= v1

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[0,3] == 8
        assert m[1,0] == 6
        assert m[1,1] == 8
        assert m[1,2] == 10
        assert m[1,3] == 12
        assert m[2,0] == 10
        assert m[2,1] == 12
        assert m[2,2] == 14
        assert m[2,3] == 16
        assert m[3,0] == 14
        assert m[3,1] == 16
        assert m[3,2] == 18
        assert m[3,3] == 20
    
    def test_isub_mat4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m -= m2

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[0,3] == 0
        assert m[1,0] == 0
        assert m[1,1] == 0
        assert m[1,2] == 0
        assert m[1,3] == 0
        assert m[2,0] == 0
        assert m[2,1] == 0
        assert m[2,2] == 0
        assert m[2,3] == 0
        assert m[3,0] == 0
        assert m[3,1] == 0
        assert m[3,2] == 0
        assert m[3,3] == 0
    
    def test_isub_negative_mat4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]))
        m -= m2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[0,3] == 8
        assert m[1,0] == 10
        assert m[1,1] == 12
        assert m[1,2] == 14
        assert m[1,3] == 16
        assert m[2,0] == 18
        assert m[2,1] == 20
        assert m[2,2] == 22
        assert m[2,3] == 24
        assert m[3,0] == 26
        assert m[3,1] == 28
        assert m[3,2] == 30
        assert m[3,3] == 32
    
    def test_imul_number(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m *= 2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[0,3] == 8
        assert m[1,0] == 10
        assert m[1,1] == 12
        assert m[1,2] == 14
        assert m[1,3] == 16
        assert m[2,0] == 18
        assert m[2,1] == 20
        assert m[2,2] == 22
        assert m[2,3] == 24
        assert m[3,0] == 26
        assert m[3,1] == 28
        assert m[3,2] == 30
        assert m[3,3] == 32
    
    def test_imul_vec4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([1, 2, 3, 4])
        m *= v1

        assert m[0,0] == 1
        assert m[0,1] == 4
        assert m[0,2] == 9
        assert m[0,3] == 16
        assert m[1,0] == 5
        assert m[1,1] == 12
        assert m[1,2] == 21
        assert m[1,3] == 32
        assert m[2,0] == 9
        assert m[2,1] == 20
        assert m[2,2] == 33
        assert m[2,3] == 48
        assert m[3,0] == 13
        assert m[3,1] == 28
        assert m[3,2] == 45
        assert m[3,3] == 64
    
    def test_imul_negative_vec4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([-1, -2, -3, -4])
        m *= v1

        assert m[0,0] == -1
        assert m[0,1] == -4
        assert m[0,2] == -9
        assert m[0,3] == -16
        assert m[1,0] == -5
        assert m[1,1] == -12
        assert m[1,2] == -21
        assert m[1,3] == -32
        assert m[2,0] == -9
        assert m[2,1] == -20
        assert m[2,2] == -33
        assert m[2,3] == -48
        assert m[3,0] == -13
        assert m[3,1] == -28
        assert m[3,2] == -45
        assert m[3,3] == -64
    
    def test_imul_mat4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m *= m2

        assert m[0,0] == 1
        assert m[0,1] == 4
        assert m[0,2] == 9
        assert m[0,3] == 16
        assert m[1,0] == 25
        assert m[1,1] == 36
        assert m[1,2] == 49
        assert m[1,3] == 64
        assert m[2,0] == 81
        assert m[2,1] == 100
        assert m[2,2] == 121
        assert m[2,3] == 144
        assert m[3,0] == 169
        assert m[3,1] == 196
        assert m[3,2] == 225
        assert m[3,3] == 256
    
    def test_imul_negative_mat4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]))
        m *= m2

        assert m[0,0] == -1
        assert m[0,1] == -4
        assert m[0,2] == -9
        assert m[0,3] == -16
        assert m[1,0] == -25
        assert m[1,1] == -36
        assert m[1,2] == -49
        assert m[1,3] == -64
        assert m[2,0] == -81
        assert m[2,1] == -100
        assert m[2,2] == -121
        assert m[2,3] == -144
        assert m[3,0] == -169
        assert m[3,1] == -196
        assert m[3,2] == -225
        assert m[3,3] == -256
    
    def test_itruediv_number(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m /= 2.0

        assert m[0,0] == 0.5
        assert m[0,1] == 1
        assert m[0,2] == 1.5
        assert m[0,3] == 2
        assert m[1,0] == 2.5
        assert m[1,1] == 3
        assert m[1,2] == 3.5
        assert m[1,3] == 4
        assert m[2,0] == 4.5
        assert m[2,1] == 5
        assert m[2,2] == 5.5
        assert m[2,3] == 6
        assert m[3,0] == 6.5
        assert m[3,1] == 7
        assert m[3,2] == 7.5
        assert m[3,3] == 8
    
    def test_itruediv_vec4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([1, 2, 3, 4])
        m /= v1

        assert m[0,0] == 1
        assert m[0,1] == 1
        assert m[0,2] == 1
        assert m[0,3] == 1
        assert m[1,0] == 5
        assert m[1,1] == 3
        assert m[1,2] == 7 / 3
        assert m[1,3] == 2
        assert m[2,0] == 9
        assert m[2,1] == 5
        assert m[2,2] == 11 / 3
        assert m[2,3] == 3
        assert m[3,0] == 13
        assert m[3,1] == 7
        assert m[3,2] == 5
        assert m[3,3] == 4

    
    def test_itruediv_negative_vec4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        v1 = Vec4([-1, -2, -3, -4])
        m /= v1

        assert m[0,0] == -1
        assert m[0,1] == -1
        assert m[0,2] == -1
        assert m[0,3] == -1
        assert m[1,0] == -5
        assert m[1,1] == -3
        assert m[1,2] == -7 / 3
        assert m[1,3] == -2
        assert m[2,0] == -9
        assert m[2,1] == -5
        assert m[2,2] == -11 / 3
        assert m[2,3] == -3
        assert m[3,0] == -13
        assert m[3,1] == -7
        assert m[3,2] == -5
        assert m[3,3] == -4
    
    def test_itruediv_mat4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m /= m2

        assert m[0,0] == 1
        assert m[0,1] == 1
        assert m[0,2] == 1
        assert m[0,3] == 1
        assert m[1,0] == 1
        assert m[1,1] == 1
        assert m[1,2] == 1
        assert m[1,3] == 1
        assert m[2,0] == 1
        assert m[2,1] == 1
        assert m[2,2] == 1
        assert m[2,3] == 1
        assert m[3,0] == 1
        assert m[3,1] == 1
        assert m[3,2] == 1
        assert m[3,3] == 1
    
    def test_itruediv_negative_mat4(self):
        m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]))
        m /= m2

        assert m[0,0] == -1
        assert m[0,1] == -1
        assert m[0,2] == -1
        assert m[0,3] == -1
        assert m[1,0] == -1
        assert m[1,1] == -1
        assert m[1,2] == -1
        assert m[1,3] == -1
        assert m[2,0] == -1
        assert m[2,1] == -1
        assert m[2,2] == -1
        assert m[2,3] == -1
        assert m[3,0] == -1
        assert m[3,1] == -1
        assert m[3,2] == -1
        assert m[3,3] == -1
    
    def test_dot(self):
        m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        m = m1.dot(m2)

        assert m[0,0] == 90
        assert m[0,1] == 100
        assert m[0,2] == 110
        assert m[0,3] == 120
        assert m[1,0] == 202
        assert m[1,1] == 228
        assert m[1,2] == 254
        assert m[1,3] == 280
        assert m[2,0] == 314
        assert m[2,1] == 356
        assert m[2,2] == 398
        assert m[2,3] == 440
        assert m[3,0] == 426
        assert m[3,1] == 484
        assert m[3,2] == 542
        assert m[3,3] == 600
    