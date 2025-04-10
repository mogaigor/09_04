import pandas 
from flask import Flask,render_template, request, redirect, url_for #importiamo la classe flask
app = Flask(__name__) #inizializza app flask


@app.route('/') #visitiamo (`/`), la funzione home() viene eseguita.
def home():
    df = pandas.read_csv('profilo.csv')
    d1 = df.iloc[0].to_dict()
    return render_template("index.html",df = d1)


@app.route('/modifica',methods=['GET','POST'])  #visitiamo (`/`), la funzione home() viene eseguita.
def modifica():
    return render_template("modifica.html")


@app.route('/aggiungi', methods=['GET','POST'])
def aggiungi():
#ottiene elemento dal form
    if request.method == "POST":
        nuovo_profilo = {
            "Nome": request.form["elemento1"],
            "Cognome": request.form["elemento2"],
            "Scuola": request.form["elemento3"],
            "Hobby": request.form["elemento4"]
        }
        df = pandas.DataFrame([nuovo_profilo])
        df.to_csv("profilo.csv", index=False)
        return redirect(url_for('home'))
    df = pd.read_csv("profilo.csv")
    d1 = df.iloc[0].to_dict()
    return render_template("modifica.html", df=d1)


#avvio flask
if __name__ == '__main__':
    app.run(debug=True) #aggiornamenti in tempo reale