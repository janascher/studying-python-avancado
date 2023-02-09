def teste_kargs(arg1="Carro", arg2=100, **arg3):
    print(f"Valores recebidos de arg3: {arg3}")
    print(arg1)
    print(arg2)
    for i in arg3:
        print(f"{i}")


#teste_kargs("Carro", 100, nome="jose", chave="teste")
teste_kargs("Carro", 100, nome="jose", chave="teste",
            outrachave="brasil", oo="python")
