# ⚙️ Simulador de Máquina de Turing

Este repositório contém um **simulador de Máquina de Turing (MT)** escrito em Python, desenvolvido para processar e verificar linguagens formais com base em um conjunto de regras definidas em um arquivo JSON.

---

## 📚 Linguagem Reconhecida

A Máquina de Turing configurada neste repositório foi projetada para reconhecer a linguagem:

$$
L = \{ a^n b^n \mid n \geq 0 \}
$$

Ou seja, todas as strings que contêm um número igual de símbolos **`a`** seguidos por um número igual de símbolos **`b`**.

### ✅ Exemplos Aceitos
- ε (string vazia)  
- `ab`  
- `aabb`  
- `aaabbb`  

### ❌ Exemplos Rejeitados
- `aab`  
- `abba`  
- `baa`  

---

## 🚀 Como Executar o Simulador

O simulador está configurado para ser executado diretamente no **VS Code**, sem a necessidade de passar argumentos no terminal.

### 🔧 Pré-requisitos
- Python 3 instalado em sua máquina.

---

## 📂 Estrutura de Arquivos

Certifique-se de que os seguintes arquivos estejam no mesmo diretório:

- `maquina_turing.py` → Código principal que contém o simulador da MT.  
- `specs.json` → Arquivo de especificações (regras de transição) para a linguagem \(a^n b^n\).  
- `problema.txt` → Arquivo que contém a palavra de entrada a ser testada na fita.  
- `saida_final.txt` → Arquivo de saída gerado pelo simulador com o estado final da fita.  

---

## ▶️ Executando o Teste

1. **Configure a Entrada:**  
   Abra o arquivo `problema.txt` e insira a palavra que deseja testar (ex: `aabb` ou `aab`). Salve o arquivo.  

2. **Execute o Script:**  
   Abra o arquivo `maquina_turing.py` no VS Code e clique em **Run File** (ícone ▶️ no canto superior direito).  

---

## 📌 Resultado

O resultado da execução será impresso no terminal do VS Code:

- `1` → A palavra foi **ACEITA** (a MT parou em um estado final).  
- `0` → A palavra foi **REJEITADA** (a MT parou em um estado não-final ou não encontrou transição).  

---

## 🏗️ Estrutura da Máquina de Turing \(a^n b^n\)

### Símbolos da fita:
- `a`, `b`, `X`, `Y`, `#` (início), `_` (branco).  

### Marcação:
- Os `a` são marcados como `X`  
- Os `b` são marcados como `Y`  

### Estados principais:
- **q0 (Inicial):** Procura o primeiro `a` para marcar.  
- **q1:** Varre para a direita após marcar um `a`, procurando o primeiro `b`.  
- **q2:** Varre para a esquerda após marcar um `b`, voltando para o início.  
- **q3:** Estado de verificação final (todos os `a` e `b` foram pareados).  
- **q4 (Final):** Estado de aceitação.  

---

✍️ Desenvolvido em Python para fins acadêmicos e de estudo em **Linguagens Formais e Autômatos**.
