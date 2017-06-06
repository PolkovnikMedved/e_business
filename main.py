# -*- coding: utf-8 -*-
"""

    Python Odoo module

"""
from odoo_connexion import *
from odoo_params import *
import http.server
import socketserver
import json



# tout d'abord on a besoin du uid
uid = get_uid(url, db, username, password)
print("uid = {}".format(uid))

# Ensuite on recupère nos données
access = have_access(url, db, uid, password, table_res_partner, lire)
all_records = ''
if(access):
    identifiants = get_ids(url, db, uid, password, table_res_partner, recherche, True, True)
    all_records = get_records(url, db, uid, password, table_res_partner, lire, identifiants)

# Et enfin on crée un serveur HTTP
class Server(http.server.SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, 'ok')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(all_records).encode("utf-8"))
        #self.wfile.write(" ".join(str(x) for x in all_records).encode("utf-8"))

    def serve_forever(port):
        socketserver.TCPServer(('', port), Server).serve_forever()

if __name__ == "__main__":
    Server.serve_forever(8000)