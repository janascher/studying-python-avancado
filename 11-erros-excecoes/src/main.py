enter = 0

try:
    division = 1/enter
except ZeroDivisionError:
    # Trata erro específico
    print("Não possível dividir por zero.")
except TypeError:
    # Trata erro específico
    print("Não possível dividir com textos.")
except Exception as error:
    # Trata erro genérico
    print(f"\nOcorreu um erro inesperado: {error}")
else:
    print(f"O resultado é {division}.")
finally:
    print("Janaína")