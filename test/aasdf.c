#include <stdio.h>
#include <string.h>
string inp="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d";
int main()
{
    int val;
    char x=0,y;
    printf("OK");
    for(i=0;i<strlen(inp);i+=2)
    {
        x=inp[i];
        y=inp[i+1];
        if(x>='a'&&x<='f') val=(x-'a'+10)*16;
        else val=(x-'0')*16;
        if(y>='a'&&y<='f') val+=y-'a'+10;
        else val+=y-'0';
        printf("%c",val);
    }
    return 0;
}