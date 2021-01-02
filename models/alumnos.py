# See LICENSE file for full copyright and licensing details.
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import datetime


class colegioalumnos(models.Model):
        _name = 'colegio.alumnos'


        @api.depends('nacimiento')
        def _calc_alumno_edad(self):
           self.edadAlumno=datetime.date.today().year - self.nacimientoAlumno.year

        aula = fields.Many2one('colegio.aulas', 'idAulas', requiered=True)
        profesor = fields.Many2one('colegio.profesores', 'nombreProfe', required=True)
        nombreAlumno = fields.Text('Nombre alumno', required=True)
        apellidoAlumno = fields.Text('Apellido alumno', required=True)
        nacimientoAlumno = fields.Date('Nacimiento', required=True)
        edadAlumno = fields.Integer('Edad', compute='_calc_alumno_edad')
        genero = fields.Selection([('Masculino','masculino'),('Femenino', 'femenino')],
                            'Genero', required=True)
        delegado = fields.Selection([('Si','si'),('No','no')],'Delegado', required=True)

        
