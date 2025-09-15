from flask import Flask,render_template,redirect,request
import random


# declaramos la aplicacion
app = Flask(__name__)


contador = 1
sum = 1
mensaje = ''


# OPCION 1 
# responsive design: que la pagina web se vea bien segun la resolucion


# OPCION 2
# Arrays: o como organizar multiples variables (mas dificil pero importante)



@app.route("/",methods=["GET","POST"])
def principal ():

    # pasas esa variable a la pagina web
    global contador,mensaje


    nombre = request.form.get("nombre")
    return render_template("index.html",contador = contador,mensaje = mensaje)

@app.route("/sumar")
def sumar():
    global contador
    global sum
    contador = contador + sum

    return redirect("/")


@app.route("/mejorarBoton")
def mejorarBoton():
    global sum,contador

    if contador > 15:
        sum = sum + 1
        contador = contador - 15

    return redirect("/")


@app.route('/CadenaDeVirus')

def CadenaDeVirus():
    


    for i in range(10):
        # i es un numero que va de desde 0 a 10.
        # i es un numero, necesito que sea un texto
        # si queres pasar de un numero (int) a un texto (string)
        # pones str(i)


        with open("virus"+ str(i)  +".txt","w") as archivo:
        
            archivo.write("te han hackeado hahaha :)")
        


        
    return ''


#  == algo es igual a otro
# < menor 
# > mayor
# <= menor o igual
# >=
# != distinto a



# texto = string
# numeros enteros = int
# decimales 6.1 7.5 = float




@app.route("/recibirInformacion",methods=["GET","POST"])


def recibirInformacion():
    año = 2025 - 12  #1998
    # si naciste antes o despues de julio
    nacisteDespues = "no"
    
    # si naciste despues normal

    # if nacisteDespues == "si":
        # vas todo  normal

    
    # si naces antes de julio un año mas
    if nacisteDespues == "no":
        año = año - 1




    return str(año)


@app.route('/azar')
def azar():
    numAzar = random.randint(0,6)
    
    texto = "salio: " + str(numAzar)

    # si no sale el 6 volve a probar con otro numero al azar
    # mientras que no sea el numero 6 volve a probar con otro numero
    while numAzar != 6:
        numAzar = random.randint(0,6)
        texto = texto + " salio: " + str(numAzar)
    



    return texto






# como hago para que no se resetee
# que se reste 
@app.route('/loteriaNacional')
def loteriaNacional():
    global contador
    numAzar = random.randint(1,6)
    
    # str = string = texto
    # int = numero
    # cuando sale el  numero 6 ganamos
    if (numAzar == 6):
        contador = contador + 100


    return "yo tengo " + str(contador) + " monedas, salio el numero " + str(numAzar)










@app.route('/ejercicioTexto')
def ejercicioTexto():
    # mostrame desde que naciste la edad que tenias en cada año
    añoNacimiento = 2014
    edad = 0
    texto = "El año es " + str(añoNacimiento) +" y vos tenias  "+ str(edad)+" año/s."

    for i in range (5):
        añoNacimiento = añoNacimiento + 1
        edad = edad + 1

        texto = texto + " El año es " + str(añoNacimiento) +" y vos tenias  "+ str(edad)+" año/s."

    #hacemos una variable "añoactual", y si es menor el año y la edad que diga tenias,
    # si es igual que el año y la edad que diga "tienes", y que si es mayo diga "tendras" 
    # cambiar de texto a numero
    return texto



# definir la ruta
@app.route('/boton')
# definir que se muestra
def casa():
    return '''

    <button   onclick="window.location.href = '/virus'"   >haga click aqui</button>
    
    '''

# ruta (depende de lo que escribas en la pagina te lleva)
@app.route('/virus')
# esto es la funcion
def jorje():
    # crear un archivo 
    with open("virus.txt","w") as archivo:
        #contenido
        archivo.write("te han hackeado hahaha :)")

        # se ejecuta apenas inicia la pagina web
    return '''

   se te instalo un virus
    '''



# inicio la aplicacion
app.run(host="0.0.0.0",port = int(os.environ.get("PORT",10000)))





