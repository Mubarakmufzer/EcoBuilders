"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_customer_details_view', views.admin_customer_details_view, name='admin_customer_details_view'),
    path('admin_customer_details_delete', views.admin_customer_details_delete, name='admin_customer_details_delete'),

    path('admin_category_details_view', views.admin_category_details_view, name='admin_category_details_view'),
    path('admin_category_details_delete', views.admin_category_details_delete, name='admin_category_details_delete'),
    path('admin_category_details_edit', views.admin_category_details_edit, name='admin_category_details_edit'),
    path('admin_category_details_add', views.admin_category_details_add, name='admin_category_details_add'),

    path('admin_designation_master_view', views.admin_designation_master_view, name='admin_designation_master_view'),
    path('admin_designation_master_delete', views.admin_designation_master_delete, name='admin_designation_master_delete'),
    path('admin_designation_master_edit', views.admin_designation_master_edit, name='admin_designation_master_edit'),
    path('admin_designation_master_add', views.admin_designation_master_add, name='admin_designation_master_add'),

    path('admin_staff_details_view', views.admin_staff_details_view, name='admin_staff_details_view'),
    path('admin_staff_details_add', views.admin_staff_details_add, name='admin_staff_details_add'),
    path('admin_staff_details_delete', views.admin_staff_details_delete, name='admin_staff_details_delete'),

    path('admin_staff_quotation_view', views.admin_staff_quotation_view, name='admin_staff_quotation_view'),
    path('admin_staff_quotation_reply_view', views.admin_staff_quotation_reply_view, name='admin_staff_quotation_reply_view'),

    path('staff_login', views.staff_login, name='staff_login'),
    path('staff_home', views.staff_home, name='staff_home'),
    path('staff_logout', views.staff_logout, name='staff_logout'),
    path('staff_changepassword', views.staff_changepassword, name='staff_changepassword'),

    path('staff_quotation_view', views.staff_quotation_view, name='staff_quotation_view'),
    path('staff_quotation_pending_view', views.staff_quotation_pending_view, name='staff_quotation_pending_view'),
    path('staff_quotation_reject_view', views.staff_quotation_reject_view, name='staff_quotation_reject_view'),
    path('staff_quotation_update', views.staff_quotation_update, name='staff_quotation_update'),

    path('staff_quotation_reply_view', views.staff_quotation_reply_view, name='staff_quotation_reply_view'),
    path('staff_quotation_reply_delete', views.staff_quotation_reply_delete, name='staff_quotation_reply_delete'),
    path('staff_quotation_reply_add', views.staff_quotation_reply_add, name='staff_quotation_reply_add'),

    path('staff_quotation_details_view', views.staff_quotation_details_view, name='staff_quotation_details_view'),
    path('staff_quotation_details_delete', views.staff_quotation_details_delete, name='staff_quotation_details_delete'),
    path('staff_quotation_details_add', views.staff_quotation_details_add, name='staff_quotation_details_add'),

    path('staff_customer_details_view', views.staff_customer_details_view, name='staff_customer_details_view'),
    path('staff_staff_details_view', views.staff_staff_details_view, name='staff_staff_details_view'),

    path('staff_edit_profile', views.staff_edit_profile, name='staff_edit_profile'),
    path('staff_profile_view', views.staff_profile_view, name='staff_profile_view'),

    path('staff_message_add', views.staff_message_add, name='staff_message_add'),
    path('staff_inbox_view', views.staff_inbox_view, name='staff_inbox_view'),
    path('staff_outbox_view', views.staff_outbox_view, name='staff_outbox_view'),
    path('staff_quotation_delete', views.staff_quotation_delete, name='staff_quotation_delete'),


    path('customer_home', views.customer_home, name='customer_home'),
    path('customer_login', views.customer_login, name='customer_login'),
    path('customer_logout', views.customer_logout, name='customer_logout'),
    path('customer_details_add', views.customer_details_add, name='customer_details_add'),
    path('customer_details_update', views.customer_details_update, name='customer_details_update'),
    path('customer_profile_view', views.customer_profile_view, name='customer_profile_view'),
    path('customer_changepassword', views.customer_changepassword, name='customer_changepassword'),

    path('customer_message_add', views.customer_message_add, name='customer_message_add'),
    path('customer_inbox_view', views.customer_inbox_view, name='customer_inbox_view'),
    path('customer_outbox_view', views.customer_outbox_view, name='customer_outbox_view'),

    path('customer_quotation_view', views.customer_quotation_view, name='customer_quotation_view'),
    path('customer_quotation_add', views.customer_quotation_add, name='customer_quotation_add'),
    path('customer_quotation_delete', views.customer_quotation_delete, name='customer_quotation_delete'),

    path('customer_quotation_reply_view', views.customer_quotation_reply_view, name='customer_quotation_reply_view'),
    path('customer_quotation_details_view', views.customer_quotation_details_view, name='customer_quotation_details_view'),

    path('contact_us_view', views.contact_us_view, name='contact_us_view'),
    path('admin_contact_view', views.admin_contact_view, name='admin_contact_view'),
    path('admin_contact_view_delete', views.admin_contact_view_delete, name='admin_contact_view_delete'),




]
