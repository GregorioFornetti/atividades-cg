
from Atividade03.src.Model import Model
import pytest

class TestLoadObjs:

    def make_model_basic_assertions(self, model: Model):
        assert len(model.vertexes) == 3
        assert len(model.faces) == 1

        assert model.vertexes[0].x == 1.0
        assert model.vertexes[0].y == 2.0
        assert model.vertexes[0].z == 3.0

        assert model.vertexes[1].x == 4.0
        assert model.vertexes[1].y == 5.0
        assert model.vertexes[1].z == 6.0

        assert model.vertexes[2].x == 7.0
        assert model.vertexes[2].y == 8.0
        assert model.vertexes[2].z == 9.0

        assert model.faces[0].vertex_1.x == 1.0
        assert model.faces[0].vertex_1.y == 2.0
        assert model.faces[0].vertex_1.z == 3.0
        assert model.faces[0].vertex_2.x == 4.0
        assert model.faces[0].vertex_2.y == 5.0
        assert model.faces[0].vertex_2.z == 6.0
        assert model.faces[0].vertex_3.x == 7.0
        assert model.faces[0].vertex_3.y == 8.0
        assert model.faces[0].vertex_3.z == 9.0
    
    def test_load_only_vertex(self):
        model = Model('Atividade03/objs/TestOnlyVertexFace.obj')

        self.make_model_basic_assertions(model)

    def test_load_vertex_and_texture(self):
        model = Model('Atividade03/objs/TestVertexAndTexture.obj')

        self.make_model_basic_assertions(model)
    
    def test_load_vertex_and_normal(self):
        model = Model('Atividade03/objs/TestVertexAndTexture.obj')

        self.make_model_basic_assertions(model)
    
    def test_load_vertex_texture_normal(self):
        model = Model('Atividade03/objs/TestVertexTextureNornal.obj')

        self.make_model_basic_assertions(model)
    
    def test_load_four_coord_vertex_obj(self):
        model = Model('Atividade03/objs/TestFourCoordVertexes.obj')

        self.make_model_basic_assertions(model)
    
    def test_load_not_triangle(self):
        with pytest.raises(Exception):
            Model('Atividade03/objs/NotTriangle.obj')


    def test_load_cube(self):
        model = Model('Atividade03/objs/cube.obj')

        assert len(model.vertexes) == 8
        assert len(model.faces) == 12

        assert model.vertexes[0].x == 0.0
        assert model.vertexes[0].y == 0.0
        assert model.vertexes[0].z == 0.0

        assert model.vertexes[1].x == 0.0
        assert model.vertexes[1].y == 0.0
        assert model.vertexes[1].z == 1.0

        assert model.vertexes[2].x == 0.0
        assert model.vertexes[2].y == 1.0
        assert model.vertexes[2].z == 0.0

        assert model.vertexes[3].x == 0.0
        assert model.vertexes[3].y == 1.0
        assert model.vertexes[3].z == 1.0

        assert model.vertexes[4].x == 1.0
        assert model.vertexes[4].y == 0.0
        assert model.vertexes[4].z == 0.0

        assert model.vertexes[5].x == 1.0
        assert model.vertexes[5].y == 0.0
        assert model.vertexes[5].z == 1.0

        assert model.vertexes[6].x == 1.0
        assert model.vertexes[6].y == 1.0
        assert model.vertexes[6].z == 0.0

        assert model.vertexes[7].x == 1.0
        assert model.vertexes[7].y == 1.0
        assert model.vertexes[7].z == 1.0

        assert model.faces[0].vertex_1.x == 0.0
        assert model.faces[0].vertex_1.y == 0.0
        assert model.faces[0].vertex_1.z == 0.0
        assert model.faces[0].vertex_2.x == 1.0
        assert model.faces[0].vertex_2.y == 1.0
        assert model.faces[0].vertex_2.z == 0.0
        assert model.faces[0].vertex_3.x == 1.0
        assert model.faces[0].vertex_3.y == 0.0
        assert model.faces[0].vertex_3.z == 0.0

        assert model.faces[1].vertex_1.x == 0.0
        assert model.faces[1].vertex_1.y == 0.0
        assert model.faces[1].vertex_1.z == 0.0
        assert model.faces[1].vertex_2.x == 0.0
        assert model.faces[1].vertex_2.y == 1.0
        assert model.faces[1].vertex_2.z == 0.0
        assert model.faces[1].vertex_3.x == 1.0
        assert model.faces[1].vertex_3.y == 1.0
        assert model.faces[1].vertex_3.z == 0.0

        assert model.faces[2].vertex_1.x == 0.0
        assert model.faces[2].vertex_1.y == 0.0
        assert model.faces[2].vertex_1.z == 0.0
        assert model.faces[2].vertex_2.x == 0.0
        assert model.faces[2].vertex_2.y == 1.0
        assert model.faces[2].vertex_2.z == 1.0
        assert model.faces[2].vertex_3.x == 0.0
        assert model.faces[2].vertex_3.y == 1.0
        assert model.faces[2].vertex_3.z == 0.0

        assert model.faces[3].vertex_1.x == 0.0
        assert model.faces[3].vertex_1.y == 0.0
        assert model.faces[3].vertex_1.z == 0.0
        assert model.faces[3].vertex_2.x == 0.0
        assert model.faces[3].vertex_2.y == 0.0
        assert model.faces[3].vertex_2.z == 1.0
        assert model.faces[3].vertex_3.x == 0.0
        assert model.faces[3].vertex_3.y == 1.0
        assert model.faces[3].vertex_3.z == 1.0

        assert model.faces[4].vertex_1.x == 0.0
        assert model.faces[4].vertex_1.y == 1.0
        assert model.faces[4].vertex_1.z == 0.0
        assert model.faces[4].vertex_2.x == 1.0
        assert model.faces[4].vertex_2.y == 1.0
        assert model.faces[4].vertex_2.z == 1.0
        assert model.faces[4].vertex_3.x == 1.0
        assert model.faces[4].vertex_3.y == 1.0
        assert model.faces[4].vertex_3.z == 0.0

        assert model.faces[5].vertex_1.x == 0.0
        assert model.faces[5].vertex_1.y == 1.0
        assert model.faces[5].vertex_1.z == 0.0
        assert model.faces[5].vertex_2.x == 0.0
        assert model.faces[5].vertex_2.y == 1.0
        assert model.faces[5].vertex_2.z == 1.0
        assert model.faces[5].vertex_3.x == 1.0
        assert model.faces[5].vertex_3.y == 1.0
        assert model.faces[5].vertex_3.z == 1.0

        assert model.faces[6].vertex_1.x == 1.0
        assert model.faces[6].vertex_1.y == 0.0
        assert model.faces[6].vertex_1.z == 0.0
        assert model.faces[6].vertex_2.x == 1.0
        assert model.faces[6].vertex_2.y == 1.0
        assert model.faces[6].vertex_2.z == 0.0
        assert model.faces[6].vertex_3.x == 1.0
        assert model.faces[6].vertex_3.y == 1.0
        assert model.faces[6].vertex_3.z == 1.0

        assert model.faces[7].vertex_1.x == 1.0
        assert model.faces[7].vertex_1.y == 0.0
        assert model.faces[7].vertex_1.z == 0.0
        assert model.faces[7].vertex_2.x == 1.0
        assert model.faces[7].vertex_2.y == 1.0
        assert model.faces[7].vertex_2.z == 1.0
        assert model.faces[7].vertex_3.x == 1.0
        assert model.faces[7].vertex_3.y == 0.0
        assert model.faces[7].vertex_3.z == 1.0

        assert model.faces[8].vertex_1.x == 0.0
        assert model.faces[8].vertex_1.y == 0.0
        assert model.faces[8].vertex_1.z == 0.0
        assert model.faces[8].vertex_2.x == 1.0
        assert model.faces[8].vertex_2.y == 0.0
        assert model.faces[8].vertex_2.z == 0.0
        assert model.faces[8].vertex_3.x == 1.0
        assert model.faces[8].vertex_3.y == 0.0
        assert model.faces[8].vertex_3.z == 1.0

        assert model.faces[9].vertex_1.x == 0.0
        assert model.faces[9].vertex_1.y == 0.0
        assert model.faces[9].vertex_1.z == 0.0
        assert model.faces[9].vertex_2.x == 1.0
        assert model.faces[9].vertex_2.y == 0.0
        assert model.faces[9].vertex_2.z == 1.0
        assert model.faces[9].vertex_3.x == 0.0
        assert model.faces[9].vertex_3.y == 0.0
        assert model.faces[9].vertex_3.z == 1.0

        assert model.faces[10].vertex_1.x == 0.0
        assert model.faces[10].vertex_1.y == 0.0
        assert model.faces[10].vertex_1.z == 1.0
        assert model.faces[10].vertex_2.x == 1.0
        assert model.faces[10].vertex_2.y == 0.0
        assert model.faces[10].vertex_2.z == 1.0
        assert model.faces[10].vertex_3.x == 1.0
        assert model.faces[10].vertex_3.y == 1.0
        assert model.faces[10].vertex_3.z == 1.0

        assert model.faces[11].vertex_1.x == 0.0
        assert model.faces[11].vertex_1.y == 0.0
        assert model.faces[11].vertex_1.z == 1.0
        assert model.faces[11].vertex_2.x == 1.0
        assert model.faces[11].vertex_2.y == 1.0
        assert model.faces[11].vertex_2.z == 1.0
        assert model.faces[11].vertex_3.x == 0.0
        assert model.faces[11].vertex_3.y == 1.0
        assert model.faces[11].vertex_3.z == 1.0