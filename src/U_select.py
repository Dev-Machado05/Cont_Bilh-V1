from src import M_txt
import time

def U_Val(txt):
    while True:
        try:
            val = input(txt)
            if val.upper() == "CANCEL" or val.upper() == "CANCELAR":
                Uch()
            v2 = float(val)
            return v2
        except ValueError:
            print("\nValor inválido, digite novamente:")

def conf(Val, N_Ac):
    if N_Ac == "1":
        acao = "redefinir para"
    elif N_Ac == "2":
        acao = "adicionar"
    elif N_Ac == "3":
        acao = "subtrair"
    while True:
        print(f"\nVocê deseja {acao} o valor de {Val}R$?")

        vf = input("\n::>")
        if vf.upper() == "SIM" or vf.upper() == "S":
            return True
        elif vf.upper() == "NAO" or vf.upper() == "N" or vf.upper() == "NÃO":
              Uch(N_Ac)

def An_txt():
    print("""\nO que você deseja fazer hoje?\n
    1- redefinir o valor.
    2- adicionar um aumento no saldo.
    3- Informar um valor gasto.
    4- sair do programa.\n""")

    Us_resp = input("::>")

    if Us_resp == "1" or Us_resp == "2" or Us_resp == "3" or Us_resp == "4":
        Uch(Us_resp)
    else:
        print("\nOpção inválida, por favor, digite novamente:     (￢︿￢⁕)")
        An_txt()

def repeat():
    while True:
        print("você deseja fazer mais algo?")
        resp = input("::>")
        if resp.upper() == "SIM" or resp.upper() == "S":
            An_txt()
        elif resp.upper() == "NAO" or resp.upper() == "NÃO" or resp.upper() == "N":
            print("\nObrigado por utilizar este programa!!    ╰(*°u°*)╯")
            time.sleep(5)
            exit()

def Uch(Us_resp):
    if Us_resp == "1":
        print("\nDigite o novo valor:  (Digite: 'Cancel' para encerrar) \nEx: 20.0\n")
        
        Val = U_Val("::>")
        if conf(Val, Us_resp):
            M_txt.redef(Val)
            print(f"\nO saldo atual agora é de {Val}R$")
        else:
            Uch()

    elif Us_resp == "2":
        print("\nDigite o valor que foi adicionado:   (Digite: 'Cancel' para encerrar) \nEx: 20.0\n")

        Val = U_Val("::>")
        if conf(Val, Us_resp):
            V_tot= M_txt.add(Val)
            print(f"\nO saldo atual agora é de {V_tot}R$")
        else: 
            Uch()
    
    elif Us_resp == "3":
        print("\nDigite o valor gasto: (Digite: 'Cancel' para encerrar) \nEx: 8.80\n")

        Val = U_Val("::>")
        if conf(Val, Us_resp):
            V_tot = M_txt.gast(Val)
            print(f"\nO saldo atual agora é de {V_tot}R$")
        else:
            Uch()

    elif Us_resp == "4":
        print("\nObrigado por utilizar este programa!!    ╰(*°u°*)╯")
        time.sleep(5)
        exit()

    else:
        print("\nOpção inválida, por favor, digite novamente:     (￢︿￢⁕)")
        Uch()

    repeat()