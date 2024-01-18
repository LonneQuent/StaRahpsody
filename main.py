from flask import Flask, render_template, render_template, request
import generateur_poeme_starwars as gps

app = Flask(__name__)

@app.route('/')
def page_acceuil():
    return render_template('index.html')

@app.route('/page_sw.html')
def page_star_wars():
    return render_template('page_sw.html')

@app.route('/page_hp.html')
def page_hp():
    return render_template('page_hp.html')

@app.route('/page_lor.html')
def page_lor():
    return render_template('page_lor.html')

@app.route('/traiter_formulaire', methods=['POST'])
def traiter_formulaire():
    valeur_input1 = request.form.get('monInput1')
    valeur_input2 = request.form.get('monInput2')
    valeur_input3 = request.form.get('monInput3')
    return f'Voici le poème : {gps.generateur_poeme(input_1=valeur_input1,input_2=valeur_input2,input_3=valeur_input3)}'
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
