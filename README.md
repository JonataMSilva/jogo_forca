# Jogo da Forca em Python

Este é um jogo simples de "Forca" implementado em Python. O jogo escolhe aleatoriamente uma palavra secreta de uma lista de frutas e permite ao jogador tentar adivinhar as letras da palavra. O jogador tem um número limitado de tentativas antes de perder o jogo.

## Como Jogar

1. O jogo escolhe aleatoriamente uma palavra secreta da lista de frutas.
2. Você tem 6 tentativas para adivinhar a palavra secreta. Cada tentativa envolve adivinhar uma letra da palavra.
3. O jogo exibirá a palavra atual com as letras adivinhadas preenchidas e as letras não adivinhadas como "_".
4. O jogo também mostrará o número de tentativas restantes e quais letras você já tentou.
5. Digite uma letra e pressione Enter para fazer uma tentativa.
6. Se a letra estiver na palavra secreta, ela será revelada na palavra atual.
7. Se a letra não estiver na palavra secreta, você perderá uma tentativa e a letra será adicionada à lista de erros.
8. Continue adivinhando letras até acertar a palavra ou ficar sem tentativas.
9. Se você acertar a palavra, você ganha o jogo!
10. Se você ficar sem tentativas, você perde o jogo e a palavra secreta será revelada.

## Como Executar o Jogo

Para executar o jogo, siga estas etapas:

1. Certifique-se de ter Python instalado em seu sistema.
2. Certifique-se de ter um arquivo chamado "palavras.py" contendo uma lista chamada "frutas" com as palavras a serem usadas como palavras secretas.
3. Copie o código do jogo para um arquivo Python, como "forca.py".
4. Execute o arquivo Python em um terminal ou ambiente Python de sua escolha.

Certifique-se de que o arquivo "palavras.py" contém algo semelhante a:

```python
frutas = ["banana", "maça", "laranja", "uva", "morango", ...]
```

Aproveite o jogo da forca e divirta-se adivinhando as palavras secretas!
