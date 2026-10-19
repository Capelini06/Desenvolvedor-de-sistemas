# Desenvolvedor-de-sistemas

Repositório com as atividades em Python feitas durante o curso de Desenvolvedor de Sistemas. Cada aula tem a sua própria pasta dentro de [atividades/](atividades/).

## Conteúdo das aulas

### [Aula 01](atividades/Aula_01/) – Primeiros passos com `print`
Primeiros programas, que apenas exibem texto na tela: uma mensagem inicial, uma apresentação pessoal e algoritmos do dia a dia escritos passo a passo (como escovar os dentes ou o caminho de casa até o Senac).

### [Aula 02](atividades/Aula_02/) – Variáveis
Criação de variáveis de diferentes tipos (texto, inteiro, decimal e booleano) e exibição dos valores com `print`. Exemplos: dados de uma pessoa, um cadastro simples e informações de um produto.
- `variaveis.py`: exemplo da aula sobre variáveis.

### [Aula 03](atividades/Aula_03/) – Operadores
Operadores aritméticos (soma, subtração, multiplicação e divisão), cálculo de média de notas e uso de comparações para saber se o aluno foi aprovado.
- `contas.py`: exemplos de operações aritméticas.
- `concatenacao.py`: junção de textos com `+`.
- `operadoresLogicos.py`: uso de `and`, `or` e operadores de comparação.

### [Aula 04](atividades/Aula_04/) – Entrada de dados
Leitura de dados digitados pelo usuário com `input()` e conversão de tipos com `int()` e `float()`. Exercícios: cadastro, cálculo de IMC, área do triângulo, divisão e resto, potência e conversão de Celsius para Fahrenheit.
- `entradaDados.py`: exemplo da aula sobre `input()`.

### [Aula 05](atividades/Aula_05/) – Exercícios com entrada e cálculos
Programas que juntam entrada de dados e operações matemáticas para resolver problemas práticos: média de notas, total de uma compra, salário final com horas extras e descontos, salário com comissão, custo de combustível de uma viagem e média ponderada.

### [Aula 06](atividades/Aula_06/) – Estrutura condicional `if` / `else`
Tomada de decisões no código: maioridade, aprovação de aluno, desconto em compras, autorização de saque, limite de velocidade, liberação de entrada e pré-aprovação de empréstimo, combinando condições com `and` e `or`.
- `if.py`: exemplo da aula sobre `if` / `else`.

### [Aula 07](atividades/Aula_07/) – Condicionais encadeadas com `elif`
Testes com mais de duas possibilidades: classificação de notas, faixas de desconto, níveis de velocidade e classificação do IMC.
- `elif.py`: exemplo da aula sobre `elif`.

### [Aula 08](atividades/Aula_08/) – Estrutura `match` / `case`
Escolha entre várias opções com `match`: dias da semana, meses do ano, menu de caixa eletrônico, calculadora com as quatro operações e conversão de metros para outras unidades.
- `match.py`: exemplo da aula sobre `match` / `case`.

### [Aula 09](atividades/Aula_09/) – Laço de repetição `while`
Repetições controladas por um contador ou por uma condição: contagem crescente e decrescente, números pares, tabuada, soma acumulada, média de notas com parada pelo usuário (`break`), pedido de pastéis em loop e validação de senha.
- `while.py`: exemplo da aula sobre `while`.

### [Aula 10](atividades/Aula_10/) – Laço de repetição `for`
Uso do `for` com `range()` (início, fim e passo): contagem crescente e decrescente, números pares, tabuada de um número digitado, soma de 1 a 100 e chamada de presença dos alunos.
- `for.py`: exemplo da aula sobre `for`.

### [Aula 11](atividades/Aula_11/) – Vetores (listas)
Criação de listas, acesso por índice, uso de `len()` e alteração de elementos. Exercícios: lista de frutas, alunos, números, lista de compras digitada pelo usuário e inventário de um jogo.
- `vetores.py`: listas de diferentes tipos e percorrendo uma lista com `for`.
- `inserindoVetor.py`: inserção com `append()` e `insert()`.
- `removendoVetor.py`: remoção com `pop()` e `remove()`.

### [Aula 12](atividades/Aula_12/) – Percorrendo e pesquisando vetores
Uso do `for` com `range(len(lista))` para listar itens numerados, preencher uma lista com dados digitados, contar aprovados e reprovados e pesquisar um nome dentro da lista.
- `forVetore.py`: preenchendo e exibindo uma lista com `for`.
- `pesquisaVetor.py`: busca de um elemento e da sua posição na lista.

### [Aula 13](atividades/Aula_13/) – Matrizes
Listas de listas (linhas e colunas): acesso por `matriz[linha][coluna]`, alteração de posições (como um mapa de assentos), percorrendo a matriz com dois `for` aninhados, notas de alunos e soma/média dos elementos.
- `matriz.py`: exemplo da aula percorrendo e somando uma matriz.

## Projeto – Sistema de restaurantes (orientação a objetos)

A pasta [projeto/](projeto/) contém um pequeno sistema feito com classes, organizado em módulos dentro de [projeto/modelos/](projeto/modelos/):

- [restaurante.py](projeto/modelos/restaurante.py) – classe `Restaurante`, com nome, categoria, estado ativo/inativo, avaliações e média das notas. Mantém a lista de todos os restaurantes criados (`listar_restaurantes()`).
- [produto.py](projeto/modelos/produto.py) – classe `Produto`, com nome, preço, disponibilidade, avaliações e aplicação de desconto (`aplicar_desconto()`).
- [pedido.py](projeto/modelos/pedido.py) – classe `Pedido`, que liga um restaurante a uma lista de produtos e calcula o total.
- [avaliacao.py](projeto/modelos/avaliacao.py) – classe `Avaliacao`, com o cliente e a nota.

O arquivo [main.py](projeto/main.py) cria restaurantes, produtos e um pedido e mostra o resultado. Ele também demonstra conceitos como atributos de classe e de instância, `@property`, `@classmethod`, o método `__str__` e a diferença entre `vars()` e `dir()`.

## Como executar

Com o Python 3.10 ou mais recente instalado (necessário para o `match` da Aula 08), rode qualquer arquivo pelo terminal:

```bash
python atividades/Aula_01/atividade-01.py
```

Para o projeto, entre na pasta `projeto` antes de executar, para que os imports de `modelos` funcionem:

```bash
cd projeto
python main.py
```
