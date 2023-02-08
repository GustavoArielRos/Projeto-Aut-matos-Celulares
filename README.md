# Projeto-Automatos-Celulares

![image](https://user-images.githubusercontent.com/101509337/217432338-debe5ce0-5c8a-49ea-acd6-90779cf70798.png)


##
Projeto de matemática discreta sobre autômatos celulares que foi realizado em dupla.

O Jogo da Vida (The Game of Life) é um algoritmo de simulação de um sistema dinâmico criado
pelo matemático britânico John Horton Conway em 1970. O algoritmo não possui entradas, i.e., só
depende do seu estado inicial. 

Resumidamente, as regras do jogo são:
1. Uma célula viva com menos do que 2 células vizinhas vivas, deve morrer na próxima geração
devido à superpopulação;
2. Uma célula viva com 2 ou 3 células vizinhas vivas permanece viva na próxima geração;
3. Uma célula viva com mais de 3 vizinhos morre na próxima geração devido à superpopulação;
4. Uma célula morta com exatamente 3 células vizinhas vivas se torna viva na próxima geração
devido à reprodução.

As regras descritas acima correspondem ao Jogo da Vida padrão. Tais regras são usualmente
resumidas através dos símbolos B3/S23 (Born 3, Stays alive 2 and 3). Várias outras regras já foram
testadas, como por exemplo, B6/S16, B36/S23, B3/S236, B3/S2367, etc. Em particular, a regra
B36/S23 (Born 3 and 6, Stays alive 2 and 3) é conhecida como High Life.

Dependendo da regra utilizada e da inicialização padrões de evolução surpreendentes podem ser
observados. Estes padrões possuem categorias como, por exemplo:
• Still lifes: padrões estáticos;
• Oscillators: padrões que se repetem indefinidamente;
• Spaceships: padrões que se assemelham a naves espaciais;
• Guns: padrões estacionários que emitem naves espaciais;
• Methuselah: padrão que demora muito tempo para estabilizar;

No projeto criado só há disponível 2 regras(regras B3/S23 e B3/S236.) e as células vivas ja são pré definidas pelo programa.
Também existe há opção de considerar ou não a borda(se as células atravessam ou não a tela).
