import pandas 
from flask import Flask,render_template, request, redirect, url_for #importiamo la classe flask
app = Flask(__name__) #inizializza app flask
df = pandas.read_csv('profilo.csv')

@app.route('/') #visitiamo (`/`), la funzione home() viene eseguita.
def home():
    d1 = df.iloc[0].to_dict()
    return render_template("index.html",df = d1)


@app.route('/modifica',methods=['GET','POST'])  #visitiamo (`/`), la funzione home() viene eseguita.
def modifica():
    return render_template("modifica.html")


@app.route('/aggiungi', methods=['POST'])
def aggiungi():
#ottiene elemento dal form
    elemento1 = request.form['elemento1']
    d1["Nome"] = elemento1
    elemento2 = request.form['elemento2']
    d1["Cognome"] = elemento2


@app.route('/ritorna',methods=['GET','POST'])  #visitiamo (`/`), la funzione home() viene eseguita.
def ritorna():
    d1 = df.iloc[0].to_dict()
    return render_template("index.html",df = d1)
#avvio flask
if __name__ == '__main__':
    app.run(debug=True) #aggiornamenti in tempo reale