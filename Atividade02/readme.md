
# Atividade 02 - Vetores e matrizes

## Documentação online

É possível acessar a documentação gerada no [Github Pages do projeto](https://gregoriofornetti.github.io/atividades-cg/Atividade02/doc/)

## Descrição original da atividade

Criar classes para representar vetores e matrizes

Descrição original da atividade:

1- Seguir o "tutorial" até a seção 3

2- Criar uma classe própria para manipular vetores e matrizes, expanda para vec2, vec4, mat2, mat3 e mat4

3- Faça testes unitários, escolha uma biblioteca que facilite

4- Faça uma breve documentação

## Execução da atividade

Para concluir a atividade, os seguintes arquivos foram criados:

- `interactive`: nesta pasta estão todas as implementações interativas (usando loops e não usando procedimentos internos da biblioteca numpy) de vetores e matrizes. No arquivo `Mat.py` está a classe base para implementação das classes `Mat2.py` (matriz 2x2), `Mat3.py` (matrix 3x3) e `Mat4.py` (matriz 4x4). No arquivo `Vec.py` está a classe base para implementação das classes `Vec2.py`, `Vec3.py` e `Vec4.py`.

- `interactive/tests`: nesta pasta, estão todos os testes automatizados relacionados às classes de vetores e matrizes citadas na pasta `interactive`.

- `vectorized`: nesta pasta estão todas as implementações vetorizadas (evitando uso de loops e usando procedimentos internos da biblioteca numpy) de vetores e matrizes.

- `vectorized/tests`: nesta pasta, estão todos os testes automatizados relacionados às classes de vetores e matrizes citadas na pasta `vectorized`.

- `doc/index.html`: documentação gerada para essa atividade, usando o `sphinx`