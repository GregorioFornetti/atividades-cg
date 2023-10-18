'''
Implementa o escritor de arquivos PPM, conforme descrito no tutorial: 
https://raytracing.github.io/books/RayTracingInOneWeekend.html?#outputanimage

O código está escrito originalmente em C++, mas foi adaptado para Python.

Para visualizar a imagem gerada, utilize o site:
https://www.cs.rhodes.edu/welshc/COMP141_F16/ppmReader.html
'''

from tqdm import tqdm

img_width = 256
img_height = 256

with open('img_tutorial.ppm', 'w') as img_file:

    # Cabeçalho do arquivo PPM
    img_file.write('P3\n')  # Formato ASCII
    img_file.write(f'{img_width} {img_height}\n')  # Largura e altura da imagem
    img_file.write('255\n')  # Valor máximo de cada cor

    # Corpo do arquivo PPM
    for i in tqdm(range(img_height)):
        for j in range(img_width):
            r = j / (img_width - 1)
            g = i / (img_height - 1)
            b = 0.0

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            img_file.write(f'{ir} {ig} {ib}\n')