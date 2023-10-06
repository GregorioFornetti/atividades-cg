
# Atividade 01 - I/O de imagens

Criar classes para Input e Output de imagens.

Descrição original da atividade:

1- Seguir o "tutorial" até a seção 2

2- Criar uma classe própria para salvar imagens, utilize bibliotecas como libpng, CImg e ImageMagick

3- Gere pelo menos três imagens. Exemplos: degradê, círculo, quadrado, etc...

4- Faça uma breve documentação: doxygen + readme


## Execução da atividade

Para concluir a atividade, os seguintes arquivos foram criados:

- `tutorial.py`: arquivo contendo o código adaptado do "tutorial".

- `ImageIO.py`: arquivo principal, contendo a implementação das classes solicitadas. Implementa a classe `ImageReader` para a leitura de imagens e `ImageWriter` para escrita de imagens.

- `notebook-testes.ipynb`: para fazer alguns testes básicos das classes implementadas, em um ambiente de fácil execução para teste (Jupyter Notebook).

- `test_ImageIO`: arquivo de testes automatizados. Testa as classes `ImageReader` e `ImageWriter`, verificando se é possível recuperar a matriz usada pelo objeto da classe `ImageWriter` para salvar a imagem, usando a classe `ImageReader` para ler essa imagem.

- `images/*`: imagens geradas pela classe `ImageWriter` no notebook `notebook-testes.ipynb`

- `doc/index.html`: documentação gerada para essa atividade, usando o `sphinx`