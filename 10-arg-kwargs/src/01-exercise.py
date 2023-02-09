def teste_args(arg1="brasil", arg2="País", *arg3):
    print(f"Valores recebidos de arg3: {arg3}")
    print(arg1)
    print(arg2)
    for i in arg3:
        print(f"{i}")


teste_args("brasil", "País", "PEDRA")
#teste_args("brasil", "País", "Mundo", "Carro", 100, 50, "Pedra")
#teste_args("brasil", "País", "Gol", "Carro", 10)