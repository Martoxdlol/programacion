#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <ctype.h>

// Nota: según mi implementación cualquier caracter que no sea un espacio es parte de la palabra

void title_case(char s[]) {
    int isFirstLetter = 1;
    for (int i = 0; s[i] != '\0'; i++)
    {
        if(isalpha(s[i]) && isFirstLetter){
            s[i] = toupper(s[i]);
            isFirstLetter = 0;
        }else if(isalpha(s[i])){
            s[i] = tolower(s[i]);
        }else if(s[i] == ' '){
            isFirstLetter = 1;
        }
    }
    
}

int main(void) {
    char s[] = "HoLa QuE tAl";
    title_case(s);
    assert(!strcmp(s, "Hola Que Tal"));

    // OPCIONAL: pruebas adicionales
    char s2[] = "HOla-Ke asE";
    title_case(s2);
    assert(!strcmp(s2, "Hola-ke Ase"));

    printf("%s: OK\n", __FILE__);
    return 0;
}
