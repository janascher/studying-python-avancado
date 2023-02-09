## 📝 Exercícios

### Questão 01 

Crie uma função chamada **teste_args** que tenha a estrutura para receber 2 argumentos fixos e outros variáveis. Ao final imprima todos os argumentos passados para essa função.  

Exemplo de passagem de argumentos que a função receberá sem precisar ter nenhuma mudança:  

- Chamada da função: `teste_args(Carro’, 100, 50, Pedra)`  
- Saída:

```bash
	arg1: ‘brasil’ 
	arg2: ‘País’  
	arg3: ‘PEDRA’
```
Outros exemplos de chamadas de função que deverão funcionar sem alterar a função:

```bash
	teste_args(‘brasil’, ‘País’, ‘Mundo’, Carro’, 100, 50, Pedra)  
	teste_args(‘brasil’, ‘País’, ‘Gol’, Carro’, 10)
```

### Questão 02 

Crie um programa em  **python** que receba via input  *n*  números e faça a  **multiplicação entre eles**  e imprima na tela.

Pode receber a quantidade ilimitada de números mas deve-se usar o  **args**  em uma função onde vai receber esses valores e irá realizar a multiplicação.

Exemplo:

- Se rodar o programa e receber : 5, 4, 5 o resultado será 100.
- Se rodar o programa e receber : 10, 2, 4, 3 o resultado será 240.

### Questão 03

Crie uma função chamada que tenha a estrutura para receber 2 argumentos fixos e N argumentos nomeados. No final imprima todos os argumentos passados para essa função.

Exemplo de passagem de argumentos que a função receberá sem precisar ter nenhuma mudança:

- Chamada da função: `teste_Kargs(Carro’, 100, nome=’jose’, chave=’teste’)`

- Saída:

```bash
	arg1=carro
	arg2=100
	nome=jose
	chave=teste
```
Outros exemplos de chamadas de função que deverão funcionar sem alterar a função:

- Chamada da função:  `teste_Kargs(Carro’, 100, nome=’jose’, chave=’teste’,outrachave=’brasil’, oo=’python’)`

- Saída:

```bash
	arg1=carro
	arg2=100
	nome=jose
	chave=teste
	outrachave = brasil
	oo = python
```