# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita o primeiro número ao usuário
# Usamos float() para permitir números decimais. Se você quiser apenas inteiros, use int().
numero1_str = input("Por favor, insira o primeiro número: ")

# Solicita o segundo número ao usuário
numero2_str = input("Por favor, insira o segundo número: ")

# Converte as entradas (que são strings) para números (float)
try:
    numero1 = float(numero1_str)
    numero2 = float(numero2_str)
except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
    exit() # Encerra o programa se a conversão falhar

# Realiza a operação de soma
resultado = numero1 + numero2

# Exibe o resultado
print(f"A soma de {numero1} e {numero2} é: {resultado}")
