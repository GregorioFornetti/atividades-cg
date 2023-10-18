
import pytest
from Atividade02.src.interactive.Mat3 import Mat3
from Atividade02.src.interactive.Vec3 import Vec3
import numpy as np


class TestMat3:

    def test_init(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        assert m[0,0] == 1
        assert m[0,1] == 2
        assert m[0,2] == 3
        assert m[1,0] == 4
        assert m[1,1] == 5
        assert m[1,2] == 6
        assert m[2,0] == 7
        assert m[2,1] == 8
        assert m[2,2] == 9

    def test_init_exception(self):
        with pytest.raises(ValueError):
            Mat3(np.array([[1, 2], [3, 4], [5, 6]]))
        
        with pytest.raises(ValueError):
            Mat3(np.array([[1, 2], [3, 4, 5]]))
        
        with pytest.raises(TypeError):
            Mat3(1)
        
        with pytest.raises(TypeError):
            Mat3("1")
    
    def test_atribuition(self):
        m = Mat3()

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[1,0] == 0
        assert m[1,1] == 0
        assert m[1,2] == 0
        assert m[2,0] == 0
        assert m[2,1] == 0
        assert m[2,2] == 0

        m[0,0] = 1
        m[0,1] = 2
        m[0,2] = 3
        m[1,0] = 4
        m[1,1] = 5
        m[1,2] = 6
        m[2,0] = 7
        m[2,1] = 8
        m[2,2] = 9
        
        assert m[0,0] == 1
        assert m[0,1] == 2
        assert m[0,2] == 3
        assert m[1,0] == 4
        assert m[1,1] == 5
        assert m[1,2] == 6
        assert m[2,0] == 7
        assert m[2,1] == 8
        assert m[2,2] == 9
    
    def test_multiple_indexing(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        assert np.all(m[0] == np.array([1, 2, 3]))
        assert np.all(m[1] == np.array([4, 5, 6]))
        assert np.all(m[2] == np.array([7, 8, 9]))

        assert np.all(m[:,0] == np.array([1, 4, 7]))
        assert np.all(m[:,1] == np.array([2, 5, 8]))
        assert np.all(m[:,2] == np.array([3, 6, 9]))


    
    def test_negation(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m = -m

        assert m[0,0] == -1
        assert m[0,1] == -2
        assert m[0,2] == -3
        assert m[1,0] == -4
        assert m[1,1] == -5
        assert m[1,2] == -6
        assert m[2,0] == -7
        assert m[2,1] == -8
        assert m[2,2] == -9
    
    def test_add_number(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m = m + 1

        assert m[0,0] == 2
        assert m[0,1] == 3
        assert m[0,2] == 4
        assert m[1,0] == 5
        assert m[1,1] == 6
        assert m[1,2] == 7
        assert m[2,0] == 8
        assert m[2,1] == 9
        assert m[2,2] == 10

    def test_add_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(1, 2, 3)
        m = m1 + v1

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[1,0] == 5
        assert m[1,1] == 7
        assert m[1,2] == 9
        assert m[2,0] == 8
        assert m[2,1] == 10
        assert m[2,2] == 12
    
    def test_add_negative_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(-1, -2, -3)
        m = m1 + v1

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[1,0] == 3
        assert m[1,1] == 3
        assert m[1,2] == 3
        assert m[2,0] == 6
        assert m[2,1] == 6
        assert m[2,2] == 6
    
    def test_add_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m = m1 + m2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[1,0] == 8
        assert m[1,1] == 10
        assert m[1,2] == 12
        assert m[2,0] == 14
        assert m[2,1] == 16
        assert m[2,2] == 18
    
    def test_add_negative_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]))
        m = m1 + m2

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[1,0] == 0
        assert m[1,1] == 0
        assert m[1,2] == 0
        assert m[2,0] == 0
        assert m[2,1] == 0
        assert m[2,2] == 0

    def test_add_exception(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        with pytest.raises(TypeError):
            m1 + "1"
        
        with pytest.raises(TypeError):
            m1 + [1]
        
        with pytest.raises(TypeError):
            m1 + (1, 2)
    
    def test_sub_number(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m = m - 1

        assert m[0,0] == 0
        assert m[0,1] == 1
        assert m[0,2] == 2
        assert m[1,0] == 3
        assert m[1,1] == 4
        assert m[1,2] == 5
        assert m[2,0] == 6
        assert m[2,1] == 7
        assert m[2,2] == 8
    
    def test_sub_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(1, 2, 3)
        m = m1 - v1

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[1,0] == 3
        assert m[1,1] == 3
        assert m[1,2] == 3
        assert m[2,0] == 6
        assert m[2,1] == 6
        assert m[2,2] == 6

    def test_sub_negative_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(-1, -2, -3)
        m = m1 - v1

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[1,0] == 5
        assert m[1,1] == 7
        assert m[1,2] == 9
        assert m[2,0] == 8
        assert m[2,1] == 10
        assert m[2,2] == 12
    
    def test_sub_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m = m1 - m2

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[0,2] == 0
        assert m[1,0] == 0
        assert m[1,1] == 0
        assert m[1,2] == 0
        assert m[2,0] == 0
        assert m[2,1] == 0
        assert m[2,2] == 0
    
    def test_sub_negative_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]))
        m = m1 - m2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[1,0] == 8
        assert m[1,1] == 10
        assert m[1,2] == 12
        assert m[2,0] == 14
        assert m[2,1] == 16
        assert m[2,2] == 18
    
    def test_sub_exception(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        with pytest.raises(TypeError):
            m1 - "1"
        
        with pytest.raises(TypeError):
            m1 - [1]
        
        with pytest.raises(TypeError):
            m1 - (1, 2)
    
    def test_mul_number(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m = m * 2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[1,0] == 8
        assert m[1,1] == 10
        assert m[1,2] == 12
        assert m[2,0] == 14
        assert m[2,1] == 16
        assert m[2,2] == 18
    
    def test_mul_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(1, 2, 3)
        m = m1 * v1

        assert m[0,0] == 1
        assert m[0,1] == 4
        assert m[0,2] == 9
        assert m[1,0] == 4
        assert m[1,1] == 10
        assert m[1,2] == 18
        assert m[2,0] == 7
        assert m[2,1] == 16
        assert m[2,2] == 27
    
    def test_mul_negative_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(-1, -2, -3)
        m = m1 * v1

        assert m[0,0] == -1
        assert m[0,1] == -4
        assert m[0,2] == -9
        assert m[1,0] == -4
        assert m[1,1] == -10
        assert m[1,2] == -18
        assert m[2,0] == -7
        assert m[2,1] == -16
        assert m[2,2] == -27
    
    def test_mul_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m = m1 * m2

        assert m[0,0] == 1
        assert m[0,1] == 4
        assert m[0,2] == 9
        assert m[1,0] == 16
        assert m[1,1] == 25
        assert m[1,2] == 36
        assert m[2,0] == 49
        assert m[2,1] == 64
        assert m[2,2] == 81
    
    def test_mul_negative_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]))
        m = m1 * m2

        assert m[0,0] == -1
        assert m[0,1] == -4
        assert m[0,2] == -9
        assert m[1,0] == -16
        assert m[1,1] == -25
        assert m[1,2] == -36
        assert m[2,0] == -49
        assert m[2,1] == -64
        assert m[2,2] == -81
    
    def test_mul_exception(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        with pytest.raises(TypeError):
            m1 * "1"
        
        with pytest.raises(TypeError):
            m1 * [1]
        
        with pytest.raises(TypeError):
            m1 * (1, 2)
    
    def test_div_number(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m = m / 2

        assert m[0,0] == 0.5
        assert m[0,1] == 1
        assert m[0,2] == 1.5
        assert m[1,0] == 2
        assert m[1,1] == 2.5
        assert m[1,2] == 3
        assert m[2,0] == 3.5
        assert m[2,1] == 4
        assert m[2,2] == 4.5
    
    def test_div_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(1, 2, 3)
        m = m1 / v1

        assert m[0,0] == 1
        assert m[0,1] == 1
        assert m[0,2] == 1
        assert m[1,0] == 4
        assert m[1,1] == 2.5
        assert m[1,2] == 2
        assert m[2,0] == 7
        assert m[2,1] == 4
        assert m[2,2] == 3

    
    def test_div_negative_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(-1, -2, -3)
        m = m1 / v1

        assert m[0,0] == -1
        assert m[0,1] == -1
        assert m[0,2] == -1
        assert m[1,0] == -4
        assert m[1,1] == -2.5
        assert m[1,2] == -2
        assert m[2,0] == -7
        assert m[2,1] == -4
        assert m[2,2] == -3
    
    def test_div_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m = m1 / m2

        assert m[0,0] == 1
        assert m[0,1] == 1
        assert m[0,2] == 1
        assert m[1,0] == 1
        assert m[1,1] == 1
        assert m[1,2] == 1
        assert m[2,0] == 1
        assert m[2,1] == 1
        assert m[2,2] == 1
    
    def test_div_negative_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]))
        m = m1 / m2

        assert m[0,0] == -1
        assert m[0,1] == -1
        assert m[0,2] == -1
        assert m[1,0] == -1
        assert m[1,1] == -1
        assert m[1,2] == -1
        assert m[2,0] == -1
        assert m[2,1] == -1
        assert m[2,2] == -1
    
    def test_div_exception(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        with pytest.raises(TypeError):
            m1 / "1"
        
        with pytest.raises(TypeError):
            m1 / [1]
        
        with pytest.raises(TypeError):
            m1 / (1, 2)
    
    def test_iadd_number(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m += 1

        assert m[0,0] == 2
        assert m[0,1] == 3
        assert m[0,2] == 4
        assert m[1,0] == 5
        assert m[1,1] == 6
        assert m[1,2] == 7
        assert m[2,0] == 8
        assert m[2,1] == 9
        assert m[2,2] == 10
    
    def test_iadd_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(1, 2, 3)
        m1 += v1

        assert m1[0,0] == 2
        assert m1[0,1] == 4
        assert m1[0,2] == 6
        assert m1[1,0] == 5
        assert m1[1,1] == 7
        assert m1[1,2] == 9
        assert m1[2,0] == 8
        assert m1[2,1] == 10
        assert m1[2,2] == 12
    
    def test_iadd_negative_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(-1, -2, -3)
        m1 += v1

        assert m1[0,0] == 0
        assert m1[0,1] == 0
        assert m1[0,2] == 0
        assert m1[1,0] == 3
        assert m1[1,1] == 3
        assert m1[1,2] == 3
        assert m1[2,0] == 6
        assert m1[2,1] == 6
        assert m1[2,2] == 6
    
    def test_iadd_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m1 += m2

        assert m1[0,0] == 2
        assert m1[0,1] == 4
        assert m1[0,2] == 6
        assert m1[1,0] == 8
        assert m1[1,1] == 10
        assert m1[1,2] == 12
        assert m1[2,0] == 14
        assert m1[2,1] == 16
        assert m1[2,2] == 18
    
    def test_iadd_negative_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]))
        m1 += m2

        assert m1[0,0] == 0
        assert m1[0,1] == 0
        assert m1[0,2] == 0
        assert m1[1,0] == 0
        assert m1[1,1] == 0
        assert m1[1,2] == 0
        assert m1[2,0] == 0
        assert m1[2,1] == 0
        assert m1[2,2] == 0
    
    def test_iadd_exception(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        with pytest.raises(TypeError):
            m1 += "1"
        
        with pytest.raises(TypeError):
            m1 += [1]
        
        with pytest.raises(TypeError):
            m1 += (1, 2)
    
    def test_isub_number(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m -= 1

        assert m[0,0] == 0
        assert m[0,1] == 1
        assert m[0,2] == 2
        assert m[1,0] == 3
        assert m[1,1] == 4
        assert m[1,2] == 5
        assert m[2,0] == 6
        assert m[2,1] == 7
        assert m[2,2] == 8
    
    def test_isub_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(1, 2, 3)
        m1 -= v1

        assert m1[0,0] == 0
        assert m1[0,1] == 0
        assert m1[0,2] == 0
        assert m1[1,0] == 3
        assert m1[1,1] == 3
        assert m1[1,2] == 3
        assert m1[2,0] == 6
        assert m1[2,1] == 6
        assert m1[2,2] == 6
    
    def test_isub_negative_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(-1, -2, -3)
        m1 -= v1

        assert m1[0,0] == 2
        assert m1[0,1] == 4
        assert m1[0,2] == 6
        assert m1[1,0] == 5
        assert m1[1,1] == 7
        assert m1[1,2] == 9
        assert m1[2,0] == 8
        assert m1[2,1] == 10
        assert m1[2,2] == 12
    
    def test_isub_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m1 -= m2

        assert m1[0,0] == 0
        assert m1[0,1] == 0
        assert m1[0,2] == 0
        assert m1[1,0] == 0
        assert m1[1,1] == 0
        assert m1[1,2] == 0
        assert m1[2,0] == 0
        assert m1[2,1] == 0
        assert m1[2,2] == 0
    
    def test_isub_negative_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]))
        m1 -= m2

        assert m1[0,0] == 2
        assert m1[0,1] == 4
        assert m1[0,2] == 6
        assert m1[1,0] == 8
        assert m1[1,1] == 10
        assert m1[1,2] == 12
        assert m1[2,0] == 14
        assert m1[2,1] == 16
        assert m1[2,2] == 18
    
    def test_isub_exception(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        with pytest.raises(TypeError):
            m1 -= "1"
        
        with pytest.raises(TypeError):
            m1 -= [1]
        
        with pytest.raises(TypeError):
            m1 -= (1, 2)
    
    def test_imul_number(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m *= 2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[0,2] == 6
        assert m[1,0] == 8
        assert m[1,1] == 10
        assert m[1,2] == 12
        assert m[2,0] == 14
        assert m[2,1] == 16
        assert m[2,2] == 18
    
    def test_imul_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(1, 2, 3)
        m1 *= v1

        assert m1[0,0] == 1
        assert m1[0,1] == 4
        assert m1[0,2] == 9
        assert m1[1,0] == 4
        assert m1[1,1] == 10
        assert m1[1,2] == 18
        assert m1[2,0] == 7
        assert m1[2,1] == 16
        assert m1[2,2] == 27
    
    def test_imul_negative_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(-1, -2, -3)
        m1 *= v1

        assert m1[0,0] == -1
        assert m1[0,1] == -4
        assert m1[0,2] == -9
        assert m1[1,0] == -4
        assert m1[1,1] == -10
        assert m1[1,2] == -18
        assert m1[2,0] == -7
        assert m1[2,1] == -16
        assert m1[2,2] == -27
    
    def test_imul_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m1 *= m2

        assert m1[0,0] == 1
        assert m1[0,1] == 4
        assert m1[0,2] == 9
        assert m1[1,0] == 16
        assert m1[1,1] == 25
        assert m1[1,2] == 36
        assert m1[2,0] == 49
        assert m1[2,1] == 64
        assert m1[2,2] == 81
    
    def test_imul_negative_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]))
        m1 *= m2

        assert m1[0,0] == -1
        assert m1[0,1] == -4
        assert m1[0,2] == -9
        assert m1[1,0] == -16
        assert m1[1,1] == -25
        assert m1[1,2] == -36
        assert m1[2,0] == -49
        assert m1[2,1] == -64
        assert m1[2,2] == -81
    
    def test_imul_exception(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        with pytest.raises(TypeError):
            m1 *= "1"
        
        with pytest.raises(TypeError):
            m1 *= [1]
        
        with pytest.raises(TypeError):
            m1 *= (1, 2)
    
    def test_itruediv_number(self):
        m = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m /= 2.0

        assert m[0,0] == 0.5
        assert m[0,1] == 1
        assert m[0,2] == 1.5
        assert m[1,0] == 2
        assert m[1,1] == 2.5
        assert m[1,2] == 3
        assert m[2,0] == 3.5
        assert m[2,1] == 4
        assert m[2,2] == 4.5
    
    def test_itruediv_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(1, 2, 3)
        m1 /= v1

        assert m1[0,0] == 1
        assert m1[0,1] == 1
        assert m1[0,2] == 1
        assert m1[1,0] == 4
        assert m1[1,1] == 2.5
        assert m1[1,2] == 2
        assert m1[2,0] == 7
        assert m1[2,1] == 4
        assert m1[2,2] == 3

    
    def test_itruediv_negative_vec3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        v1 = Vec3(-1, -2, -3)
        m1 /= v1

        assert m1[0,0] == -1
        assert m1[0,1] == -1
        assert m1[0,2] == -1
        assert m1[1,0] == -4
        assert m1[1,1] == -2.5
        assert m1[1,2] == -2
        assert m1[2,0] == -7
        assert m1[2,1] == -4
        assert m1[2,2] == -3
    
    def test_itruediv_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m1 /= m2

        assert m1[0,0] == 1
        assert m1[0,1] == 1
        assert m1[0,2] == 1
        assert m1[1,0] == 1
        assert m1[1,1] == 1
        assert m1[1,2] == 1
        assert m1[2,0] == 1
        assert m1[2,1] == 1
        assert m1[2,2] == 1
    
    def test_itruediv_negative_mat3(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]))
        m1 /= m2

        assert m1[0,0] == -1
        assert m1[0,1] == -1
        assert m1[0,2] == -1
        assert m1[1,0] == -1
        assert m1[1,1] == -1
        assert m1[1,2] == -1
        assert m1[2,0] == -1
        assert m1[2,1] == -1
        assert m1[2,2] == -1
    
    def test_itruediv_exception(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        with pytest.raises(TypeError):
            m1 /= "1"
        
        with pytest.raises(TypeError):
            m1 /= [1]
        
        with pytest.raises(TypeError):
            m1 /= (1, 2)
    
    def test_dot(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m2 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        m = m1.dot(m2)

        assert m[0,0] == 30
        assert m[0,1] == 36
        assert m[0,2] == 42
        assert m[1,0] == 66
        assert m[1,1] == 81
        assert m[1,2] == 96
        assert m[2,0] == 102
        assert m[2,1] == 126
        assert m[2,2] == 150
    
    def test_dot_exception(self):
        m1 = Mat3(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        
        with pytest.raises(TypeError):
            m1.dot("1")
        
        with pytest.raises(TypeError):
            m1.dot([1])
        
        with pytest.raises(TypeError):
            m1.dot((1, 2))