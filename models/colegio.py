# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
import datetime

class colegiocolegio(models.Model):
        _name = 'colegio.colegio'
        nombre = fields.Text('Nombre del centro', required=True)
        id = fields.Char('Identificador' , required=True)
        educacion= fields.Selection([
            ('publica'),
            ('privada'),
            ('concertada')
        ])
        materiales = fields.Many2one('colegio.materiales', 'Proveedor de Materiales', required=True)




class colegioprofesores(models.Model):
    _name = 'colegio.profesores'

    @api.depends('nacimiento', 'edad')

    def _edad(self):
            self.edad=datetime.date.today().year - self.nacimiento.year

    nombreProfe = fields.Text('Nombre')
    apellido = fields.Text('Apellido')
    nacimiento = fields.Date('Año nacimiento', required=True, default=fields.Date.context_today)
    edad = fields.Integer('Años', compute='_edad')
    director = fields.Boolean('Director')
    centro = fields.One2one('colegio.colegio', 'Centro', required=True)
    aula = fields.One2one('colegio.aulas', 'Aulas', required=True)




class colegioaulas(models.Model):
        _name = 'colegio.aulas'

        idAula = fields.Text('Aula', required=True)
        profesorAula = fields.One2one('colegio.profesores', 'Profesor', required=True)
        delegado = fields.One2one('colegio.alumnos', 'Delegado', required=True)
        bilingue = fields.Boolean('Bilingue')




class colegioprovedores(models.Model):
        _name = 'colegio.provedores'

         @api.depends('cantidad', 'prize')
    def _equal(self):
        self.equal = self.cantidad *self.prize *(26/100)
        
    marca = fields.Text('Marca', required=True)
    modelo = fields.Text('Modelo', required=True)
    cantidad = fields.Float(string='Cantidad')
    prize = fields.Float(string='prize', required=True)
    equal = fields.Float(string='equal', compute='_equal')
    

class colegioalumnos(models.Model):
        _name = 'colegio.alumnos'

        aula = fields.One2one('colegio.aulas', 'Aula', required=True)
        profesor = fields.One2one('colegio.profesores', 'Porfesor', required=True)
        nombreAlumno = fields.Text('Nombre alumno', required=True)
        apellidoAlumno = fields.Text('Apellido alumno')