from flask import Flask, render_template, request, send_file
from DND.generator import generate_character 
from DND.generator import fill_character_sheet # Import vaší funkce pro generování postavy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Získání dat z formuláře
    race = request.form.get('race')
    char_class = request.form.get('class')
    

    # Generování postavy
    character = generate_character()

    return render_template('character.html', character=character)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/download_pdf')
def download_pdf():
    # Vygenerujte PDF pomocí fill_character_sheet
    fill_character_sheet("dnd_character_sheet.pdf", "character_sheet_filled.pdf", character, class_spell_slots[character.char_class.name])
    return send_file("character_sheet_filled.pdf", as_attachment=True)