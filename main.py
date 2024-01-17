from flask import Flask, render_template, render_template, request
import poeme_generator as gps

app = Flask(__name__)

@app.route('/')
def page_acceuil():
    return render_template('accueil.html')

@app.route('/S-W.html')
def page_star_wars():
    return render_template('S-W.html')

@app.route('/H-P_page.html')
def page_hp():
    return render_template('H-P_page.html')

@app.route('/S-W_page.html')
def page_lor():
    return render_template('S-W_page.html')

@app.route('/traiter_formulaire', methods=['POST'])
def traiter_formulaire():
    valeur_input1 = request.form.get('monInput1')
    valeur_input2 = request.form.get('monInput2')
    valeur_input3 = request.form.get('monInput3')
    # return f'Voici le poème : {gps.generateur_poeme(input_1=valeur_input1,input_2=valeur_input2,input_3=valeur_input3)}'
    
    return f'Voici les choix : tu es ',valeur_input1, 'tu veux un ', valeur_input2, 'et ton univers est : ', valeur_input3



if __name__ == '__main__':
    app.run(debug=True)