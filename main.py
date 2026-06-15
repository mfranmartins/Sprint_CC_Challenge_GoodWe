# ================================================================================
# SPRINT 02: SISTEMA DE RESFRIAMENTO PARA TOTENS DE RECARGA DE VEÍCULOS ELÉTRICOS
# ================================================================================

while True:
    #interface de simulação para o usuário
    print("="*60)
    print(" "*11 + "SISTEMA DE RESFRIAMENTO DO CARREGADOR." + " "*11)
    print("="*60)
    print("Responda às perguntas abaixo para simular os sensores:\n")

    #Perguntas para o usuário simular os sensores do sistema
    print("O Sensor de Temperatura está detectando algo acima de 45ºC?\n")
    print("[1] Sim (Crítico)")
    print("[2] Não (Normal)\n")
    opção_A = int(input("Escolha uma opção: "))
    A = (opção_A == 1)

    print("\nO Carregador está em uso?")
    print("[1] Sim")
    print("[2] Não\n")
    opção_B = int(input("Escolha uma opção: "))
    B = (opção_B == 1)

    print("\nO Sensor de Segurança indica que o Cooler está funcionando corretamente?")
    print("[1] Sim (OK)")
    print("[2] Não (Travado/Falha)\n")
    opção_C = int(input("Escolha uma opção: "))
    C = (opção_C == 1)

    #Processamento lógico para determinar o estado do cooler com base nas variáveis e condicionais
    X = (A or B) and C

    #Condições para diagnóstico e mensagens detalhadas para o usuário
    print("\n" + "="*60)
    print(" "*19 + "DIAGNÓSTICO DO SISTEMA" + " "*19)
    print("="*60)

    if X:
        print("Status do Cooler: LIGADO")
        
        # Validação detalhada dos motivos da ativação
        if A and B:
            print("Motivo: Alta temperatura detectada e veículo em recarga.")
        elif A:
            print("Motivo: Alerta de superaquecimento.")
        elif not A and B:
            print("Motivo: Veículo em carregamento(resfriamento preventivo).")
    else:
        print("Status do Cooler: DESLIGADO")
        
        #Precisa de resfriamento, mas o cooler está com problemas (Alerta Crítico)
        if (A or B) and not C:
            print("\nALERTA: O resfriamento é necessário, mas o cooler está com falha.")
            print("Ação do Sistema: desligando a estação de recarga até a chegada da equipe técnica.")
        
        #O sistema está ocioso, mas foi detectado problemas no cooler (Manutenção Preditiva)
        elif not A and not B and not C:
            print("\nALERTA: Estação ociosa, mas falha no cooler detectada.")
            print("Ação do Sistema: solicitando equipe técnica antes do próximo uso.")
        
        #Tudo desligado porque está tudo bem e seguro
        else:
            print("Motivo: Estação operando em temperatura segura e sem carga ativa.")

    print("="*60)
    
    #Controle de loop para permitir simulações contínuas ou encerrar o programa
    print("\nGostaria de realizar outra simulação?\n")
    print("[1] Sim")
    print("[2] Não (Encerrar)\n")
    resposta = int(input("Escolha uma opção: "))
    
    if resposta != 1:
        print("\nEncerrando o simulador do sistema. Até mais!")
        break
