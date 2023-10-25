
import pytest
from Atividade02.src.vectorized.Mat2 import Mat2
from Atividade02.src.vectorized.Vec2 import Vec2
import numpy as np


class TestMat2:

    def test_init(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))

        assert m[0,0] == 1
        assert m[0,1] == 2
        assert m[1,0] == 3
        assert m[1,1] == 4
    
    def test_init_excpetion(self):
        with pytest.raises(ValueError):
            Mat2(np.array([[1, 2], [3, 4], [5, 6]]))
        
        with pytest.raises(ValueError):
            Mat2(np.array([[1, 2], [3, 4, 5]]))
        
        with pytest.raises(TypeError):
            Mat2(1)
        
        with pytest.raises(TypeError):
            Mat2("1")
    
    def test_atribuition(self):
        m = Mat2()

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[1,0] == 0
        assert m[1,1] == 0

        m[0,0] = 1
        m[0,1] = 2
        m[1,0] = 3
        m[1,1] = 4
        
        assert m[0,0] == 1
        assert m[0,1] == 2
        assert m[1,0] == 3
        assert m[1,1] == 4
    
    def test_multiple_indexing(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))

        assert np.all(m[0] == np.array([1, 2]))
        assert np.all(m[1] == np.array([3, 4]))

        assert np.all(m[:,0] == np.array([1, 3]))
        assert np.all(m[:,1] == np.array([2, 4]))


    
    def test_negation(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m = -m

        assert m[0,0] == -1
        assert m[0,1] == -2
        assert m[1,0] == -3
        assert m[1,1] == -4
    
    def test_add_number(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m = m + 1

        assert m[0,0] == 2
        assert m[0,1] == 3
        assert m[1,0] == 4
        assert m[1,1] == 5

    def test_add_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([1, 2])
        m = m1 + v1

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[1,0] == 4
        assert m[1,1] == 6
    
    def test_add_negative_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([-1, -2])
        m = m1 + v1

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[1,0] == 2
        assert m[1,1] == 2
    
    def test_add_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[5, 6], [7, 8]]))
        m = m1 + m2

        assert m[0,0] == 6
        assert m[0,1] == 8
        assert m[1,0] == 10
        assert m[1,1] == 12
    
    def test_add_negative_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[-1, -2], [-3, -4]]))
        m = m1 + m2

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[1,0] == 0
        assert m[1,1] == 0
    
    def test_add_exception(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))

        with pytest.raises(TypeError):
            m1 + "1"
        
        with pytest.raises(TypeError):
            m1 + [1]
        
        with pytest.raises(TypeError):
            m1 + (1, 2)
    
    def test_add_integer_left_side(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m = 1 + m

        assert m[0,0] == 2
        assert m[0,1] == 3
        assert m[1,0] == 4
        assert m[1,1] == 5

    def test_add_vec2_left_side(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([1, 2])
        m = v1 + m1

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[1,0] == 4
        assert m[1,1] == 6



    def test_sub_number(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m = m - 1

        assert m[0,0] == 0
        assert m[0,1] == 1
        assert m[1,0] == 2
        assert m[1,1] == 3
    
    def test_sub_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([1, 2])
        m = m1 - v1

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[1,0] == 2
        assert m[1,1] == 2
    
    def test_sub_negative_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([-1, -2])
        m = m1 - v1

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[1,0] == 4
        assert m[1,1] == 6
    
    def test_sub_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[5, 6], [7, 8]]))
        m = m1 - m2

        assert m[0,0] == -4
        assert m[0,1] == -4
        assert m[1,0] == -4
        assert m[1,1] == -4
    
    def test_sub_negative_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[-1, -2], [-3, -4]]))
        m = m1 - m2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[1,0] == 6
        assert m[1,1] == 8
    
    def test_sub_exception(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))

        with pytest.raises(TypeError):
            m1 - "1"
        
        with pytest.raises(TypeError):
            m1 - [1]
        
        with pytest.raises(TypeError):
            m1 - (1, 2)
    
    def test_sub_integer_left_side(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m = 1 - m

        assert m[0,0] == 0
        assert m[0,1] == -1
        assert m[1,0] == -2
        assert m[1,1] == -3
    
    def test_sub_vec2_left_side(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([1, 2])
        m = v1 - m1

        assert m[0,0] == 0
        assert m[0,1] == 0
        assert m[1,0] == -2
        assert m[1,1] == -2


    
    def test_mul_number(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m = m * 2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[1,0] == 6
        assert m[1,1] == 8
    
    def test_mul_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([1, 2])
        m = m1 * v1

        assert m[0,0] == 1
        assert m[0,1] == 4
        assert m[1,0] == 3
        assert m[1,1] == 8
    
    def test_mul_negative_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([-1, -2])
        m = m1 * v1

        assert m[0,0] == -1
        assert m[0,1] == -4
        assert m[1,0] == -3
        assert m[1,1] == -8
    
    def test_mul_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[5, 6], [7, 8]]))
        m = m1 * m2

        assert m[0,0] == 5
        assert m[0,1] == 12
        assert m[1,0] == 21
        assert m[1,1] == 32
    
    def test_mul_negative_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[-5, -6], [-7, -8]]))
        m = m1 * m2

        assert m[0,0] == -5
        assert m[0,1] == -12
        assert m[1,0] == -21
        assert m[1,1] == -32
    
    def test_mul_exception(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))

        with pytest.raises(TypeError):
            m1 * "1"
        
        with pytest.raises(TypeError):
            m1 * [1]
        
        with pytest.raises(TypeError):
            m1 * (1, 2)
    
    def test_mul_integer_left_side(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m = 2 * m

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[1,0] == 6
        assert m[1,1] == 8
    
    def test_mul_vec2_left_side(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([1, 2])
        m = v1 * m1

        assert m[0,0] == 1
        assert m[0,1] == 4
        assert m[1,0] == 3
        assert m[1,1] == 8


    
    def test_div_number(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m = m / 2

        assert m[0,0] == 0.5
        assert m[0,1] == 1
        assert m[1,0] == 1.5
        assert m[1,1] == 2
    
    def test_div_vec2(self):
        m1 = Mat2(np.array([[4, 10], [12, 20]]))
        v1 = Vec2([4, 5])
        m = m1 / v1

        assert m[0,0] == 1
        assert m[0,1] == 2
        assert m[1,0] == 3
        assert m[1,1] == 4

    def test_div_negative_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([-1, -2])
        m = m1 / v1

        assert m[0,0] == -1
        assert m[0,1] == -1
        assert m[1,0] == -3
        assert m[1,1] == -2
    
    def test_div_mat2(self):
        m1 = Mat2(np.array([[4, 10], [12, 21]]))
        m2 = Mat2(np.array([[4, 5], [6, 7]]))
        m = m1 / m2

        assert m[0,0] == 1
        assert m[0,1] == 2
        assert m[1,0] == 2
        assert m[1,1] == 3
    
    def test_div_negative_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[-1, -2], [-3, -4]]))
        m = m1 / m2

        assert m[0,0] == -1
        assert m[0,1] == -1
        assert m[1,0] == -1
        assert m[1,1] == -1
    
    def test_div_exception(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))

        with pytest.raises(TypeError):
            m1 / "1"
        
        with pytest.raises(TypeError):
            m1 / [1]
        
        with pytest.raises(TypeError):
            m1 / (1, 2)
    
    def test_div_integer_left_side(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m = 2 / m

        assert m[0,0] == 2
        assert m[0,1] == 1
        assert m[1,0] == 2/3
        assert m[1,1] == 0.5
    
    def test_div_vec2_left_side(self):
        m1 = Mat2(np.array([[4, 10], [12, 20]]))
        v1 = Vec2([4, 5])
        m = v1 / m1

        assert m[0,0] == 1
        assert m[0,1] == 0.5
        assert m[1,0] == 1/3
        assert m[1,1] == 0.25

    
    def test_iadd_number(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m += 1

        assert m[0,0] == 2
        assert m[0,1] == 3
        assert m[1,0] == 4
        assert m[1,1] == 5
    
    def test_iadd_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([3, 4])
        m1 += v1

        assert m1[0,0] == 4
        assert m1[0,1] == 6
        assert m1[1,0] == 6
        assert m1[1,1] == 8
    
    def test_iadd_negative_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([-1, -2])
        m1 += v1

        assert m1[0,0] == 0
        assert m1[0,1] == 0
        assert m1[1,0] == 2
        assert m1[1,1] == 2
    
    def test_iadd_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[5, 6], [7, 8]]))
        m1 += m2

        assert m1[0,0] == 6
        assert m1[0,1] == 8
        assert m1[1,0] == 10
        assert m1[1,1] == 12
    
    def test_iadd_negative_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[-1, -2], [-3, -4]]))
        m1 += m2

        assert m1[0,0] == 0
        assert m1[0,1] == 0
        assert m1[1,0] == 0
        assert m1[1,1] == 0
    
    def test_iadd_exception(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))

        with pytest.raises(TypeError):
            m1 += "1"
        
        with pytest.raises(TypeError):
            m1 += [1]
        
        with pytest.raises(TypeError):
            m1 += (1, 2)
    

    
    def test_isub_number(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m -= 1

        assert m[0,0] == 0
        assert m[0,1] == 1
        assert m[1,0] == 2
        assert m[1,1] == 3
    
    def test_isub_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([3, 4])
        m1 -= v1

        assert m1[0,0] == -2
        assert m1[0,1] == -2
        assert m1[1,0] == 0
        assert m1[1,1] == 0
    
    def test_isub_negative_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([-1, -2])
        m1 -= v1

        assert m1[0,0] == 2
        assert m1[0,1] == 4
        assert m1[1,0] == 4
        assert m1[1,1] == 6
    
    def test_isub_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[5, 6], [7, 8]]))
        m1 -= m2

        assert m1[0,0] == -4
        assert m1[0,1] == -4
        assert m1[1,0] == -4
        assert m1[1,1] == -4
    
    def test_isub_negative_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[-1, -2], [-3, -4]]))
        m1 -= m2

        assert m1[0,0] == 2
        assert m1[0,1] == 4
        assert m1[1,0] == 6
        assert m1[1,1] == 8
    
    def test_isub_exception(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))

        with pytest.raises(TypeError):
            m1 -= "1"
        
        with pytest.raises(TypeError):
            m1 -= [1]
        
        with pytest.raises(TypeError):
            m1 -= (1, 2)
    


    def test_imul_number(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m *= 2

        assert m[0,0] == 2
        assert m[0,1] == 4
        assert m[1,0] == 6
        assert m[1,1] == 8
    
    def test_imul_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([3, 4])
        m1 *= v1

        assert m1[0,0] == 3
        assert m1[0,1] == 8
        assert m1[1,0] == 9
        assert m1[1,1] == 16
    
    def test_imul_negative_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([-1, -2])
        m1 *= v1

        assert m1[0,0] == -1
        assert m1[0,1] == -4
        assert m1[1,0] == -3
        assert m1[1,1] == -8
    
    def test_imul_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[5, 6], [7, 8]]))
        m1 *= m2

        assert m1[0,0] == 5
        assert m1[0,1] == 12
        assert m1[1,0] == 21
        assert m1[1,1] == 32
    
    def test_imul_negative_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[-5, -6], [-7, -8]]))
        m1 *= m2

        assert m1[0,0] == -5
        assert m1[0,1] == -12
        assert m1[1,0] == -21
        assert m1[1,1] == -32
    
    def test_imul_exception(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))

        with pytest.raises(TypeError):
            m1 *= "1"
        
        with pytest.raises(TypeError):
            m1 *= [1]
        
        with pytest.raises(TypeError):
            m1 *= (1, 2)
    

    
    def test_itruediv_number(self):
        m = Mat2(np.array([[1, 2], [3, 4]]))
        m /= 2.0

        assert m[0,0] == 0.5
        assert m[0,1] == 1
        assert m[1,0] == 1.5
        assert m[1,1] == 2
    
    def test_itruediv_vec2(self):
        m1 = Mat2(np.array([[4, 10], [12, 20]]))
        v1 = Vec2([4, 5])
        m1 /= v1

        assert m1[0,0] == 1
        assert m1[0,1] == 2
        assert m1[1,0] == 3
        assert m1[1,1] == 4
    
    def test_itruediv_negative_vec2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        v1 = Vec2([-1, -2])
        m1 /= v1

        assert m1[0,0] == -1
        assert m1[0,1] == -1
        assert m1[1,0] == -3
        assert m1[1,1] == -2
    
    def test_itruediv_mat2(self):
        m1 = Mat2(np.array([[4, 10], [12, 21]]))
        m2 = Mat2(np.array([[4, 5], [6, 7]]))
        m1 /= m2

        assert m1[0,0] == 1
        assert m1[0,1] == 2
        assert m1[1,0] == 2
        assert m1[1,1] == 3
    
    def test_itruediv_negative_mat2(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[-1, -2], [-3, -4]]))
        m1 /= m2

        assert m1[0,0] == -1
        assert m1[0,1] == -1
        assert m1[1,0] == -1
        assert m1[1,1] == -1
    
    def test_itruediv_exception(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))

        with pytest.raises(TypeError):
            m1 /= "1"
        
        with pytest.raises(TypeError):
            m1 /= [1]
        
        with pytest.raises(TypeError):
            m1 /= (1, 2)
    

    
    def test_dot(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))
        m2 = Mat2(np.array([[5, 6], [7, 8]]))
        m = m1.dot(m2)

        assert m[0,0] == 19
        assert m[0,1] == 22
        assert m[1,0] == 43
        assert m[1,1] == 50
    
    def test_dot_exception(self):
        m1 = Mat2(np.array([[1, 2], [3, 4]]))

        with pytest.raises(TypeError):
            m1.dot("1")
        
        with pytest.raises(TypeError):
            m1.dot([1])
        
        with pytest.raises(TypeError):
            m1.dot((1, 2))