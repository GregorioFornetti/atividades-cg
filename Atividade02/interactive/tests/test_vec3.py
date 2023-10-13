
from Atividade02.interactive.Vec3 import Vec3

class TestVec3:

    def test_init(self):
        v = Vec3(1, 2, 3)

        assert v.x == 1
        assert v.y == 2
        assert v.z == 3
    
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