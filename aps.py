def cript_descript(mensagem, chave):
    txt_cript = []
    for i in range(len(mensagem)):
        criptografia = chr(ord(mensagem[i]) ^ ord(chave[i % len(chave)]))
        txt_cript.append(criptografia)
    return ''.join(txt_cript)

mensagem = input("Digite o texto que você deseja que seja criptografado: ")
chave = input("Digite a chave que deseja ser utilizada para a criptografia: ")

msg_cript = cript_descript(mensagem, chave)
print("Mensagem criptografada:", msg_cript)

max_tentativas = 5
tentativas = 0

while tentativas < max_tentativas:
    senha = input("Digite a senha: ")
    if senha == chave:
        txt_dscript = cript_descript(msg_cript, senha)
        print("Texto descriptografado:", txt_dscript)
        break 
    else:
        tentativas += 1
        tent_rest = max_tentativas - tentativas
        if tent_rest > 0:
            print(f"Senha incorreta, tente novamente! (restam {tent_rest} tentativas).")
        else:
            print("Número máximo de tentativas foi atingido. Seu acesso foi negado!")
