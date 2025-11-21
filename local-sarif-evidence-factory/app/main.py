from flask import Flask, request, jsonify

app = Flask(__name__)

# Code smell: variable global mutable
calculation_history = []

# Code smell: función muy larga, sin validación
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    op = data['operation']
    a = data['a']
    b = data['b']
    
    # Code smell: demasiados if/elif anidados
    if op == 'add':
        result = a + b
    elif op == 'subtract':
        result = a - b
    elif op == 'multiply':
        result = a * b
    elif op == 'divide':
        result = a / b  # Code smell: sin manejo de división por cero
    else:
        result = None
    
    calculation_history.append({'op': op, 'result': result})
    return jsonify({'result': result})

@app.route('/history', methods=['GET'])
def history():
    return jsonify(calculation_history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**app/requirements.txt:**
```
flask==2.3.0
requests==2.31.0