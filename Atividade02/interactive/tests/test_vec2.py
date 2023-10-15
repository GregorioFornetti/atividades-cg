
import pytest
from Atividade02.interactive.Vec2 import Vec2
import numpy as np


class TestVec2:

    def test_init(self):
        v = Vec2(1, 2)

        assert v.x == 1
        assert v.y == 2
    
    def test_init_excpetion(self):
        with pytest.raises(TypeError):
            Vec2(1, 2, 3)
        
        with pytest.raises(TypeError):
            Vec2([1], 2)
        
        with pytest.raises(TypeError):
            Vec2("1", 2)
        
        with pytest.raises(TypeError):
            Vec2(1, [2])

        with pytest.raises(TypeError):
            Vec2(1, "2")
        
    def test_xyz_atribuition(self):
        v = Vec2()

        assert v.x == 0
        assert v.y == 0

        v.x = 1
        v.y = 2
        
        assert v.x == 1
        assert v.y == 2
    
    def test_negation(self):
        v = Vec2(1, 2)
        v = -v

        assert v.x == -1
        assert v.y == -2
    
    def test_getitem(self):
        v = Vec2(1, 2)

        assert v[0] == 1
        assert v[1] == 2
    
    def test_add_number(self):
        v = Vec2(1, 2)
        v = v + 1

        assert v.x == 2
        assert v.y == 3

    def test_add_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(3, 4)
        v = v1 + v2

        assert v.x == 4
        assert v.y == 6
    
    def test_add_negative_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(-1, -2)
        v = v1 + v2

        assert v.x == 0
        assert v.y == 0
    
    def test_add_exception(self):
        v1 = Vec2(1, 2)

        with pytest.raises(TypeError):
            v1 + "1"
        
        with pytest.raises(TypeError):
            v1 + [1]
        
        with pytest.raises(TypeError):
            v1 + (1, 2)
    
    def test_sub_number(self):
        v = Vec2(1, 2)
        v = v - 1

        assert v.x == 0
        assert v.y == 1
    
    def test_sub_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(3, 4)
        v = v1 - v2

        assert v.x == -2
        assert v.y == -2
    
    def test_sub_negative_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(-1, -2)
        v = v1 - v2

        assert v.x == 2
        assert v.y == 4
    
    def test_sub_exception(self):
        v1 = Vec2(1, 2)

        with pytest.raises(TypeError):
            v1 - "1"
        
        with pytest.raises(TypeError):
            v1 - [1]
        
        with pytest.raises(TypeError):
            v1 - (1, 2)
    
    def test_mul_number(self):
        v = Vec2(1, 2)
        v = v * 2

        assert v.x == 2
        assert v.y == 4
    
    def test_mul_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(3, 4)
        v = v1 * v2

        assert v.x == 3
        assert v.y == 8
    
    def test_mul_negative_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(-1, -2)
        v = v1 * v2

        assert v.x == -1
        assert v.y == -4
    
    def test_mul_exception(self):
        v1 = Vec2(1, 2)

        with pytest.raises(TypeError):
            v1 * "1"
        
        with pytest.raises(TypeError):
            v1 * [1]
        
        with pytest.raises(TypeError):
            v1 * (1, 2)
    
    def test_div_number(self):
        v = Vec2(2, 4)
        v = v / 2

        assert v.x == 1
        assert v.y == 2
    
    def test_div_vec2(self):
        v1 = Vec2(4, 10)
        v2 = Vec2(4, 5)
        v = v1 / v2

        assert v.x == 1
        assert v.y == 2
    
    def test_div_negative_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(-1, -2)
        v = v1 / v2

        assert v.x == -1
        assert v.y == -1
    
    def test_div_exception(self):
        v1 = Vec2(1, 2)

        with pytest.raises(TypeError):
            v1 / "1"
        
        with pytest.raises(TypeError):
            v1 / [1]
        
        with pytest.raises(TypeError):
            v1 / (1, 2)
    
    def test_iadd_number(self):
        v = Vec2(1, 2)
        v += 1

        assert v.x == 2
        assert v.y == 3
    
    def test_iadd_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(3, 4)
        v1 += v2

        assert v1.x == 4
        assert v1.y == 6
    
    def test_iadd_negative_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(-1, -2)
        v1 += v2

        assert v1.x == 0
        assert v1.y == 0
    
    def test_iadd_exception(self):
        v1 = Vec2(1, 2)

        with pytest.raises(TypeError):
            v1 += "1"
        
        with pytest.raises(TypeError):
            v1 += [1]
        
        with pytest.raises(TypeError):
            v1 += (1, 2)
    
    def test_isub_number(self):
        v = Vec2(1, 2)
        v -= 1

        assert v.x == 0
        assert v.y == 1
    
    def test_isub_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(3, 4)
        v1 -= v2

        assert v1.x == -2
        assert v1.y == -2
    
    def test_isub_negative_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(-1, -2)
        v1 -= v2

        assert v1.x == 2
        assert v1.y == 4
    
    def test_isub_exception(self):
        v1 = Vec2(1, 2)

        with pytest.raises(TypeError):
            v1 -= "1"
        
        with pytest.raises(TypeError):
            v1 -= [1]
        
        with pytest.raises(TypeError):
            v1 -= (1, 2)
    
    def test_imul_number(self):
        v = Vec2(1, 2)
        v *= 2

        assert v.x == 2
        assert v.y == 4
    
    def test_imul_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(3, 4)
        v1 *= v2

        assert v1.x == 3
        assert v1.y == 8
    
    def test_imul_negative_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(-1, -2)
        v1 *= v2

        assert v1.x == -1
        assert v1.y == -4
    
    def test_imul_exception(self):
        v1 = Vec2(1, 2)

        with pytest.raises(TypeError):
            v1 *= "1"
        
        with pytest.raises(TypeError):
            v1 *= [1]
        
        with pytest.raises(TypeError):
            v1 *= (1, 2)
    
    def test_itruediv_number(self):
        v = Vec2(2, 4)
        v /= 2

        assert v.x == 1
        assert v.y == 2
    
    def test_itruediv_vec2(self):
        v1 = Vec2(4, 10)
        v2 = Vec2(4, 5)
        v1 /= v2

        assert v1.x == 1
        assert v1.y == 2
    
    def test_itruediv_negative_vec2(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(-1, -2)
        v1 /= v2

        assert v1.x == -1
        assert v1.y == -1
    
    def test_itruediv_exception(self):
        v1 = Vec2(1, 2)

        with pytest.raises(TypeError):
            v1 /= "1"
        
        with pytest.raises(TypeError):
            v1 /= [1]
        
        with pytest.raises(TypeError):
            v1 /= (1, 2)
    
    def test_length(self):
        v = Vec2(1, 2)

        assert v.length() == np.sqrt(1 ** 2 + 2 ** 2)
    
    def test_squared_length(self):
        v = Vec2(1, 2)

        assert v.squared_length() == 1 ** 2 + 2 ** 2
    
    def test_dot(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(3, 4)

        assert v1.dot(v2) == 1 * 3 + 2 * 4
    
    def test_dot_exception(self):
        v1 = Vec2(1, 2)

        with pytest.raises(TypeError):
            v1.dot("1")
        
        with pytest.raises(TypeError):
            v1.dot([1])
        
        with pytest.raises(TypeError):
            v1.dot((1, 2))
    
    def test_cross(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(3, 4)
        res = v1.cross(v2)

        assert res == 1 * 4 - 2 * 3
    
    def test_cross_exception(self):
        v1 = Vec2(1, 2)

        with pytest.raises(TypeError):
            v1.cross("1")
        
        with pytest.raises(TypeError):
            v1.cross([1])
        
        with pytest.raises(TypeError):
            v1.cross((1, 2))
    
    def test_unit_vector(self):
        v = Vec2(1, 2)
        v = v.unit_vector()

        assert v.x == 1 / np.sqrt(1 ** 2 + 2 ** 2)
        assert v.y == 2 / np.sqrt(1 ** 2 + 2 ** 2)
