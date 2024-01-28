from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name="home"),
   path('facilities', views.facilities, name='facilities'),
   path('body', views.body, name='body'),
   path('faq',views.faq,name="faq"),
   path('vision',views.vision,name="vision"),
   path('objectives',views.objectives,name="objectives"),
   path('contacts',views.contacts,name="contacts"),
   path('boardofdirectors',views.boardofdirectors,name="boardofdirectors"),
   path('team',views.team,name="team"),
   path('collabrations',views.collabrations,name="collabrations"),
   path('collabrations/<str:tab>/', views.collabrations, name='collabrations_tab'),
   path('startups',views.startups,name="startups"),
   path('mentors',views.mentors,name="mentors"),
   path('makerslab',views.makerslab,name="makerslab"),
   path('sectorspecificlab',views.sectorspecificlab,name="sectorspecificlab"),
   path('communityinnovativespace',views.communityinnovativespace,name="communityinnovativespace"),
   path('events',views.events,name="events"),
   path('events/<str:name>/', views.eventnames, name="eventnames"),
   path('events/<str:name>/<str:dname>/', views.eventdetails, name="eventdetails"),
]