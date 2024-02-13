"""
Este script extrai texto de uma imagem e realiza a tokenização do texto extraído.

Usage:
    python script.py <filename> [--language LANGUAGE]

Arguments:
    filename (str): O caminho para o arquivo de imagem a ser processado.

Options:
    --language, -l LANGUAGE: O idioma a ser usado para o OCR (default: eng).

Exemplos de Uso:
    # Extrair texto de uma imagem 'imagem.png' e salvar o texto extraído, as palavras tokenizadas e as sentenças tokenizadas
    python script.py imagem.png

    # Extrair texto de uma imagem 'imagem.png' em espanhol e salvar o texto extraído, as palavras tokenizadas e as sentenças tokenizadas
    python script.py imagem.png -l spa
"""

import cv2
import pytesseract
import argparse
import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def extract_text(filename, language='eng'):
    """
    Extrai texto de uma imagem e realiza a tokenização do texto extraído.

    Args:
        filename (str): O caminho para o arquivo de imagem a ser processado.
        language (str): O idioma a ser usado para o OCR (default: 'eng').

    Returns:
        None

    Raises:
        FileNotFoundError: Se o arquivo especificado não for encontrado.
        Exception: Se ocorrer um erro ao processar a imagem.

    """
    try:
        # Carrega a imagem
        img = cv2.imread(filename)

        # Extrai texto da imagem
        resultado = pytesseract.image_to_string(img, lang=language)

        # Salva o texto extraído em um arquivo de texto
        with open("texto_extraido.txt", "w", encoding="utf-8") as f:
            f.write(resultado)
        print("Texto extraído salvo em 'texto_extraido.txt'")

        # Tokenização do texto
        tokenized_words = word_tokenize(resultado)
        tokenized_sentence = sent_tokenize(resultado)

        # Salva o texto tokenizado em um arquivo de texto
        with open("tokenized_words.txt", "w", encoding="utf-8") as f:
            f.write(str(tokenized_words))
        print("Texto extraído salvo em 'tokenized_words.txt'")

        # Salva o texto tokenizado em um arquivo de texto
        with open("tokenized_sentence.txt", "w", encoding="utf-8") as f:
            f.write(str(tokenized_sentence))
        print("Texto extraído salvo em 'tokenized_sentence.txt'")

    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    # Configura o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Extract text from an image")
    parser.add_argument("filename", help="caminho para o arquivo de imagem")
    parser.add_argument("--language", "-l", default="eng", help="idioma para OCR (default: eng)")

    # Analisa os argumentos da linha de comando
    args = parser.parse_args()

    # Chama a função extract_text com os argumentos fornecidos
    extract_text(args.filename, args.language)
