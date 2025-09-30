⚙️ Simulador de Máquina de Turing
Este repositório contém um simulador de Máquina de Turing (MT) escrito em Python, desenvolvido para processar e verificar linguagens formais com base em um conjunto de regras (especificações) definidas em um arquivo JSON.

Linguagem Reconhecida
A Máquina de Turing configurada neste repositório foi projetada para reconhecer a linguagem L={a 
n
 b 
n
 ∣n≥0}.

Esta linguagem é composta por todas as strings que contêm um número igual de símbolos 'a' seguido por um número igual de símbolos 'b'.

Exemplos Aceitos:

ϵ (string vazia)

ab

aabb

aaabbb

Exemplos Rejeitados:

aab

abba

baa

🚀 Como Executar o Simulador
O simulador é configurado para ser executado diretamente no VS Code sem a necessidade de passar argumentos no terminal.

Pré-requisitos
Você precisa ter o Python 3 instalado em sua máquina.

Estrutura de Arquivos
Certifique-se de que os seguintes arquivos estejam no mesmo diretório:

maquina_turing.py: O código principal que contém o simulador da MT.

specs.json.json: O arquivo de especificações (regras de transição) para a linguagem a 
n
 b 
n
 .

problema.txt: O arquivo que contém a palavra de entrada a ser testada na fita.

saida_final.txt: Arquivo de saída gerado pelo simulador com o estado final da fita.

Executando o Teste
Configure a Entrada: Abra o arquivo problema.txt e insira a palavra que deseja testar (ex: aabb ou aab). Salve o arquivo.

Execute o Script: Abra o arquivo maquina_turing.py no VS Code.

Clique no botão "Run File" (Geralmente o ícone de Play) no canto superior direito do editor.

Resultado
O resultado da execução será impresso no terminal do VS Code:

1: A palavra foi ACEITA (a MT parou em um estado final).

0: A palavra foi REJEITADA (a MT parou em um estado não-final ou não encontrou transição).

Estrutura da Máquina de Turing (a 
n
 b 
n
 )
A MT utiliza o seguinte esquema de estados e símbolos:

Símbolos de Fita: a, b, X, Y, # (início), _ (branco).

Marcação: Os 'a's são marcados como X e os 'b's são marcados como Y.

Estados Principais:

q0 (Inicial): Procura o primeiro 'a' para marcar.

q1: Varre para a direita após marcar um 'a', procurando o primeiro 'b'.

q2: Varre para a esquerda após marcar um 'b', voltando para o início.

q3: Estado de verificação final (todos os 'a's e 'b's foram pareados).

q4 (Final): Estado de aceitação.
