def cifra_cesar(texto, deslocamento, operacao='criptografar'):
    resultado = ""
    
    # Se for descriptografar, inverte o deslocamento
    if operacao == 'descriptografar':
        deslocamento = -deslocamento
    
    for char in texto:
        if char.isalpha():
            # Determina se é maiúscula ou minúscula
            ascii_base = ord('A') if char.isupper() else ord('a')
            
            # Aplica o deslocamento mantendo dentro do alfabeto
            novo_char = chr((ord(char) - ascii_base + deslocamento) % 26 + ascii_base)
            resultado += novo_char
        else:
            # Mantém caracteres não alfabéticos inalterados
            resultado += char
    
    return resultado

def main():
    print("=== CIFRA DE CÉSAR ===")
    print("1. Criptografar mensagem")
    print("2. Descriptografar mensagem")
    print("3. Sair")
    
    while True:
        try:
            opcao = input("\nEscolha uma opção (1-3): ").strip()
            
            if opcao == '3':
                print("Programa encerrado!")
                break
            
            elif opcao in ['1', '2']:
                # Solicita a mensagem
                mensagem = input("Digite a mensagem: ")
                
                # Solicita o deslocamento
                while True:
                    try:
                        deslocamento = int(input("Digite o número de deslocamentos: "))
                        break
                    except ValueError:
                        print("Por favor, digite um número inteiro válido.")
                
                # Processa a mensagem
                if opcao == '1':
                    resultado = cifra_cesar(mensagem, deslocamento, 'criptografar')
                    print(f"\nMensagem criptografada: {resultado}")
                else:
                    resultado = cifra_cesar(mensagem, deslocamento, 'descriptografar')
                    print(f"\nMensagem descriptografada: {resultado}")
            
            else:
                print("Opção inválida! Escolha 1, 2 ou 3.")
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# Função adicional para teste rápido
def exemplo_uso():
    """Exemplo de como usar a cifra de César"""
    print("\n" + "="*50)
    print("EXEMPLO DE USO:")
    print("="*50)
    
    mensagem_original = "Bio Hacking"
    deslocamento = 3
    
    print(f"Mensagem original: {mensagem_original}")
    print(f"Deslocamento: {deslocamento}")
    
    # Criptografar
    mensagem_criptografada = cifra_cesar(mensagem_original, deslocamento, 'criptografar')
    print(f"Mensagem criptografada: {mensagem_criptografada}")
    
    # Descriptografar
    mensagem_descriptografada = cifra_cesar(mensagem_criptografada, deslocamento, 'descriptografar')
    print(f"Mensagem descriptografada: {mensagem_descriptografada}")

if __name__ == "__main__":
    # Executa o exemplo
    exemplo_uso()
    
    # Executa o programa principal
    main()