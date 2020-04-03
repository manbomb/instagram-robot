# Insta Robot

## Justificativa
Aumentar o engajamento (curtidas e seguidores) em páginas de maneira automática, sem ser necessário esforço manual por parte do administrador.

## Alerta !
O uso deste tipo de script de maneira constante e exagerada pode levar ao bloqueio da página ou perfil por parte do Instagram, temporário ou permanente.

## Pidao
É um robô que dispara comentários listados no arquivo 'comment_pidao.py' de maneira aleatória em posts das tags listadas no arquivo 'tags.txt'.

## Inteligente
Diferente do Pidao, o Inteligente é um robô que analisa a foto do post e faz um comentário de acordo com o conteúdo que encontra nela, para isso utiliza detecção de objetos com a tecnologia YOLO (You Only Look Once) uma lista de comentários (em 'comment.txt') preenchidos de acordo com o contexto.

## Como funciona ?
Ambos utilizam a biblioteca Selenium do Python e o ChromeDriver para acessar e logar no Instagram, porém, devido o fato do campo de comentários do Instagram ser 'não-clicável', fez se necessário utilizar a biblioteca PyAutoGUI para digitar 'manualmente' os comentários. Para a detecção de objetos no Inteligente, o método YOLO foi utilizado, pois, apresenta um melhor desempenho que outras tecnologias (tanto em velocidade quanto precisão) como a Haar Cascade, além de o site https://www.pyimagesearch.com/ já disponibilizar um modelo treinado para 80 label's. O PHP foi utilizado devido a afinidade do desenvolvedor com a linguagem para este tipo de aplicação (sequestro de objetos através de file_get_contents) e deve ser executado em um localhost de preferência.

## Dificuldades e desvantagens do Inteligente
Por enquanto, o robô Inteligente ainda não possui um desempenho satisfatório, pois, gera comentários rasos e não analisa a situação como um todo, apenas aquilo que está com a 'maior presença' nas imagens. 

## Futura implementação
Uma futura implementação poderia ser utilizar unicamente deeplearning para analisar um vetor criado a partir do resultado do YOLO, utilizando como objetivo da rede neural, criar um comentário o mais próximo possível dos que já existem no post, supostamente feitos por humanos.
