"""
Dunder Name e Dunder Maim

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando Double Under 
para não gerar conflito com os nomes desses  elementos na programação.

# Na linguagem C, temos um programa na seguinte forma:

int main(){

    return 0;
}

# na linguagem java, temos um programa da seguinte forma:

public static void main(string[] args){

}

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente o Python
atribuirá a variável __name__ o valor __main__ indicando que esse módulo é o módulo de execução principal.


"""