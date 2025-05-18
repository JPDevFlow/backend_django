# Importa la clase base para formularios de Flask-WTF
from flask_wtf import FlaskForm

# Importa el validador que asegura que un campo no esté vacío
from wtforms.validators import DataRequired

# Importa campos de tipo texto y botón de envío
from wtforms.fields.simple import StringField, SubmitField

# Importa campo de tipo numérico entero
from wtforms.fields.numeric import IntegerField

# Define una clase de formulario para clientes, heredando de FlaskForm
class ClienteForma(FlaskForm):
    # Campo de texto para el nombre, obligatorio
    nombre = StringField("Nombre", validators =[DataRequired()])
    # Campo de texto para el apellido, obligatorio
    apellido = StringField("Apellido", validators=[DataRequired()])
    # Campo numérico para la membresía, obligatorio
    membresia = IntegerField("Membresia", validators=[DataRequired()])
    # Botón para enviar el formulario
    guardar = SubmitField("Guardar")
