def notas(* a,sit=False):
    if sit==True:
        print(
        """
        PROGRAMA PARA AVALIAR SUA CONDUTA ESCOLAR
        """
        )
    dic={}
    soma=0
    maior=max(a)
    menor=min(a)
    soma=sum(a)
    media=soma/len(a)
    dic['quantidade de notas']=len(a)
    dic['maior nota'] =maior
    dic['menor nota'] =menor
    dic['media das notas'] =media
    print(dic)
    if media>=7:
        print('\033[32m BOA')
    elif media>=5 and media<7:
        print('\033[33m RASOAVEL')
    elif media<5:
        print('\033[31m RUIM')


n1=float(input('DIGITE SUA PRIMEIRA NOTA:'))
n2=float(input('DIGITE SUA SEGUNDA NOTA:'))
n3=float(input('DIGITE SUA TERCEIRA NOTA:'))
opc=str(input('DIGITE SE QUER RECEBER INFO EXTRA [S/N]')).upper().strip()[0]
while opc not in 'SsNn':
    opc = str(input('DIGITE SE QUER RECEBER INFO EXTRA [S/N]')).upper().strip()[0]
if opc in 'Ss':
    notas(n1,n2,n3,sit=True)
else:
    notas(n1, n2, n3, sit=False)



