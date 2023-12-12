# Atividade 5 - Materiais difusos

## Descrição original da atividade

1- Siga o tutorial, especialmente as seções 6, 7, 8 e 9.

2- Implemente o material difuso, usando a normal do modelo (utilize um arquivo com informação de normal)

3- Visualize uma cena (com pelo menos três objetos) e de dois pontos de vista diferente.

4- Documente adequadamente

## Execução da atividade

OBS: Muitas das tarefas pedidas no exercício dependem de outras implementações (das outras atividades). Muito do código dessa atividade está distribuido em mudanças das outras atividades, mas os resultados dessas mudanças podem ser todos consultados aqui, nos notebooks.

**Sobre a tarefa 1:**

O tutorial inteiro foi seguido no repositório principal do projeto em `tutorial/tutorial.ipynb`.

Todos os códigos implementados nele (material difuso e camera com configurações de posição e fov) foram passados como código das outras atividades. Por exemplo, muitas modificações na câmera foram feitas, e esta já foi definida na Atividade04, então, para não ter várias classes câmera, modifiquei a mesma classe da Atividade04 (o mesmo vale para outras classes, como HitRecord, Vec3, etc).

**Sobre a tarefa 2:**

A classe Model e Triangle foram modificadas para carregar as normais. O triângulo agora utiliza coordenadas baricêntricas para gerar uma normal resultante final, caso os vértices do mesmo possuam normais (que podem ser fornecidas pelo modelo .obj). Agora a classe Model carrega as normais do modelo e cria os triângulos do modelo utilizando essas normais, caso elas existam.

**Sobre a tarefa 3:**

Em `src/notebooks/final_render.ipynb`, a renderização de uma cena com no mínimo 3 objetos foi feita, utilizando dois ângulos de câmera diferentes. O resultado final da execução desse notebook pode ser consultado em: `imgs/final-first-angle.png` e `imgs/final-second-angle.png`.

**Sobre a tarefa 4:**

Novos métodos e funcionalidades que foram adicionados também foram documentados. Este documente `readme.md` também tem essa mesma finalidade.