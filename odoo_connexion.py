# -*- coding: utf-8 -*-
'''
    Ici, vous avez des fonctions simples à utiliser pour recupérer des résultats
'''
import xmlrpc.client

def get_uid(url, db, username, password):
    """
        Cette fonction vous donne votre identifiant Odoo

        :param: url         (String)
        :param: db          (String)
        :param: username    (String email)
        :param: password    (String)
        :rtype: Integer

    """
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    return common.authenticate(db, username, password, {})


def have_access(url, db, uid, pw, table, mode):
    """
        Cette fonction vous dis si vous avez l'accès à une table

        :param: url         (String)
        :param: db          (String)
        :param: uid         (Int)
        :param: pw          (String password)
        :param: table       (String)
        :param: mode        (String)
        :rtype: Boolean

    """
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    return models.execute_kw(db, uid, pw, table, 'check_access_rights', [mode], {'raise_exception': False})


def get_ids(url, db, uid, pw, table, mode, is_company, is_customer):
    """
        Cette fonction vous donne les identifiants de vos records
        de la table choisie

        :param: url         (String)
        :param: db          (String)
        :param: uid         (int)
        :param: pw          (String password)
        :param: table       (String)
        :param: mode        (String)
        :param: is_company  (Boolean)
        :param: is_customer (Boolean)
        :rtype: ???
    """
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    return models.execute_kw(db, uid, pw, table, mode, [[['is_company', '=', is_company], ['customer', '=', is_customer]]])


def get_records(url, db, uid, pw, table, mode, ids):
    """
        Cette fonction vous donne les records de la table choisie
        en fonction des ids que vous lui envoyez

        :param: url         (String)
        :param: db          (String)
        :param: uid         (int)
        :param: pw          (String password)
        :param: table       (String)
        :param: mode        (String)
        :param: ids         (?? Tuple ??)
        :rtype: ???

    """
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    return models.execute_kw(db, uid, pw, table, mode, [ids], {'fields':['id', 'customer', 'create_date', 'website', 'country_id', 'lang', 'name', 'create_uid', 'email', 'street', 'zip', 'city']})
