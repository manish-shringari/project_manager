"""Djangomon url"""
import views

from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^dashboard/$',
    	views.DashboardView.as_view(), name='dashboard'),
    url(r'^user_dashboard/$',
    	views.UserDashboardView.as_view(), name='user_dashboard'),
    url(r'^create/$',
        TicketCreateView.as_view(), name='create'),
    url(r'^add_milestone/$',
        MilestoneCreateView.as_view(), name='add_milestone'),
    url(r'^delete/$',
        delete_ticket, name='delete'),
    url(r'^user_ticket_list/$',
    	TicketListUserView.as_view(), name='user_ticket_list'),
    url(r'^ticket_list/$',
    	views.TicketListView.as_view(), name='ticket_list'),
    url(r'^update_template/(?P<ticket_id>[^/]+)/$',
        TicketUpdateTemplateView.as_view(), name='update_template'),
    url(r'^update/(?P<ticket_id>[^/]+)/$',
        TicketUpdateView.as_view(), name='update'),
    url(r'^user_detail/(?P<ticket_id>[^/]+)/$',
        TicketDetailUserView.as_view(), name='user_details'),
    url(r'^(?P<ticket_id>[^/]+)/$',
        TicketDetailView.as_view(), name='details')

]
