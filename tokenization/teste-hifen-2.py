"""
Este script corrige palavras divididas por hífen e quebra de linha em um arquivo de texto.

Usage:
    python script.py <arquivo>

Arguments:
    arquivo (str): O caminho para o arquivo de texto a ser corrigido.

Options:
    None

Exemplo de Uso:
    # Corrigir palavras divididas em um arquivo de texto e imprimir o texto corrigido na tela
    python script.py arquivo.txt
"""

import argparse
import re

def corrigir_palavra(match):
    """
    Função de substituição para corrigir palavras divididas por hífen e quebra de linha.

    Args:
        match (re.Match): O objeto de correspondência de padrão.

    Returns:
        str: A palavra corrigida.
    """
    palavra_corrigida = match.group(1) + match.group(2)
    return palavra_corrigida

def main():
    """
    Função principal para corrigir palavras divididas por hífen e quebra de linha em um arquivo de texto.
    """
    # Definindo o parser para tratar argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Corrigir palavras divididas por hífen e quebra de linha em um arquivo de texto.")
    parser.add_argument("arquivo", help="Caminho para o arquivo de texto a ser corrigido.")
    args = parser.parse_args()

    # Ler o texto do arquivo
    with open(args.arquivo, 'r', encoding='utf-8') as file:
        texto = file.read()

    # Padrão regex para encontrar palavras divididas por hífen e quebra de linha
    padrao = r"(\w+)-\n(\w+)"

    # Substituir as ocorrências do padrão pelo seu equivalente corrigido
    texto_corrigido = re.sub(padrao, corrigir_palavra, texto)

    # Imprimir o texto corrigido
    print(texto_corrigido)

if __name__ == "__main__":
    main()
