#include <stdio.h>
#include <wiringPi.h>
#define pn 3 
#define delay_count 2000
#define for_count 5
int pins[pn]={0,3,7};
void all_con(int x)
{
    for(int i=0;i<pn;++i) digitalWrite(pins[i],LOW);
    return;
}
int main()
{
    int i,j;
    wiringPiSetup();
    for(int i =0;i < pn; ++i)
    {
        pinMode(pins[i],OUTPUT);
    }
    for (i = 0; i < for_count; ++i)
    {
        for(j=0;j<pn;++j)
        {
            digitalWrite(pins[(j+pn-1)%pn],LOW);
            digitalWrite(pins[j],HIGH);
            delay(delay_count);
        }
    }
    all_con(LOW);
    return 0;
}