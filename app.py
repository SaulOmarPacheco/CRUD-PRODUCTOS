from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

# crear instancia
app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la base de datos (tabla productos)
class Producto(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)  # SERIAL en PostgreSQL
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': float(self.precio),  # por si lo usas en JSON
            'stock': self.stock,
        }

# Ruta raíz: listar productos
@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

# Crear producto
# @app.route('/productos/new', methods=['GET', 'POST'])
# def create_producto():
#     if request.method == 'POST':
#         nombre = request.form['nombre']
#         descripcion = request.form.get('descripcion')  # puede venir vacío
#         precio = request.form['precio']
#         stock = request.form['stock']

#         nvo_producto = Producto(
#             nombre=nombre,
#             descripcion=descripcion,
#             precio=precio,
#             stock=stock
#         )

#         db.session.add(nvo_producto)
#         db.session.commit()
#         return redirect(url_for('index'))

#     return render_template('create_producto.html')

# Eliminar producto
# @app.route('/productos/delete/<int:id_producto>')
# def delete_producto(id_producto):
#     producto = Producto.query.get(id_producto)
#     if producto:
#         db.session.delete(producto)
#         db.session.commit()
#     return redirect(url_for('index'))

# Actualizar producto
# @app.route('/productos/update/<int:id_producto>', methods=['GET', 'POST'])
# def update_producto(id_producto):
#     producto = Producto.query.get(id_producto)
#     if request.method == 'POST':
#         producto.nombre = request.form['nombre']
#         producto.descripcion = request.form.get('descripcion')
#         producto.precio = request.form['precio']
#         producto.stock = request.form['stock']
#         db.session.commit()
#         return redirect(url_for('index'))

    return render_template('update_producto.html', producto=producto)

if __name__ == '__main__':
    app.run(debug=True)