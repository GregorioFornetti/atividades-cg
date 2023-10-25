
import pytest
from Atividade02.src.interactive.Vec4 import Vec4
import numpy as np


class TestVec4:

    def test_init(self):
        v = Vec4(1, 2, 3, 4)

        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
        assert v.w == 4
    
    def test_init_excpetion(self):
        with pytest.raises(TypeError):
            Vec4(1, 2, 3, 4, 5)
        
        with pytest.raises(TypeError):
            Vec4([1], 2, 3, 4)
        
        with pytest.raises(TypeError):
            Vec4("1", 2, 3, 4)
        
        with pytest.raises(TypeError):
            Vec4(1, [2], 3, 4)

        with pytest.raises(TypeError):
            Vec4(1, "2", 3, 4)
        
        with pytest.raises(TypeError):
            Vec4(1, 2, [3], 4)
        
        with pytest.raises(TypeError):
            Vec4(1, 2, "3", 4)
        
        with pytest.raises(TypeError):
            Vec4(1, 2, 3, [4])
        
        with pytest.raises(TypeError):
            Vec4(1, 2, 3, "4")
    
    def test_xyz_atribuition(self):
        v = Vec4()

        assert v.x == 0
        assert v.y == 0
        assert v.z == 0
        assert v.w == 0

        v.x = 1
        v.y = 2
        v.z = 3
        v.w = 4
        
        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
        assert v.w == 4
    
    def test_negation(self):
        v = Vec4(1, 2, 3, 4)
        v = -v

        assert v.x == -1
        assert v.y == -2
        assert v.z == -3
        assert v.w == -4
    
    def test_getitem(self):
        v = Vec4(1, 2, 3, 4)

        assert v[0] == 1
        assert v[1] == 2
        assert v[2] == 3
        assert v[3] == 4
    
    def test_add_number(self):
        v = Vec4(1, 2, 3, 4)
        v = v + 1

        assert v.x == 2
        assert v.y == 3
        assert v.z == 4
        assert v.w == 5

    def test_add_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(5, 6, 7, 8)
        v = v1 + v2

        assert v.x == 6
        assert v.y == 8
        assert v.z == 10
        assert v.w == 12
    
    def test_add_negative_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(-1, -2, -3, -4)
        v = v1 + v2

        assert v.x == 0
        assert v.y == 0
        assert v.z == 0
        assert v.w == 0
    
    def test_add_exception(self):
        v1 = Vec4(1, 2, 3, 4)

        with pytest.raises(TypeError):
            v1 + "1"
        
        with pytest.raises(TypeError):
            v1 + [1]
        
        with pytest.raises(TypeError):
            v1 + (1, 2)
    
    def test_add_integer_left_side(self):
        v = Vec4(1, 2, 3, 4)
        v = 1 + v

        assert v.x == 2
        assert v.y == 3
        assert v.z == 4
        assert v.w == 5
    

    
    def test_sub_number(self):
        v = Vec4(1, 2, 3, 4)
        v = v - 1

        assert v.x == 0
        assert v.y == 1
        assert v.z == 2
        assert v.w == 3
    
    def test_sub_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(5, 6, 7, 8)
        v = v1 - v2

        assert v.x == -4
        assert v.y == -4
        assert v.z == -4
        assert v.w == -4
    
    def test_sub_negative_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(-1, -2, -3, -4)
        v = v1 - v2

        assert v.x == 2
        assert v.y == 4
        assert v.z == 6
        assert v.w == 8
    
    def test_sub_exception(self):
        v1 = Vec4(1, 2, 3, 4)

        with pytest.raises(TypeError):
            v1 - "1"
        
        with pytest.raises(TypeError):
            v1 - [1]
        
        with pytest.raises(TypeError):
            v1 - (1, 2)
    
    def test_sub_integer_left_side(self):
        v = Vec4(1, 2, 3, 4)
        v = 1 - v

        assert v.x == 0
        assert v.y == -1
        assert v.z == -2
        assert v.w == -3
    

    
    def test_mul_number(self):
        v = Vec4(1, 2, 3, 4)
        v = v * 2

        assert v.x == 2
        assert v.y == 4
        assert v.z == 6
        assert v.w == 8
    
    def test_mul_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(5, 6, 7, 8)
        v = v1 * v2

        assert v.x == 5
        assert v.y == 12
        assert v.z == 21
        assert v.w == 32
    
    def test_mul_negative_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(-1, -2, -3, -4)
        v = v1 * v2

        assert v.x == -1
        assert v.y == -4
        assert v.z == -9
        assert v.w == -16
    
    def test_mul_exception(self):
        v1 = Vec4(1, 2, 3, 4)

        with pytest.raises(TypeError):
            v1 * "1"
        
        with pytest.raises(TypeError):
            v1 * [1]
        
        with pytest.raises(TypeError):
            v1 * (1, 2)
    
    def test_mul_integer_left_side(self):
        v = Vec4(1, 2, 3, 4)
        v = 2 * v

        assert v.x == 2
        assert v.y == 4
        assert v.z == 6
        assert v.w == 8
    

    
    def test_div_number(self):
        v = Vec4(2, 4, 6, 8)
        v = v / 2

        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
        assert v.w == 4
    
    def test_div_vec4(self):
        v1 = Vec4(4, 10, 18, 28)
        v2 = Vec4(4, 5, 6, 7)
        v = v1 / v2

        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
        assert v.w == 4
    
    def test_div_negative_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(-1, -2, -3, -4)
        v = v1 / v2

        assert v.x == -1
        assert v.y == -1
        assert v.z == -1
        assert v.w == -1
    
    def test_div_exception(self):
        v1 = Vec4(1, 2, 3, 4)

        with pytest.raises(TypeError):
            v1 / "1"
        
        with pytest.raises(TypeError):
            v1 / [1]
        
        with pytest.raises(TypeError):
            v1 / (1, 2)
    
    def test_div_integer_left_side(self):
        v = Vec4(2, 4, 6, 8)
        v = 2 / v

        assert v.x == 1
        assert v.y == 1 / 2
        assert v.z == 1 / 3
        assert v.w == 1 / 4
    

    
    def test_iadd_number(self):
        v = Vec4(1, 2, 3, 4)
        v += 1

        assert v.x == 2
        assert v.y == 3
        assert v.z == 4
        assert v.w == 5
    
    def test_iadd_Vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(5, 6, 7, 8)
        v1 += v2

        assert v1.x == 6
        assert v1.y == 8
        assert v1.z == 10
        assert v1.w == 12
    
    def test_iadd_negative_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(-1, -2, -3, -4)
        v1 += v2

        assert v1.x == 0
        assert v1.y == 0
        assert v1.z == 0
        assert v1.w == 0
    
    def test_iadd_exception(self):
        v1 = Vec4(1, 2, 3, 4)

        with pytest.raises(TypeError):
            v1 += "1"
        
        with pytest.raises(TypeError):
            v1 += [1]
        
        with pytest.raises(TypeError):
            v1 += (1, 2)
    
    def test_isub_number(self):
        v = Vec4(1, 2, 3, 4)
        v -= 1

        assert v.x == 0
        assert v.y == 1
        assert v.z == 2
        assert v.w == 3
    
    def test_isub_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(5, 6, 7, 8)
        v1 -= v2

        assert v1.x == -4
        assert v1.y == -4
        assert v1.z == -4
        assert v1.w == -4
    
    def test_isub_negative_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(-1, -2, -3, -4)
        v1 -= v2

        assert v1.x == 2
        assert v1.y == 4
        assert v1.z == 6
        assert v1.w == 8
    
    def test_isub_exception(self):
        v1 = Vec4(1, 2, 3, 4)

        with pytest.raises(TypeError):
            v1 -= "1"
        
        with pytest.raises(TypeError):
            v1 -= [1]
        
        with pytest.raises(TypeError):
            v1 -= (1, 2)
    
    def test_imul_number(self):
        v = Vec4(1, 2, 3, 4)
        v *= 2

        assert v.x == 2
        assert v.y == 4
        assert v.z == 6
        assert v.w == 8
    
    def test_imul_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(5, 6, 7, 8)
        v1 *= v2

        assert v1.x == 5
        assert v1.y == 12
        assert v1.z == 21
        assert v1.w == 32
    
    def test_imul_negative_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(-1, -2, -3, -4)
        v1 *= v2

        assert v1.x == -1
        assert v1.y == -4
        assert v1.z == -9
        assert v1.w == -16
    
    def test_imul_exception(self):
        v1 = Vec4(1, 2, 3, 4)

        with pytest.raises(TypeError):
            v1 *= "1"
        
        with pytest.raises(TypeError):
            v1 *= [1]
        
        with pytest.raises(TypeError):
            v1 *= (1, 2)
    
    def test_itruediv_number(self):
        v = Vec4(2, 4, 6, 8)
        v /= 2

        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
        assert v.w == 4
    
    def test_itruediv_vec4(self):
        v1 = Vec4(4, 10, 18, 28)
        v2 = Vec4(4, 5, 6, 7)
        v1 /= v2

        assert v1.x == 1
        assert v1.y == 2
        assert v1.z == 3
        assert v1.w == 4
    
    def test_itruediv_negative_vec4(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(-1, -2, -3, -4)
        v1 /= v2

        assert v1.x == -1
        assert v1.y == -1
        assert v1.z == -1
        assert v1.w == -1
    
    def test_itruediv_exception(self):
        v1 = Vec4(1, 2, 3, 4)

        with pytest.raises(TypeError):
            v1 /= "1"
        
        with pytest.raises(TypeError):
            v1 /= [1]
        
        with pytest.raises(TypeError):
            v1 /= (1, 2)
    
    def test_length(self):
        v = Vec4(1, 2, 3, 4)

        assert v.length() == np.sqrt(1 ** 2 + 2 ** 2 + 3 ** 2 + 4 ** 2)
    
    def test_squared_length(self):
        v = Vec4(1, 2, 3, 4)

        assert v.squared_length() == 1 ** 2 + 2 ** 2 + 3 ** 2 + 4 ** 2
    
    def test_dot(self):
        v1 = Vec4(1, 2, 3, 4)
        v2 = Vec4(5, 6, 7, 8)

        assert v1.dot(v2) == 1 * 5 + 2 * 6 + 3 * 7 + 4 * 8
    
    def test_dot_exception(self):
        v1 = Vec4(1, 2, 3, 4)

        with pytest.raises(TypeError):
            v1.dot("1")
        
        with pytest.raises(TypeError):
            v1.dot([1])
        
        with pytest.raises(TypeError):
            v1.dot((1, 2))
    
    def test_unit_vector(self):
        v = Vec4(1, 2, 3, 4)
        v = v.unit_vector()

        assert v.x == 1 / np.sqrt(1 ** 2 + 2 ** 2 + 3 ** 2 + 4 ** 2)
        assert v.y == 2 / np.sqrt(1 ** 2 + 2 ** 2 + 3 ** 2 + 4 ** 2)
        assert v.z == 3 / np.sqrt(1 ** 2 + 2 ** 2 + 3 ** 2 + 4 ** 2)
