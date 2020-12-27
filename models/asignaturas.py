# See LICENSE file for full copyright and licensing details.
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import datetime


class colegioasignaturas(models.Model):
    _name = 'colegio.asignaturas'

    nombreAsig = fields.Text('Nombre de la asignatura', required=True)
    idAsig = fields.Text('Id de la asignatura', required=True)
    obligatoria = fields.Selection([('Si', 'si'), ('No','no')], 'Obligatoria', required=True)
    profesorAsig = fields.Many2one('colegio.profesores', 'nombreProfe')
