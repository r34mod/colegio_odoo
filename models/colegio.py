# -*- coding: utf-8 -*-


from odoo import api, fields, models,tools, _
import datetime

##One2Many que puede haber muchos en un mismo sitio

##Many2one eliges uno de muchos

class colegiocolegio(models.Model):
        _name = 'colegio.colegio'
        nombre = fields.Text('Nombre del centro', required=True)
        idCentro = fields.Char('Identificador' , required=True)
        educacion= fields.Selection([
            ('publica'),
            ('privada'),
            ('concertada')
        ])
        aulaCentro = fields.One2many('colegio.aulas', 'idAula', 'Aula')
        profesoresCentro = fields.One2many('colegio.profesores', 'nombreProfe', 'Profesor')
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
    centro = fields.One2Many('colegio.colegio', 'nombre', 'Centro', required=True)
    aula = fields.Many2one('colegio.aulas', 'Aulas', required=True)




class colegioaulas(models.Model):
        _name = 'colegio.aulas'

        idAula = fields.Text('Aula', required=True)
        profesorAula = fields.Many2one('colegio.profesores', 'Profesor', required=True)
        delegado = fields.Many2one('colegio.alumnos', 'Delegado', required=True)
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
    



