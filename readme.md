# Atividades de computação gráfica

Repositório contendo todas as atividades/trabalhos feitos na disciplina de computação gráfica (2023/2) , ministrada pelo professor Mario Liziér.

Aluno: Gregório Fornetti Azevedo

RA: 792181

## Detalhes sobre a implementação

A linguagem escolhida para a implementação geral do projeto foi [Python](https://www.python.org/)

Todas as atividades feitas estão nos repositórios `AtividadeXX`, sendo XX o número da atividade. Por exemplo, a implementação da atividade 1 está disponível na pasta `Atividade01`.

### Principais bibliotecas utilizadas no projeto

- [NumPy](https://numpy.org/): fornece estruturas de dados (arrays) e operações sobre elas que serão úteis para manipular e gerar as imagens.
- [Pillow](https://pypi.org/project/Pillow/): para salvar e ler imagens em diversos formatos.
- [Sphinx](https://www.sphinx-doc.org/pt_BR/master/): gerador de documentação a partir dos comentários de documentação incluídos no próprio código.
- [tqdm](https://tqdm.github.io/): para indicar progresso das operações/funções mais demoradas.
- [pytest](https://docs.pytest.org/en/7.4.x/): para criação dos testes automatizados.

### Instalação

Para conseguir executar o projeto, é necessário ter instalado o Python e todas as bibliotecas citadas. Para instalar mais facilmente as bibliotecas necessárias, foi criado o arquivo `requirements.txt`, e utilizando o pip (sistema de gerenciamento de pacotes do Python), é possível instalar todas as bibliotecas usando o comando `pip install -r requirements.txt`

## Testes automatizados

Para executar os testes automatizados, execute o comando: `pytest`

## Sobre geração de documentação usando Sphinx

Para usar o gerador de documentação Sphinx, foi seguido o [tutorial do canal Learn Programming with Joel](https://www.youtube.com/watch?v=BWIrhgCAae0)

Comandos necessários para gerar a página de documentação:

1- Para gerar alguns arquivos necessários para a geração da documentação, execute o comando:

```
sphinx-apidoc -o docs .
```

2- Para de fato gerar a documentação, execute o comando:

```
docs/create.bat html
```

A documentação gerada será salva no caminho `docs/_build/html`, podendo ser vizualizada no arquivo `index.html`

3- Em alguns casos, a documentação pode parecer desatualizada. Isso pode acontecer quando os arquivos gerados na etapa 1 já tinham sido criados antes,
e não foram atualizados nessa atualização. Para atualiza-los, é preciso exclui-los e depois criar novamente com o comando da etapa 1. No geral,
para excluir os arquivos que precisam ser atualizados, execute os comandos:

```
rm docs/modules.rst
rm docs/Atividade<NUM_ATIVIDADE>.rst
```
