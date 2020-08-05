from flask import Flask,render_template

app=Flask(__name__)

lista=[]
for i in range(101,120):
  lista.append(i)
  i=i+2
  

@app.route("/")
def index():
  titulo="home"
  return render_template("index.html",titulo=titulo,lista=lista) 

if __name__=="__main__":
  app.run(debug=True)
