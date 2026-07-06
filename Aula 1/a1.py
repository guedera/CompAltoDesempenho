import time

chamadas = 0

def fibonacci(n, nivel=0):
  global chamadas
  chamadas += 1
  if n < 2:
    return n
  return fibonacci(n - 1, nivel + 1) + fibonacci(n - 2, nivel + 1)

inicio = time.perf_counter()

print("Calculando, tenha paciência...")

resultado = fibonacci(42)

fim = time.perf_counter()

print(f"\nResultado final: {resultado}")

print(f"Chamadas realizadas: {chamadas}")

print(f"Tempo de execução: {fim - inicio:.6f} segundos")