# product-registration-automation
Automação em Python que lê um arquivo CSV e cadastra produtos automaticamente em um sistema.
Automação de Cadastro de Produtos com Python

Este projeto é uma automação de tarefas desenvolvida em Python para realizar o cadastro automático de produtos em um sistema web a partir de uma base de dados em arquivo CSV.

O script acessa o sistema da empresa, realiza o login e preenche automaticamente os campos do formulário para cadastrar os produtos, utilizando automação de teclado e mouse.

O objetivo é demonstrar como a programação pode ser utilizada para automatizar tarefas repetitivas e operacionais, aumentando a produtividade e reduzindo erros manuais.

Contexto do Projeto
Este projeto foi desenvolvido durante uma aula prática de automação com Python.
Durante o desenvolvimento, mantive no código as anotações e comentários que fiz ao longo da aula, com o objetivo de registrar meu processo de ensino-aprendizagem.
Optei por manter essas anotações visíveis neste repositório para que recrutadores e pessoas interessadas possam acompanhar:
Como organizei o raciocínio do projeto
Como fui estruturando o passo a passo da automação
Meu processo de aprendizado ao estudar automação com Python

O que a automação faz:
A automação executa as seguintes etapas
Abre o navegador
Acessa o sistema da empresa
Realiza login automaticamente
Lê uma base de produtos em arquivo CSV
Preenche os campos do sistema automaticamente
Cadastra os produtos um a um
Repete o processo até finalizar toda a base de dados

Tecnologias utilizadas:
Python
PyAutoGUI (automação de teclado e mouse)
Pandas (leitura e manipulação de dados)
CSV (base de dados)

Estrutura do Projeto
📂 automacao-cadastro-produtos
 ├── automacao.py
 ├── produtos.csv
 └── README.md

Exemplo de funcionamento
O script lê os dados da base de produtos:
codigo | marca | tipo | categoria | preco_unitario | custo | obs
E preenche automaticamente os campos do sistema web para realizar o cadastro.

Objetivo do projeto
Este projeto foi desenvolvido com o objetivo de praticar:
Automação de tarefas com Python
Manipulação de dados com Pandas
Integração entre dados e sistemas
Criação de soluções para otimizar processos operacionais
Observação
Este projeto foi desenvolvido para fins educacionais, utilizando um ambiente de simulação disponibilizado para treinamento.

## Aprendizados

Durante o desenvolvimento deste projeto pratiquei:

- Automação de tarefas com Python
- Controle de teclado e mouse com PyAutoGUI
- Leitura e manipulação de dados com Pandas
- Integração entre dados estruturados (CSV) e sistemas web
- Estruturação de scripts para automatizar processos repetitivos

## Demonstração da automação
![Automação funcionando](GIFautomacao.gif)

## Problema que o projeto resolve

Em muitos sistemas de gestão, o cadastro de produtos é feito manualmente, o que pode ser demorado e sujeito a erros.

Este projeto demonstra como a automação com Python pode ser utilizada para:

- Reduzir tarefas repetitivas
- Aumentar a velocidade de cadastro de produtos
- Diminuir erros humanos
- Integrar dados estruturados (CSV) com sistemas web
