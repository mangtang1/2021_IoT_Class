#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <cstring>
using namespace std;
int valid(string str) {

    string input = str;
    int i, j, flag = 1;
    string str1 = "CmpFny4T@1d";
    if(input.length()!=18) return 0;
    string letters = str1;
    for (i = 4; i < 18; i++) {
        for (j = 0; j < letters.length(); j++) {
            flag = 1;
            if (input[i] == letters[j]) {
                flag = 0;
                break;
            }
        }
        if (flag == 1) {
            break;
        }
    }
    if (flag == 1) {
        return 0;
    }
    if (input[0] != 'k') return 0;
    if (input[1] != '3') return 0;
    if (input[2] != '3') return 0;
    if (input[3] != 'p') return 0;

    if (input[4] != input[15]) return 0;
    if (input[5] != input[8]) return 0;
    if (input[6] != input[12]) return 0;

    if ((input[7] - input[4]) != 42) return 0;
    if ((input[7] + 1) != input[9]) return 0;
    if ((input[9] % input[8]) != 46) return 0;
    if ((input[11] - input[8] + input[2]) != 'c') return 0;
    if ((input[14] - input[6]) != (input[17] + 2)) return 0;
    if ((input[9] % input[5]) * 2 != (input[13] + 40)) return 0;
    if ((input[4] % input[13]) != 15) return 0;
    if ((input[14] % input[13]) != (input[12] - 32)) return 0;
    if (((input[7] % input[6]) + 89) != input[10]) return 0;
    if ((input[16] % input[15]) != 17) {
        cout<<(input[16] % input[15]);
        return 0;
    }
    int x = 0;
    int y = 132;
    for (i = 4; i < 18; i++) {
        x = x ^ input[i];
        y = y + input[i];
    }
    if (x != 72) return 0;
    if (y != 1250) return 0;

    return 1;
}
void makestring(int no,string res)
{
    if(no==17)
    {
        if(valid(res))
        {
            cout<<res<<" Correct!";
            exit(0);
        }
        return;
    }
    for(int i=0;i<128;++i)
    {
        res[no+1]=i;
        makestring(no+1,res);
    }

}
int main()
{
    string inp="k33p                             ";
    cout<<"Start!";
    //makestring(3,inp);

}