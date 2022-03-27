# -*- coding: utf-8 -*-
{
    'name': 'KFSYSTMES SARL',
    'version': '1',
    'category': 'Extra',
    'description': """
   Odoo Custom Reports,Reports,odoo reports,Custom Reports,Customize reports,customize your report,
                   Sales Order report,Purchase Order report,Payment 
        """,
    'author': 'KFSYSTEMES',
    "website": "http://",
    'summary': """
    Odoo Custom Reports,Reports,odoo reports,Custom Reports,Customize reports,customize your report,
                   Sales Order report,Purchase Order report,Payment 
        """,
    'depends': [
        'base',
        'account',
        'sale',
        'stock',
        'purchase',
        'amount_to_text_fr',
        'sale_invoice_product_image_app'
    ],
    "data": [
        "reports/layout.xml",
        "data/ir_sequence_data.xml",
        "views/account_payment.xml",
        "views/res_company.xml",
        "views/res_partner.xml",
        "reports/invoice.xml",
        "reports/sale_order.xml",
        "reports/purchase_order.xml",
        "reports/request_for_quotation.xml",
        "reports/rfq_photo.xml",
        "reports/delivery_order.xml",
        "reports/stock_onhand.xml",
        "reports/liste_article_avec_prix.xml",
        "views/report.xml",
    ],
    'license': 'AGPL-3',
    'demo_xml': [],
    'installable': True,
}
