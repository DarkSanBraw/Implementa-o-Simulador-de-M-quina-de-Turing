import json
import sys
import os

# --- FUNÇÕES DE SIMULAÇÃO (Copiadas de maquina_turing.py) ---

def ler_especificacoes(arquivo_json):
    """Lê o arquivo JSON com as especificações da Máquina de Turing"""
    try:
        # Resolve o caminho absoluto para o arquivo JSON
        caminho_abs = os.path.join(os.path.dirname(__file__), arquivo_json)
        with open(caminho_abs, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo de especificações '{arquivo_json}' não encontrado no diretório.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Erro: Arquivo '{arquivo_json}' não é um JSON válido.")
        sys.exit(1)

def ler_problema(arquivo_txt):
    """Lê o arquivo TXT com a entrada da fita"""
    try:
        # Resolve o caminho absoluto para o arquivo TXT
        caminho_abs = os.path.join(os.path.dirname(__file__), arquivo_txt)
        with open(caminho_abs, 'r', encoding='utf-8') as f:
            return f.read().splitlines()[0].strip()
    except FileNotFoundError:
        print(f"Erro: Arquivo de problema '{arquivo_txt}' não encontrado no diretório.")
        sys.exit(1)
    except IndexError:
        return ""

def simular_maquina_turing(specs, entrada):
    """
    Simula a execução de uma Máquina de Turing.
    (Lógica idêntica ao seu script original)
    """
    branco = specs.get('white', '_')
    fita = list('#' + entrada) 
    posicao = 1 
    estado_atual = specs['initial']
    estados_finais = set(specs['final'])
    
    transicoes = {}
    for t in specs['transitions']:
        chave = (t['from'], t['read'])
        transicoes[chave] = t
    
    max_passos = 1000000
    passos = 0
    
    while passos < max_passos:
        passos += 1
        
        if estado_atual in estados_finais:
            break
        
        if posicao < 0:
            fita.insert(0, branco)
            posicao = 0
        elif posicao >= len(fita):
            fita.append(branco)
        
        simbolo_atual = fita[posicao]
        
        chave = (estado_atual, simbolo_atual)
        if chave not in transicoes:
            break
        
        transicao = transicoes[chave]
        
        fita[posicao] = transicao['write']
        estado_atual = transicao['to']
        
        if transicao['dir'] == 'R':
            posicao += 1
        elif transicao['dir'] == 'L':
            posicao -= 1
    
    aceita = estado_atual in estados_finais
    fita_saida = ''.join(fita).strip(branco).lstrip('#')
    
    return fita_saida, aceita

def salvar_saida(arquivo_saida, fita):
    """Salva a fita de saída em um arquivo TXT"""
    try:
        # Resolve o caminho absoluto para o arquivo de saída
        caminho_abs = os.path.join(os.path.dirname(__file__), arquivo_saida)
        with open(caminho_abs, 'w', encoding='utf-8') as f:
            f.write(fita + '\n')
    except Exception as e:
        print(f"Erro ao salvar arquivo de saída: {e}")
        sys.exit(1)

# --- FUNÇÃO PRINCIPAL COM ARQUIVOS FIXOS ---

def main_runner():
    # Caminhos dos arquivos FIXOS na sua pasta:
    arquivo_specs = 'specs.json.json'
    arquivo_problema = 'problema.txt'
    arquivo_saida = 'saida_final.txt'
    
    print(f"--- Simulador MT em Execução ---")
    print(f"Lendo especificações: {arquivo_specs}")
    print(f"Lendo entrada: {arquivo_problema}")

    # Lê os arquivos de entrada
    specs = ler_especificacoes(arquivo_specs)
    problema = ler_problema(arquivo_problema)
    
    # Simula a Máquina de Turing
    fita_saida, aceita = simular_maquina_turing(specs, problema)
    
    # Salva a saída
    salvar_saida(arquivo_saida, fita_saida)
    
    # Imprime o resultado final (1 aceita, 0 rejeita)
    resultado = 1 if aceita else 0
    print(f"Entrada da Fita: '{problema}'")
    print(f"Fita Final (salva em {arquivo_saida}): '{fita_saida}'")
    print(f"RESULTADO: {resultado} ({'ACEITA' if aceita else 'REJEITA'})")
    print("---------------------------------")

if __name__ == "__main__":
    main_runner()
