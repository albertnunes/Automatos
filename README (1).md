🤖 Simulador de Autômato Finito Determinístico (DFA)

Este projeto implementa um simulador de Autômato Finito Determinístico (DFA) que lê a definição de um autômato a partir de um arquivo, processa uma lista de palavras e determina se cada uma é aceita ou rejeitada conforme as transições e estados finais definidos.

🚀 Tecnologias Utilizadas

Python 🐍

Manipulação de arquivos (open, readlines)

Estruturas de dados (listas, tuplas)

Simulação de autômatos finitos

⚙️ Etapas Principais

Leitura dos arquivos de entrada

dfa.txt contém o estado inicial, os estados finais e as transições.

words.txt contém as palavras a serem testadas.

Processamento das transições

Cada transição é convertida de uma linha no formato origem|símbolo|destino para uma tupla (int, str, int).

Simulação do DFA

Para cada palavra, o programa percorre os estados conforme os símbolos.

Se a palavra terminar em um estado final, é marcada como aceita (1); caso contrário, rejeitada (0).

Geração dos resultados

Os resultados são gravados no arquivo results.txt, um por linha, seguindo a ordem das palavras.

📊 Saída do Sistema

1 → Palavra aceita pelo autômato

0 → Palavra rejeitada pelo autômato
