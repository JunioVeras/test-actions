import os,sys,maltplotlib   # múltiplos imports na mesma linha (E401)


def handler(event,context):   # espaços errados (E231), nome ok mas estilo ruim
    unused_variable = 123     # variável não usada (F841)

    if(event==None):          # comparação errada com None (E711)
        print("No event")

    result=do_something(  event )  # espaços estranhos (E201, E202)

    return  result            # espaço extra