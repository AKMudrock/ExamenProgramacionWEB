from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#menu principal
@app.route('/')
def index():
    return render_template('index.html')

#formulario ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])
        
        valor_tarro = 9000
        total_sin_descuento = cantidad_tarros * valor_tarro
        
        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0
        
        total_descuento = total_sin_descuento * (1 - descuento)
        
        return render_template('ejercicio1.html', nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               total_descuento=total_descuento)
    return render_template('ejercicio1.html')

#formulario ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ''
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        
        if usuario == 'juan' and contrasena == 'admin':
            mensaje = f'Bienvenido administrador {usuario}'
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = f'Bienvenido usuario {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'
    
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)