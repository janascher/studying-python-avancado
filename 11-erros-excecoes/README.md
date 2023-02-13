## 📝 Exercícios

### Questão 01 

Faça um programa em **python** que faça a divisão de 1 por um valor passado por uma variável e realize o tratamento para as entradas abaixo:

```bash
    entrada = 0
    divisao = 1/entrada # vai dar error
```

Nesse caso tem que ser tratado o erro de divisão por zero, criar um tratamento de exceção para esse tipo de erro e imprimir uma mensagem amigável com o tipo de erro.

```bash
    entrada = ‘teste’
    divisao = 1/entrada # vai dar error
```

Nesse caso tem que ser tratado o erro de tipo, criar um tratamento exceção para esse tipo de erro e imprimir uma mensagem amigável com o tipo de erro.

E deixar o código para tratar erros genéricos diferentes dos mencionados acima.

Caso a entrada seja um valor que não provoque erro, imprimir o valor da divisão.

Por fim, independente de ter erro ou não imprimir ao final da execução do programa, dentro da estrutura de tratamento de exceções uma mensagem informando seu nome.