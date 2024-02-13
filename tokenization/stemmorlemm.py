"""
Este script permite realizar stemming e lematização em palavras fornecidas como entrada.

O stemming é o processo de reduzir palavras ao seu radical ou raiz, removendo afixos derivacionais.
A lematização é o processo de determinar a forma básica de uma palavra, considerando sua forma flexionada e a classe gramatical.

Usage:
    python script.py <palavra> <opcao>

Arguments:
    palavra (str): A palavra a ser processada.
    opcao (str): A opção de processamento a ser realizada. Pode ser 'stem' para stemming, 'lemmatize' para lematização ou 'ambos' para executar ambos os processos.

Options:
    None

Exemplos de Uso:
    # Executar stemming na palavra 'running'
    python script.py running stem

    # Executar lematização na palavra 'running'
    python script.py running lemmatize

    # Executar stemming e lematização na palavra 'running'
    python script.py running ambos
"""

import argparse
from nltk.stem import SnowballStemmer as sbs
from nltk.stem import WordNetLemmatizer

def stem_word(word):
    """
    Realiza stemming em uma palavra.

    Args:
        word (str): A palavra a ser stemizada.

    Returns:
        str: O radical ou raiz da palavra.

    """
    stemmer = sbs('english')
    return stemmer.stem(word)

def lemmatize_word(word):
    """
    Realiza lematização em uma palavra.

    Args:
        word (str): A palavra a ser lematizada.

    Returns:
        str: A forma básica da palavra.

    """
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word, pos='v')

def main():
    """
    Função principal que analisa os argumentos da linha de comando e executa a operação selecionada.
    
    """
    parser = argparse.ArgumentParser(description="Script para stemizar e lematizar palavras.")
    parser.add_argument("palavra", help="Palavra a ser processada.")
    parser.add_argument("opcao", choices=["stem", "lemmatize", "ambos"], help="Opção de processamento (stem, lemmatize, ambos).")

    args = parser.parse_args()

    if args.opcao == "stem":
        result = stem_word(args.palavra)
        print("Stem da palavra '{}': {}".format(args.palavra, result))
    elif args.opcao == "lemmatize":
        result = lemmatize_word(args.palavra)
        print("Lematização da palavra '{}': {}".format(args.palavra, result))
    elif args.opcao == "ambos":
        stem_result = stem_word(args.palavra)
        lemma_result = lemmatize_word(args.palavra)
        print("Stem da palavra '{}': {}".format(args.palavra, stem_result))
        print("Lematização da palavra '{}': {}".format(args.palavra, lemma_result))

if __name__ == "__main__":
    main()
