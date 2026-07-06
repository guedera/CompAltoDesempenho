# Aula 1 — Introdução a Computação de Alto Desempenho (HPC)

## 1. O que é HPC?

HPC (*High Performance Computing*) trata de problemas que um computador
comum não consegue resolver em tempo ou capacidade viáveis. Esses
problemas se encaixam em três categorias:

| Categoria | Característica |
|---|---|
| **Grandes** | Grande volume de dados — não cabe na memória/armazenamento de um computador comum. |
| **Intensivos** | Cálculos complexos e demorados, exigindo horas (ou mais) de processamento. |
| **Combo** | As duas características acima: muitos dados **e** processamento pesado. |

---

## 2. Hardware x Software

Pilha de camadas entre o hardware físico e o usuário final:

```
Hardware → Sistema Operacional (SO) → Aplicação/Software → Usuário
```

- **Hardware** — os componentes físicos (CPU, memória, disco, etc.).
- **Sistema Operacional** — gerencia os recursos de hardware e expõe uma interface para os programas.
- **Aplicação/Software** — os programas que resolvem problemas específicos.
- **Usuário** — quem interage com a aplicação.

---

## 3. Linguagens Compiladas x Interpretadas

**Linguagem compilada**

```
Linguagem → Código de Máquina → Pronto para Executar
```

O código-fonte é traduzido para código de máquina *antes* da execução
(pelo compilador). O resultado tende a rodar mais rápido, mas precisa
ser recompilado para cada arquitetura/SO diferente.

**Linguagem interpretada**

```
Linguagem → Pronto para Executar → Máquina Virtual → Código de Máquina
```

Não há uma etapa de compilação separada e visível ao usuário: o código
já é "pronto para executar". Quem converte para código de máquina, em
tempo real, é a Máquina Virtual/interpretador. Isso torna a linguagem
mais portável, porém geralmente mais lenta que uma linguagem compilada.

---

## 4. Falando de Hardware: o que é uma ULA?

**ULA (Unidade Lógica e Aritmética)** é o componente do processador
responsável por executar:

- **Operações aritméticas** — soma, subtração, multiplicação, etc.
- **Operações lógicas** — AND, OR, NOT, comparações, etc.

Ela recebe os dados (operandos) e a operação a ser feita, processa e
devolve o resultado — é basicamente o "calculador" central da CPU.

---

## 5. Analisando Fibonacci

> Nota: seção estava em branco (anotada no intervalo). Completei com o
> exemplo clássico de análise de complexidade — conferir/ajustar com o
> que for de fato apresentado depois do intervalo.

Fibonacci é um exemplo clássico para mostrar por que a forma como se
escreve um algoritmo impacta diretamente o desempenho — o tema central
de HPC.

**Versão recursiva (ingênua)**

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

- Recalcula os mesmos valores várias vezes (ex.: `fib(5)` chama `fib(3)` duas vezes).
- Complexidade de tempo: **O(2ⁿ)** — cresce exponencialmente.
- Para `n` grande, fica inviável mesmo em computadores rápidos.

**Versão iterativa**

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

- Guarda apenas os dois últimos valores calculados.
- Complexidade de tempo: **O(n)** — cresce linearmente.

**Por que isso importa para HPC?**

O mesmo problema pode ter soluções com custo computacional radicalmente
diferente. Antes de jogar mais hardware (paralelismo, clusters, GPUs)
em um problema, vale a pena garantir que o algoritmo em si já é
eficiente.
