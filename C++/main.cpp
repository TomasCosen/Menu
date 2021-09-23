#include <iostream>
#include <time.h>
#include <windows.h>
#include <stdlib.h>
#include <iomanip>
using namespace std;
typedef struct{
    string nombresensor;
    double medicion;
    string unidad;
    int prioridad;
}sensores;
sensores listasensores[10];
void altasensor();
void bajasensor();
void modsens();
void visualsensor();
int i = 0;

int main()
{
    int opcion, sino;
    do{
        system("cls");
        cout << "1 - Conectar Sensor " << endl;
        cout << "2 - Eliminar Sensor "<< endl;
        cout << "3 - Modificar Sensor " << endl;
        cout << "4 - Visualizar Sensores " << endl;
        cout << "5 - Salir" << endl;
        cout << "Ingrese opcion: ";
        cin >> opcion;

        switch (opcion){
            case 1:
                altasensor();
                break;
            case 2:
                bajasensor();
                break;
            case 3:
                modsens();
                break;
            case 4:
                visualsensor();
                break;
            case 5:
                cout << "Seguro que quieres salir?" << endl;
                cout << "1 - SI" << endl;
                cout << "2 - NO" << endl;
                cin >> sino;
                if (sino == 1){
                    return 0;
                }
                else{
                    return main();
            }
            break;
        }



    }while(opcion != 5);
}
void altasensor(){
    cout << "Ingrese el nombre del sensor: ";
    cin >> listasensores[i].nombresensor;
    cout << "Ingrese el numero de prioridad(1-10): ";
    cin >> listasensores[i].prioridad;
    cout << "Ingrese la unidad de medicion: ";
    cin >> listasensores[i].unidad;
    i ++;
    system("pause");
    return;
}
void bajasensor(){

    int k, senselim;
    for (k = 0; k < 10; k++){
        cout << "Sensor - " << k <<", "<< listasensores[k].nombresensor << endl;
    }
    cout << "Seleccione el sensor a eliminar: ";
    cin >> senselim;
    for (k =0; k < 10; k++){
        if (k == senselim){
            listasensores[senselim].nombresensor = " " ;
            listasensores[senselim].medicion = 0;
            listasensores[senselim].prioridad = 0;
            listasensores[senselim].unidad = " " ;
        }
    }
    cout << "Se ha eliminado el sensor: " << senselim <<endl;
    ///i = senselim;
    system("pause");
    return;
}

void modsens(){

    int k, sensmod;
    for (k = 0; k < 10; k++){
        cout << "Sensor - " << k <<", "<< listasensores[k].nombresensor << endl;
    }
    cout << "Seleccione el sensor a modificar: ";
    cin >> sensmod;
    for (k =0; k < 10; k++){
        if (k == sensmod){
            cout << "Ingrese el nuevo nombre del sensor: ";
            cin >> listasensores[sensmod].nombresensor;
            cout << "Ingrese el nuevo numero de prioridad(1-10): ";
            cin >> listasensores[sensmod].prioridad;
            cout << "Ingrese la nueva unidad de medida: ";
            cin >> listasensores[sensmod].unidad;
        }
    }
    cout << " " << sensmod <<endl;
    cout << "Se guardo el sensor: " << sensmod <<endl;
    cout << "Con el nombre: " << listasensores[sensmod].nombresensor <<endl;
    cout << "Numero de prioridad: " << listasensores[sensmod].prioridad <<endl;
    cout << "Y unidad: " << listasensores[sensmod].unidad <<endl;
    system("pause");
    return;
}
void visualsensor(){
    int k;
    srand(time(0));
    while (true){
        system("cls");
        for (k = 0; k < 10; k++){
            if (listasensores[k].prioridad == 0){
                cout << "Sensor no conectado" << endl;
            }
            else{
                cout << "Nombre del Sensor  ;  Medicion  ;  Unidad  ;  Prioridad" << endl;
                cout << listasensores[k].nombresensor << "  ;  ";
                listasensores[k].medicion = rand()%(51);
                cout << listasensores[k].medicion << "  ;  ";
                cout << listasensores[k].unidad << "  ;  ";
                cout << listasensores[k].prioridad << endl;
            }
        }
        if ((GetAsyncKeyState(27))){
            break;
        }
        cout << "Presiona ESC para volver al menu anterior";
        Sleep(1000);
    }
    return;
}
