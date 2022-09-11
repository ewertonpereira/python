#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (){

    char word[50];
    char copy_word[50];
    int size, i, j;

    printf("Digite uma palavra: ");
    fgets(word, 50, stdin);
    strcpy(copy_word, word);
    size = strlen(word);

    j = size - 2;

    // remove => !?,;.
    for(i = 0; i < strlen(word); i++){
        if(word[i] != '!')
    }

    for(i = 0; i < (size - 2); i++){
        if(word[i] != copy_word[j]){
            printf("Nao eh um palindromo.");
            return 0;
        }
        j--;      
    }

    printf("Eh palindromo!\n\n");
    // printf("Size: %d\nWord: %s\nCopy word: %s", size, word, copy_word);

    return 0;
}
