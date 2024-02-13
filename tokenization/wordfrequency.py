"""
Este script lê um arquivo de texto e extrai as 20 palavras mais frequentes juntamente com suas frequências.

Usage:
    python script.py <arquivo>

Arguments:
    arquivo (str): O caminho para o arquivo de texto a ser processado.

Options:
    None

Exemplos de Uso:
    # Extrair as 20 palavras mais frequentes de um arquivo de texto 'texto.txt'
    python script.py texto.txt
"""

import argparse
from nltk import FreqDist
from nltk.tokenize import word_tokenize

def extract_most_common_words(filename):
    """
    Lê um arquivo de texto, extrai as 20 palavras mais comuns e suas frequências.

    Args:
        filename (str): O caminho para o arquivo de texto a ser processado.

    Returns:
        None

    Raises:
        FileNotFoundError: Se o arquivo especificado não for encontrado.
    """
    try:
        # Lê o conteúdo do arquivo
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # Tokeniza o texto
        tokens = word_tokenize(text)

        # Calcula a frequência das palavras
        freqs = FreqDist(tokens)

        # Obtém as 20 palavras mais frequentes
        most_common_words = freqs.most_common(20)

        # Exibe as 20 palavras mais frequentes e suas frequências
        print("As 20 palavras mais comuns:")
        for word, freq in most_common_words:
            print(word, freq)

    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")

if __name__ == "__main__":
    # Configura o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Extract the 20 most common words from a text file")
    parser.add_argument("filename", help="O caminho para o arquivo de texto")

    # Analisa os argumentos da linha de comando
    args = parser.parse_args()

    # Chama a função para extrair as palavras mais comuns
    extract_most_common_words(args.filename)

