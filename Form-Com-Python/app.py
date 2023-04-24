from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/operacao", methods=['POST','GET'])
def write():
    print('Requisições')
    if request.method == 'POST':
        print('Requisições')
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        n3 = int(request.form['n3'])

        oper = (n1 + n2 + n3) * 2
    else:
        print('Requisições')
        n1 = int(request.args.get['n1'])
        n2 = int(request.args.get['n2'])
        n3 = int(request.args.get['n3'])

        oper = (n1 + n2 + n3) * 2
    return f'Operação: {oper}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)