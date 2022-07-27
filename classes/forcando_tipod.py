"""
Forçando tipos de dados com decorators


"""
def forca_tipo(*tipos):
    def decorador(function):
        def convert(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor)) 
            return function(*novo_args, **kwargs)
        return convert
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Ewerton, tu é top!', '12')

@forca_tipo(float, float)
def dividir(a, b):
    print(a / b) 


dividir('1', 5)
