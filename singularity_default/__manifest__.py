# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2022 jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
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
# -----------------------------------------------------------------------------------
{
    "name": "singularity",
    "version": "16.0.1.0.0",
    "license": "Other OSI approved licence",
    "category": "Tools",
    "summary": "Customización Singularity",
    "author": "jeo Software",
    "depends": [
    ],
    "data": [],
    "test": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": [],
    "config": [],
    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # manifest version, if omitted it is backward compatible
    "env-ver": "2",
    # if Enterprise it installs in a different directory than community
    "odoo-license": "EE",
    # port where odoo starts serving pages
    "port": "8069",
    # list of url repos to install in the form 'repo-url directory'
    "git-repos": [
        "git@github.com:jobiols/cl-singularity",
        "git@github.com:jobiols/jeo-enterprise.git",
        # ingadhoc
        "https://github.com/ingadhoc/odoo-argentina ingadhoc-odoo-argentina",
        "https://github.com/ingadhoc/account-financial-tools ingadhoc-account-financial-tools",
        "https://github.com/ingadhoc/account-invoicing ingadhoc-account-invoicing",
        "https://github.com/ingadhoc/account-payment ingadhoc-account-payment",
    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-ent:16.0e",
        "postgres postgres:14.1-alpine",
    ],
}
