from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    #render_template > renderiza .html o jinja
    return render_template(
        'inicio.jinja',
        nombre='Joseph',
        dia='Jueves',
        integrantes=['Foca','Lapagol','Ruidiaz','Paolin','Rayoo Advincula'],
        usuario={'nombre':'Juan','direccion':'Las piedritas 105','edad':'40'},
        selecciones=[
            {'nombre':'Bolivia','clasificado':False},
            {'nombre':'Brasil','clasificado':True},
            {'nombre':'Chile','clasificado':False},
            {'nombre':'Peru','clasificado':True}        
        ]
    )

if(__name__ == '__main__'):
    app.run(debug=True)
