#include <iostream>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <locale>
using namespace std;

void funMatriz(char lcV[6][6]) {
    for(int i=0; i<6; i++) {
        for(int j=0; j<6; j++) {
            lcV[i][j]='O';
        }
    }
}
void funVisual(char lcV[6][6]) {
    cout<<"\t     0   1   2   3   4   5 "<<endl<<endl;
    cout<<"\t0   | "<<lcV[0][0]<<" | "<<lcV[1][0]<<" | "<<lcV[2][0]<<" | "<<lcV[3][0]<<" | "<<lcV[4][0]<<" | "<<lcV[5][0]<<" | "<<endl;
    cout<<"\t1   | "<<lcV[0][1]<<" | "<<lcV[1][1]<<" | "<<lcV[2][1]<<" | "<<lcV[3][1]<<" | "<<lcV[4][1]<<" | "<<lcV[5][1]<<" | "<<endl;
    cout<<"\t2   | "<<lcV[0][2]<<" | "<<lcV[1][2]<<" | "<<lcV[2][2]<<" | "<<lcV[3][2]<<" | "<<lcV[4][2]<<" | "<<lcV[5][2]<<" | "<<endl;
    cout<<"\t3   | "<<lcV[0][3]<<" | "<<lcV[1][3]<<" | "<<lcV[2][3]<<" | "<<lcV[3][3]<<" | "<<lcV[4][3]<<" | "<<lcV[5][3]<<" | "<<endl;
    cout<<"\t0   | "<<lcV[0][4]<<" | "<<lcV[1][4]<<" | "<<lcV[2][4]<<" | "<<lcV[3][4]<<" | "<<lcV[4][4]<<" | "<<lcV[5][4]<<" | "<<endl;
    cout<<"\t0   | "<<lcV[0][5]<<" | "<<lcV[1][5]<<" | "<<lcV[2][5]<<" | "<<lcV[3][5]<<" | "<<lcV[4][5]<<" | "<<lcV[5][5]<<" | "<<endl;
}

main(){setlocale(LC_ALL,"portuguese");
    int minado[6][6], lp=1; 
    char visual[6][6];
    int col, linha; 
    int bk = 1;

    funMatriz(visual);

        srand (time(NULL));
        for(int i=0; i<6; i++) {
            for(int j=0; j<6; j++) {
                minado[i][j]= rand() %3;
            }
        }

    cout<<"Para vencer acerte 5 sem atingir a bomba, Boa sorte!"<<endl;

    while(lp == 1) {
        funVisual(visual);
        cout<<"Indique a coluna: "; cin>>col;
        cout<<"Indique a linha: "; cin>>linha;
        visual[col][linha]='X';
        system("cls");
         
        
        if (bk == 5){
        cout<<"Parabéns, você venceu!";
        lp = 0;
        }

        else if(minado[col][linha]==2) {
            visual[col][linha]='B';
            funVisual(visual);
            cout<<"[ -- DERROTA! -- ]"<<endl;
            cout<<"Linha ["<<col<<"] Coluna ["<<linha<<"] tinha uma bomba :(, tente novamente"<<endl;
            lp = 0;
            system("pause"); 
            system("cls");
        }

        else {
            cout<<"Não tem bomba em ["<<col<<"] ["<<linha<<"], continue..."<<endl;
            bk++;
        }
    }