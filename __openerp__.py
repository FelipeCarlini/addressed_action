# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2017-TODAY Eynes - Ingenieria del software.
#	 (http://www.eynes.com.ar) All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Addressed Action",
    "category": "Other",
    "version": "8.0.1.0.0",
    "description": "Allows quick access to a actions",
    "author": "Eynes",
    "website": "http://www.eynes.com.ar/",
    "data": [
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/addressed_action_view.xml",
    ],
    "qweb": [
        "static/src/xml/base.xml",
    ],
    "installable": True,
    "application": True,
}
