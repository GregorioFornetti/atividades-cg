
# Atividade 03 - I/O de malhas

## Documentação online

É possível acessar a documentação gerada no [Github Pages do projeto](https://gregoriofornetti.github.io/atividades-cg/Atividade03/docs/)

## Descrição original da atividade

Criar classes para representar e ler objetos 3D.

Descrição original da atividade:

1- Criar um repositório individual no github e enviar o endereço como comentário da atividade

2- Observar o formato obj, utilize algum repositório com modelos abertos, por exemplo: https://free3d.com/

3- Criar uma classe própria para ler modelos obj

4- Faça uma breve documentação e testes unitários

## Execução da atividade

Para concluir a atividade, os seguintes arquivos foram criados:

- `src/Model.py`: classe principal para leitura e representação de um modelo 3D. Responsável por ler um arquivo `.obj` e representa-lo em um objeto Python com diversos atributos e métodos para acessar informações relevantes ao modelo.

- `src/Triangle.py`: classe que armazenará as faces do modelo, no caso, apenas triângulos. Atualmente, armazena apenas os vértices das faces, ignorando a normal e as texturas.

- `src/TriangleFaceIndexes.py`: classe para armazenar os índices de vértices, texturas e normais relacionados a uma face.

- `tests`: nesta pasta, estão todos os arquivos de testes automatizados relacionados à representação e leitura de arquivos `.obj`.

- `objs`: nesta pasta, estão os arquivos `.obj` utilizados nos testes automatizados.

- `docs`: todos arquivos relacionados à documentação. A documentação pode ser visualizada [clicando aqui](https://gregoriofornetti.github.io/atividades-cg/Atividade03/docs/).
