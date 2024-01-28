from django.shortcuts import render, redirect
from . models import *
import re
from django.contrib import messages
from datetime import datetime
from itertools import chain
from django.http import HttpResponse



# Create your views here.
def home(request):
    labcount1 = MakersLab.objects.all().count()
    labcount2 = SectorSpecificLab.objects.all().count()
    labcount3 = CommunityInnovativeSpace.objects.all().count()
    totallabcount = labcount1 + labcount2 + labcount3
    eventcount = EventNames.objects.all().count()
    mentorcount = Mentors.objects.all().count()
    startupcount = StartUps.objects.all().count()
    collabrationcount = Collabrations.objects.all().count()
    teamcount = Team.objects.all().count()
    directorscount = BoardOfDirectors.objects.all().count()
    return render(request,"acicmain/index.html", {"totallabcount": totallabcount,
                                                  "eventcount": eventcount,
                                                  "mentorcount": mentorcount,
                                                  "startupcount": startupcount,
                                                  "collabrationcount": collabrationcount,
                                                  "teamcount": teamcount,
                                                  "directorscount": directorscount})

def facilities(request):
    labname = MakersLab.objects.all()
    labname2 = SectorSpecificLab.objects.all()
    labname3 = CommunityInnovativeSpace.objects.all()

    return render(request, "acicmain/pages/facilities.html", {
        "labname": labname,
        "labname2": labname2,
        "labname3": labname3
    })

def body(request):
    return render(request, "acicmain/inc/body.html") 

def faq(request):
    collaborations = None
    search_date = None
    
    if request.method == 'POST':
        search_date = request.POST.get('search_date')  # Get the search date from the form
        parsed_date = datetime.strptime(search_date, '%Y-%m-%d').date()
        collaborations = Collabrations.objects.filter(created_at__date=parsed_date)  # Retrieve collaborations with the specified date
    
    else:
        collaborations = Collabrations.objects.all()  # If no search is performed, retrieve all collaborations
        
    return render(request, "acicmain/pages/faq.html", {'collaborations': collaborations, "search_date": search_date})


def vision(request):
    # Assuming you want to retrieve the first object from the VisObjCon model
    vision_object = VisObjCon.objects.first()
    vision_paragraph = vision_object.vision if vision_object else ""
    bullet_points = vision_paragraph.split('\n')  # Split the paragraph into bullet points
    return render(request, "acicmain/pages/vision.html", {"bullet_points": bullet_points})

def objectives(request):
    # Assuming you want to retrieve the first object from the VisObjCon model
    vision_object = VisObjCon.objects.first()
    vision_paragraph = vision_object.objectives if vision_object else ""
    bullet_points = vision_paragraph.split('\n')  # Split the paragraph into bullet points
    return render(request, "acicmain/pages/objectives.html", {"bullet_points": bullet_points})

def contacts(request):
    # Assuming you want to retrieve the first object from the VisObjCon model
    vision_object = VisObjCon.objects.first()
    vision_paragraph = vision_object.contacts if vision_object else ""
    bullet_points = vision_paragraph.split('\n')  # Split the paragraph on newline character
    return render(request, "acicmain/pages/contacts.html", {"bullet_points": bullet_points})

def boardofdirectors(request):
    bod = BoardOfDirectors.objects.all()
    return render(request,"acicmain/pages/boardofdirectors.html",{"bod": bod})

def team(request):
    head_team = Team.objects.filter(head=True)
    other_team = Team.objects.filter(head=False)
    return render(request, "acicmain/pages/team.html",{"head_team": head_team,"other_team": other_team})

def collabrations(request, tab=None):
    if tab == 'government':
        active_tab = 'government'
        collabrations = Collabrations.objects.first()
        collabrations_paragraph = collabrations.government if collabrations else ""
        collabrations_tab = collabrations_paragraph.split('\n')  # Split the paragraph on newline character
    elif tab == 'corporate':
        active_tab = 'corporate'
        collabrations = Collabrations.objects.first()
        collabrations_paragraph = collabrations.corporate if collabrations else ""
        collabrations_tab = collabrations_paragraph.split('\n')  # Split the paragraph on newline character
    elif tab == 'academic':
        active_tab = 'academic'
        collabrations = Collabrations.objects.first()
        collabrations_paragraph = collabrations.academic if collabrations else ""
        collabrations_tab = collabrations_paragraph.split('\n')  # Split the paragraph on newline character
    else:
        active_tab = 'government'  # Default to government tab
        collabrations = Collabrations.objects.first()
        collabrations_paragraph = collabrations.government if collabrations else ""
        collabrations_tab = collabrations_paragraph.split('\n')  # Split the paragraph on newline character

    return render(request, "acicmain/pages/collabrations.html", {'active_tab': active_tab, 'collabrations_tab': collabrations_tab})

def startups(request):
    startupname = StartUps.objects.all()
    return render(request,"acicmain/pages/startups.html",{"startupname": startupname})

def mentors(request):
    inter_mentor = Mentors.objects.filter(international=True)
    mentor = Mentors.objects.filter(international=False)
    return render(request,"acicmain/pages/mentors.html",{"inter_mentor": inter_mentor,"mentor": mentor})

def makerslab(request):
    labname = MakersLab.objects.all()
    return render(request,"acicmain/pages/makerslab.html",{"labname": labname})

def sectorspecificlab(request):
    labname2 = SectorSpecificLab.objects.all()
    return render(request,"acicmain/pages/sectorspecificlab.html",{"labname2": labname2})

def communityinnovativespace(request):
    labname3 = CommunityInnovativeSpace.objects.all()
    return render(request,"acicmain/pages/communityinnovativespace.html",{"labname3": labname3})

def events(request):
    eventname = Events.objects.all()
    return render(request,"acicmain/pages/events.html",{"eventname": eventname})

def eventnames(request,name):
    if(Events.objects.filter(name=name)):
        eventnames = EventNames.objects.filter(event__name=name)
        return render(request,"acicmain/pages/eventnames.html",{"eventnames": eventnames,"prev_event": name})
    else:
        messages.warning(request,"No Event Found")
        return redirect('events')


def eventdetails(request, name, dname):
    try:
       
        event = Events.objects.get(name=name)
        event_name = EventNames.objects.get(name=dname, event=event)
        event_details = EventDetails.objects.filter(event=event_name.event)
        return render(request, "acicmain/pages/eventdetails.html", {"event_name": event_name,"event_details": event_details})
    except Events.DoesNotExist:
        messages.error(request, "No Events found")
        return redirect('events')
    except EventNames.DoesNotExist:
        messages.error(request, "No event is found")
        return redirect('events')
    except EventDetails.DoesNotExist:
        messages.error(request, "No event is found")
        return redirect('events')
        

    