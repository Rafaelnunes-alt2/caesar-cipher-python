# caesar-cipher-python

Cifra Caesar por CLI, Python stdlib puro. Encripta e decripta preservando
case e ignorando não-letras.

## Uso

    python3 caesar.py --text "Hello World" --shift 3 --encrypt
    python3 caesar.py --text "Khoor Zruog" --shift 3 --decrypt
    printf 'abc xyz' | python3 caesar.py --shift 5 --encrypt

## Testes validados

    Hello World +3 vira Khoor Zruog — OK
    Khoor Zruog -3 volta Hello World — OK
    stdin com shift 5 vira fgh cde — OK

## Limitações

É cifra clássica dicional, não é criptografia segura. Shuntado em shift 0-25.

## Autor

Rafael Nunes — [@Rafaelnunes-alt2](https://github.com/Rafaelnunes-alt2)
