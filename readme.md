# Atividades de computação gráfica

Repositório contendo todas as atividades/trabalhos feitos na disciplina de computação gráfica (2023/2) , ministrada pelo professor

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
