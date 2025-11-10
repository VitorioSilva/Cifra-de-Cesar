# 🔐 Cifra de César em Python

Implementação simples e interativa da **Cifra de César**, um dos algoritmos de criptografia mais antigos da história.  
O programa permite **criptografar** e **descriptografar** mensagens de texto, aplicando um deslocamento fixo sobre as letras do alfabeto.

---

## 📜 Sobre o Projeto

A **Cifra de César** é uma técnica de substituição onde cada letra de uma mensagem é deslocada um número fixo de posições no alfabeto.  
Por exemplo, com deslocamento igual a `3`, a letra **A** torna-se **D**, **B** torna-se **E**, e assim por diante.

Este programa:
- Criptografa e descriptografa mensagens.
- Mantém espaços e caracteres especiais inalterados.
- Funciona com letras maiúsculas e minúsculas.
- Inclui tratamento de erros e interrupções de teclado.
- Possui um modo de demonstração automática (`exemplo_uso()`).

---

## 🚀 Como Usar

### 🔧 Pré-requisitos
- Python 3 instalado em seu sistema.

### ▶️ Executar o Programa

1. Salve o código em um arquivo chamado `cifra_cesar.py`.
2. No terminal, execute:
   ```bash
   python3 cifra_cesar.py
   ```
3. Escolha uma das opções:
   ```
   === CIFRA DE CÉSAR ===
   1. Criptografar mensagem
   2. Descriptografar mensagem
   3. Sair
   ```

### 💡 Exemplo de Uso
#### Execução automática
Ao iniciar, o programa mostra um exemplo prático:
```
==================================================
EXEMPLO DE USO:
==================================================
Mensagem original: Bio Hacking
Deslocamento: 3
Mensagem criptografada: Elr Kdfnlqj
Mensagem descriptografada: Bio Hacking
```

#### Execução interativa
```
=== CIFRA DE CÉSAR ===
1. Criptografar mensagem
2. Descriptografar mensagem
3. Sair

Escolha uma opção (1-3): 1
Digite a mensagem: OpenAI GPT
Digite o número de deslocamentos: 5

Mensagem criptografada: TujsFN LKUY
```

---

## 🧠 Estrutura do Código

| Função | Descrição |
|--------|------------|
| `cifra_cesar(texto, deslocamento, operacao)` | Aplica a lógica de criptografia ou descriptografia. |
| `main()` | Interface interativa para o usuário. |
| `exemplo_uso()` | Mostra um exemplo prático de funcionamento. |

---

## 🧩 Lógica da Cifra

A criptografia é feita através da manipulação do código ASCII das letras:
```python
novo_char = chr((ord(char) - ascii_base + deslocamento) % 26 + ascii_base)
```
- `ord(char)` converte o caractere em número.
- `ascii_base` define se a letra é maiúscula (`'A'`) ou minúscula (`'a'`).
- `% 26` garante o retorno ao início do alfabeto se ultrapassar `Z`.

---

## ⚠️ Observações
- O deslocamento pode ser positivo ou negativo.
- Apenas letras do alfabeto são alteradas.
- Caracteres como números, espaços e pontuação permanecem inalterados.

---

## 🧑‍💻 Autor
**Vitório Santos**  
💬 Projeto educativo em Python — domínio de fundamentos de criptografia clássica.