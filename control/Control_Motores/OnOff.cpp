#include <bits/stdc++.h>

//Creamos la clase del controlador
class OnOff
{
private:
public:
    // se definen las funciones de la clase
    
    // init
    OnOff();
    
   // funcion del controlador,
    int OnOffController( int state);
};
// función init
OnOff::OnOff(){}

//función on/off
int OnOff::OnOffController(int state){
    //Si el sensor esta prendido prende el actuador
    if (state)
        return 1;
    //Si el sensor esta apagado el acutador se apaga
    else
        return 0;
}



