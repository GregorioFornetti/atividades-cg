
import pytest
from Atividade02.src.vectorized.Vec3 import Vec3, Color
import numpy as np


class TestVec3:

    def test_init(self):
        v = Vec3([1, 2, 3])

        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
    
    def test_init_exception(self):
        with pytest.raises(ValueError):
            Vec3([1, 2])
        
        with pytest.raises(ValueError):
            Vec3([[1], 2])
        
        with pytest.raises(TypeError):
            Vec3("1")
        
        with pytest.raises(TypeError):
            Vec3(1)
    
    def test_xyz_atribuition(self):
        v = Vec3()

        assert v.x == 0
        assert v.y == 0
        assert v.z == 0

        v.x = 1
        v.y = 2
        v.z = 3
        
        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
    
    def test_negation(self):
        v = Vec3([1, 2, 3])
        v = -v

        assert v.x == -1
        assert v.y == -2
        assert v.z == -3
    
    def test_getitem(self):
        v = Vec3([1, 2, 3])

        assert v[0] == 1
        assert v[1] == 2
        assert v[2] == 3
    
    def test_add_number(self):
        v = Vec3([1, 2, 3])
        v = v + 1

        assert v.x == 2
        assert v.y == 3
        assert v.z == 4

    def test_add_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([4, 5, 6])
        v = v1 + v2

        assert v.x == 5
        assert v.y == 7
        assert v.z == 9
    
    def test_add_negative_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([-1, -2, -3])
        v = v1 + v2

        assert v.x == 0
        assert v.y == 0
        assert v.z == 0
    
    def test_add_exception(self):
        v1 = Vec3([1, 2, 3])

        with pytest.raises(TypeError):
            v1 + "1"
        
        with pytest.raises(TypeError):
            v1 + [1]
        
        with pytest.raises(TypeError):
            v1 + (1, 2)
    
    def test_add_integer_left_side(self):
        v = Vec3([1,2,3])
        v = 1 + v

        assert v.x == 2
        assert v.y == 3
        assert v.z == 4
    


    def test_sub_number(self):
        v = Vec3([1, 2, 3])
        v = v - 1

        assert v.x == 0
        assert v.y == 1
        assert v.z == 2
    
    def test_sub_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([4, 5, 6])
        v = v1 - v2

        assert v.x == -3
        assert v.y == -3
        assert v.z == -3
    
    def test_sub_negative_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([-1, -2, -3])
        v = v1 - v2

        assert v.x == 2
        assert v.y == 4
        assert v.z == 6
    
    def test_sub_exception(self):
        v1 = Vec3([1, 2, 3])

        with pytest.raises(TypeError):
            v1 - "1"
        
        with pytest.raises(TypeError):
            v1 - [1]
        
        with pytest.raises(TypeError):
            v1 - (1, 2)
    
    def test_sub_integer_left_side(self):
        v = Vec3([1,2,3])
        v = 1 - v

        assert v.x == 0
        assert v.y == -1
        assert v.z == -2
    

    
    def test_mul_number(self):
        v = Vec3([1, 2, 3])
        v = v * 2

        assert v.x == 2
        assert v.y == 4
        assert v.z == 6
    
    def test_mul_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([4, 5, 6])
        v = v1 * v2

        assert v.x == 4
        assert v.y == 10
        assert v.z == 18
    
    def test_mul_negative_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([-1, -2, -3])
        v = v1 * v2

        assert v.x == -1
        assert v.y == -4
        assert v.z == -9

    def test_mul_exception(self):
        v1 = Vec3([1, 2, 3])

        with pytest.raises(TypeError):
            v1 * "1"
        
        with pytest.raises(TypeError):
            v1 * [1]
        
        with pytest.raises(TypeError):
            v1 * (1, 2)
    
    def test_mul_integer_left_side(self):
        v = Vec3([1,2,3])
        v = 2 * v

        assert v.x == 2
        assert v.y == 4
        assert v.z == 6
    

    
    def test_div_number(self):
        v = Vec3([2, 4, 6])
        v = v / 2

        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
    
    def test_div_vec3(self):
        v1 = Vec3([4, 10, 18])
        v2 = Vec3([4, 5, 6])
        v = v1 / v2

        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
    
    def test_div_negative_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([-1, -2, -3])
        v = v1 / v2

        assert v.x == -1
        assert v.y == -1
        assert v.z == -1
    
    def test_div_exception(self):
        v1 = Vec3([1, 2, 3])

        with pytest.raises(TypeError):
            v1 / "1"
        
        with pytest.raises(TypeError):
            v1 / [1]
        
        with pytest.raises(TypeError):
            v1 / (1, 2)
        
    def test_div_integer_left_side(self):
        v = Vec3([2,4,6])
        v = 2 / v

        assert v.x == 1
        assert v.y == 0.5
        assert v.z == 1/3
    
    
    
    def test_iadd_number(self):
        v = Vec3([1, 2, 3])
        v += 1

        assert v.x == 2
        assert v.y == 3
        assert v.z == 4
    
    def test_iadd_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([4, 5, 6])
        v1 += v2

        assert v1.x == 5
        assert v1.y == 7
        assert v1.z == 9
    
    def test_iadd_negative_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([-1, -2, -3])
        v1 += v2

        assert v1.x == 0
        assert v1.y == 0
        assert v1.z == 0
    
    def test_iadd_exception(self):
        v1 = Vec3([1, 2, 3])

        with pytest.raises(TypeError):
            v1 += "1"
        
        with pytest.raises(TypeError):
            v1 += [1]
        
        with pytest.raises(TypeError):
            v1 += (1, 2)
    
    def test_isub_number(self):
        v = Vec3([1, 2, 3])
        v -= 1

        assert v.x == 0
        assert v.y == 1
        assert v.z == 2
    
    def test_isub_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([4, 5, 6])
        v1 -= v2

        assert v1.x == -3
        assert v1.y == -3
        assert v1.z == -3
    
    def test_isub_negative_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([-1, -2, -3])
        v1 -= v2

        assert v1.x == 2
        assert v1.y == 4
        assert v1.z == 6
    
    def test_isub_exception(self):
        v1 = Vec3([1, 2, 3])

        with pytest.raises(TypeError):
            v1 -= "1"
        
        with pytest.raises(TypeError):
            v1 -= [1]
        
        with pytest.raises(TypeError):
            v1 -= (1, 2)
    
    def test_imul_number(self):
        v = Vec3([1, 2, 3])
        v *= 2

        assert v.x == 2
        assert v.y == 4
        assert v.z == 6
    
    def test_imul_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([4, 5, 6])
        v1 *= v2

        assert v1.x == 4
        assert v1.y == 10
        assert v1.z == 18
    
    def test_imul_negative_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([-1, -2, -3])
        v1 *= v2

        assert v1.x == -1
        assert v1.y == -4
        assert v1.z == -9
    
    def test_imul_exception(self):
        v1 = Vec3([1, 2, 3])

        with pytest.raises(TypeError):
            v1 *= "1"
        
        with pytest.raises(TypeError):
            v1 *= [1]
        
        with pytest.raises(TypeError):
            v1 *= (1, 2)
    
    def test_itruediv_number(self):
        v = Vec3([2, 4, 6])
        v /= 2

        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
    
    def test_itruediv_vec3(self):
        v1 = Vec3([4, 10, 18])
        v2 = Vec3([4, 5, 6])
        v1 /= v2

        assert v1.x == 1
        assert v1.y == 2
        assert v1.z == 3
    
    def test_itruediv_negative_vec3(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([-1, -2, -3])
        v1 /= v2

        assert v1.x == -1
        assert v1.y == -1
        assert v1.z == -1
    
    def test_itruediv_exception(self):
        v1 = Vec3([1, 2, 3])

        with pytest.raises(TypeError):
            v1 /= "1"
        
        with pytest.raises(TypeError):
            v1 /= [1]
        
        with pytest.raises(TypeError):
            v1 /= (1, 2)
    
    def test_length(self):
        v = Vec3([1, 2, 3])

        assert v.length() == np.sqrt(1 ** 2 + 2 ** 2 + 3 ** 2)
    
    def test_squared_length(self):
        v = Vec3([1, 2, 3])

        assert v.squared_length() == 1 ** 2 + 2 ** 2 + 3 ** 2
    
    def test_dot(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([4, 5, 6])

        assert v1.dot(v2) == 1 * 4 + 2 * 5 + 3 * 6
    
    def test_dot_exception(self):
        v1 = Vec3([1, 2, 3])

        with pytest.raises(TypeError):
            v1.dot("1")
        
        with pytest.raises(TypeError):
            v1.dot([1])
        
        with pytest.raises(TypeError):
            v1.dot((1, 2))
    
    def test_cross(self):
        v1 = Vec3([1, 2, 3])
        v2 = Vec3([4, 5, 6])
        v = v1.cross(v2)

        assert v.x == 2 * 6 - 3 * 5
        assert v.y == 3 * 4 - 1 * 6
        assert v.z == 1 * 5 - 2 * 4
    
    def test_cross_exception(self):
        v1 = Vec3([1, 2, 3])

        with pytest.raises(TypeError):
            v1.cross("1")
        
        with pytest.raises(TypeError):
            v1.cross([1])
        
        with pytest.raises(TypeError):
            v1.cross((1, 2))
    
    def test_unit_vector(self):
        v = Vec3([1, 2, 3])
        v = v.unit_vector()

        assert v.x == 1 / np.sqrt(1 ** 2 + 2 ** 2 + 3 ** 2)
        assert v.y == 2 / np.sqrt(1 ** 2 + 2 ** 2 + 3 ** 2)
        assert v.z == 3 / np.sqrt(1 ** 2 + 2 ** 2 + 3 ** 2)

    def test_color(self):
        c = Color([1, 2, 3])

        assert c.r == 1
        assert c.g == 2
        assert c.b == 3