{
    'name': 'Control de Colegios',
    'sequence': 120,
    'version': '1.0',
    'depends': ['base'],
    'category': 'Schools',
    'summary': 'Control de Colegios',
    'description': """ Modulo para visualizar los datos de cualquier centro
    escolar registrado de manera rapida y eficiente""",

    'data': [
        'views/colegio_view.xml',
        'views/colegio_provedores.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable':True,
    'aplication':True,

}