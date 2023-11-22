from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),

    path('xml/', show_xml, name='show_xml'),
    path('html/', show_html, name='show_html'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),

    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('delete/<int:id>', delete_item, name='delete_item'),
    
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('delete_item_ajax/', delete_item_ajax, name='delete_item_ajax'),
    path('edit_item_ajax/', edit_item_ajax, name='edit_item_ajax'),

    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]