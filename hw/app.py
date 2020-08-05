from flask import Flask, request
app=Flask(__name__)

@app.route("/")
def index():
  return("<h1>Hello World!!!!</h1>")

@app.route("/hola")
def hola():
  return("hola.")

@app.route("/user/<string:user>")
def user(user):
  return "Hola "+user

@app.route("/numero/<int:n>")
def numero(n):
  return "El doble de {} es {}.".format(n,2*n)

@app.route("/primos/<int:n>")
def primos(n):
    pagina="<h1>Generaion de "+str(n)+" numeros primos</h1><br>"
    pagina+='2<br>'
    for i in range(3,n,2):  
        for j in range(3,i,2):  
            if i%j==0:  
                break  
        else:         
            pagina+=str(i)+'<br>'   
    return pagina

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
  return "<p>ID: {} <br> Nombre de usuario: {}</p>".format(id,username)

@app.route("/suma")
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1="7",n2="3"):
  return "Si sumamos {} y {} obtendremos {}".format(n1,n2,float(n1)+float(n2))

@app.route("/parames")
def parames():
  param=request.args.get('params1','Vacío')
  return 'El parámetro es {}'.format(param)

@app.route("/params")
def params():
  param1=request.args.get('ciudad','N/D')
  param2=request.args.get('habitantes','N/D')
  return('La ciudad de {} tiene {} millones de habitantes.'.format(param1,param2))




if __name__=="__main__":
  app.run(debug=True,host='0.0.0.0')

