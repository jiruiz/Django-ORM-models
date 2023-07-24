from django import forms 

class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    telefono = forms.CharField(label="telefono")
    servicio = forms.CharField(label="servicio")

    """"""
    solo_empresas = forms.BooleanField(label="Es solo para empresas?", required=False)
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )
    turno = forms.ChoiceField(label="Turno", choices=TURNOS)
    fecha_inicio = forms.DateField(label="Fecha Inicio")

'''
    # Campo de texto
    text = forms.CharField(label="Texto", max_length=100)

    # Campo de contraseña
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    # Campo de texto múltiple (textarea)
    textarea = forms.CharField(label="Área de texto", widget=forms.Textarea)

    # Campo de número entero
    integer = forms.IntegerField(label="Entero")

    # Campo de número decimal
    decimal = forms.DecimalField(label="Decimal", max_digits=5, decimal_places=2)

    # Campo de fecha
    date = forms.DateField(label="Fecha")

    # Campo de hora
    time = forms.TimeField(label="Hora")

    # Campo de fecha y hora
    datetime = forms.DateTimeField(label="Fecha y Hora")

    # Campo de selección
    choice = forms.ChoiceField(label="Selección", choices=[("opcion1", "Opción 1"), ("opcion2", "Opción 2")])

    # Campo de selección múltiple
    multiple_choice = forms.MultipleChoiceField(label="Selección múltiple", choices=[("opcion1", "Opción 1"), ("opcion2", "Opción 2")])

    # Campo de archivo
    file = forms.FileField(label="Archivo")

    # Campo de imagen
    image = forms.ImageField(label="Imagen")

    # Campo de correo electrónico
    email = forms.EmailField(label="Correo electrónico")

    # Campo de URL
    url = forms.URLField(label="URL")

    # Campo de booleano (checkbox)
    boolean = forms.BooleanField(label="Booleano", required=False)

    # Campo oculto
    hidden = forms.HiddenInput()

    # Campo de UUID
    uuid = forms.UUIDField(label="UUID")

    # Campo de opción múltiple con checkboxes
    checkbox_select_multiple = forms.MultipleChoiceField(label="Opción múltiple con checkboxes", choices=[("opcion1", "Opción 1"), ("opcion2", "Opción 2")], widget=forms.CheckboxSelectMultiple)

    # Campo de opción múltiple con select
    select_multiple = forms.MultipleChoiceField(label="Opción múltiple con select", choices=[("opcion1", "Opción 1"), ("opcion2", "Opción 2")], widget=forms.SelectMultiple)

    # Campo de lista desplegable
    dropdown = forms.ChoiceField(label="Lista desplegable", choices=[("opcion1", "Opción 1"), ("opcion2", "Opción 2")], widget=forms.Select)

    # Campo de lista desplegable con búsqueda
    autocomplete = forms.CharField(label="Lista desplegable con búsqueda", widget=forms.TextInput(attrs={"data-select2-tags": "true"}))
    # Campo de número de teléfono
    phone_number = forms.CharField(label="Número de teléfono", max_length=20)

    # Campo de dirección postal
    address = forms.CharField(label="Dirección", widget=forms.Textarea)

    # Campo de código postal
    postal_code = forms.CharField(label="Código Postal", max_length=10)
    
    # Campo de texto con validación de longitud mínima y máxima
    text_length = forms.CharField(label="Texto con longitud", min_length=5, max_length=20)

    # Campo de número entero con rango mínimo y máximo
    integer_range = forms.IntegerField(label="Entero con rango", min_value=1, max_value=10)

    # Campo de elección con widget RadioSelect
    radio_choice = forms.ChoiceField(label="Elección con radio", choices=[("opcion1", "Opción 1"), ("opcion2", "Opción 2")], widget=forms.RadioSelect)

    # Campo de selección múltiple con widget CheckboxSelectMultiple
    checkbox_multiple_choice = forms.MultipleChoiceField(label="Selección múltiple con checkboxes", choices=[("opcion1", "Opción 1"), ("opcion2", "Opción 2")], widget=forms.CheckboxSelectMultiple)

    # Campo de fecha con widget SelectDateWidget
    select_date = forms.DateField(label="Fecha con select", widget=forms.SelectDateWidget)



    # Campo de texto con widget PasswordInput
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    

    # Campo de elección con widget SelectMultiple
    select_multiple = forms.ChoiceField(label="Selección múltiple con select", choices=[("opcion1", "Opción 1"), ("opcion2", "Opción 2")], widget=forms.SelectMultiple)

    # Campo de fecha con widget DateInput
    date_input = forms.DateField(label="Fecha con input", widget=forms.DateInput)

    # Campo de hora con widget TimeInput
    time_input = forms.TimeField(label="Hora con input", widget=forms.TimeInput)

    # Campo de texto con widget Textarea y atributos personalizados
    textarea_custom = forms.CharField(label="Área de texto personalizada", widget=forms.Textarea(attrs={"rows": 4, "cols": 40}))


'''