# Atividade 06 - Metal e Vidro

## Descrição original da atividade

1- Siga o tutorial, especialmente as seções 10 e 11

2- Implemente o materiais com reflexão e refração

3- Visualize uma cena com um objeto metálico e outro de vidro.

4- Documente adequadamente

## Execução da atividade

**Sobre a tarefa 1:**

O tutorial inteiro foi seguido no repositório principal do projeto em `tutorial/tutorial.ipynb`.

**Sobre a tarefa 2:**

Todos os materiais estão implementados nessa atividade: difuso (`src/Lambertian.py`), metal (`src/Metal.py`) e vidro (`src/Dielectric.py`). A câmera foi modificada na Atividade04 para utilizar os materias. As classes de Esfera e Triângulo da Atividade04 também foram modificadas para adicionar o material do objeto em questão. A classe HitRecord da Atividade04 também foi modificado para informar o material do objeto que ocorreu a colisão

**Sobre a tarefa 3:**

Em `src/notebooks/final_render.ipynb`, a renderização de uma cena com objetos metálicos e outra com vidros foi feita. O resultado da renderização dos metais está disponível em `imgs/final-metals.png` e a dos vidros em `imgs/final-glasses.png`.

**Sobre a tarefa 4:**

Novos métodos e funcionalidades que foram adicionados também foram documentados. Este documente `readme.md` também tem essa mesma finalidade.