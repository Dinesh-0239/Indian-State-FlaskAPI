from flask import Flask, jsonify, request, redirect, render_template
from state_data import states  # fix import to actual filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        state_name = request.form.get('state_name')
        return redirect(f'/states/{state_name}')
    return render_template('index.html')


@app.route('/states/<string:state_name>', methods=['GET'])
def get_state_info(state_name):
    state_info = states.get(state_name.title())
    if state_info:
        return jsonify({
            'Name': state_name.title(),
            'Information' : state_info
        })
    else:
        return jsonify({'error': 'State not found'}), 404

if __name__ == '__main__':
    app.run(debug=True,port=8000)
