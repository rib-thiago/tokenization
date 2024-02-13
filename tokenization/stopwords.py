"""
Este script realiza três funções diferentes: etiquetagem POS, geração de lista de stopwords e geração de lista de tokens que não são stopwords.

Usage:
    python script.py <opcao> <caminho_para_arquivo> <caminho_para_output>

Arguments:
    opcao (str): A opção a ser executada. Pode ser 'tags', 'stopwords' ou 'non_stopwords'.
    caminho_para_arquivo (str): O caminho para o arquivo de texto a ser processado.
    caminho_para_output (str): O caminho para o arquivo de saída onde os resultados serão salvos.

Options:
    None

Exemplos de Uso:
    # Etiquetar POS de um arquivo de texto e salvar as tags em um arquivo de texto
    python script.py tags texto.txt tags.txt

    # Gerar lista de stopwords e salvar a contagem em um arquivo de texto
    python script.py stopwords texto.txt stopwords.txt

    # Gerar lista de tokens que não são stopwords e salvar a contagem em um arquivo de texto
    python script.py non_stopwords texto.txt non_stopwords.txt
"""

import argparse
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from collections import Counter

def generate_pos_tags(text):
    """
    Gera as etiquetas POS (Part-of-Speech) de um texto.

    Args:
        text (str): O texto a ser processado.

    Returns:
        list: Lista de etiquetas POS.
    """
    tokens = word_tokenize(text)
    tags = pos_tag(tokens)
    return tags

def list_stopwords(text):
    """
    Gera uma lista de stopwords contidas no texto.

    Args:
        text (str): O texto a ser processado.

    Returns:
        list: Lista de stopwords contidas no texto.
    """
    stopwords_set = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    stopwords_list = [token.lower() for token in tokens if token.lower() in stopwords_set]
    return stopwords_list

def list_non_stopwords(text):
    """
    Gera uma lista de tokens que não são stopwords.

    Args:
        text (str): O texto a ser processado.

    Returns:
        list: Lista de tokens que não são stopwords.
    """
    stopwords_set = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    non_stopwords_list = [token.lower() for token in tokens if token.lower() not in stopwords_set]
    return non_stopwords_list

def save_to_file(data, output_file):
    """
    Salva os dados em um arquivo de texto.

    Args:
        data (list): Os dados a serem salvos.
        output_file (str): O caminho para o arquivo de saída.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        for item in data:
            f.write(str(item) + "\n")

if __name__ == "__main__":
    # Configura o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Realiza três funções diferentes: etiquetagem POS, geração de lista de stopwords e geração de lista de tokens que não são stopwords.")
    parser.add_argument("opcao", choices=["tags", "stopwords", "non_stopwords"], help="A opção a ser executada (tags, stopwords, non_stopwords).")
    parser.add_argument("caminho_para_arquivo", help="O caminho para o arquivo de texto a ser processado.")
    parser.add_argument("caminho_para_output", help="O caminho para o arquivo de saída onde os resultados serão salvos.")

    # Analisa os argumentos da linha de comando
    args = parser.parse_args()

    # Lê o texto do arquivo
    with open(args.caminho_para_arquivo, 'r', encoding='utf-8') as file:
        text = file.read()

    # Executa a função selecionada
    if args.opcao == "tags":
        tags = generate_pos_tags(text)
        save_to_file(tags, args.caminho_para_output)
        print("Tags POS salvas em", args.caminho_para_output)
    elif args.opcao == "stopwords":
        stopwords_list = list_stopwords(text)
        count_stopwords = len(stopwords_list)
        save_to_file(stopwords_list, args.caminho_para_output)
        print(f"Lista de stopwords salva em {args.caminho_para_output} com {count_stopwords} palavras.")
    elif args.opcao == "non_stopwords":
        non_stopwords_list = list_non_stopwords(text)
        count_non_stopwords = len(non_stopwords_list)
        save_to_file(non_stopwords_list, args.caminho_para_output)
        print(f"Lista de tokens não stopwords salva em {args.caminho_para_output} com {count_non_stopwords} palavras.")
