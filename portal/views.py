"""This module manages the views for the Portal
when request comes in from webserver
it decided which template to render for the user """

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def portal_home(request):
    """handles the traffic for the Portal Main page of visualisation app"""
    return redirect(trends)


@login_required
def trends(request):
    """Routes the user to the Trends visualisation page"""
    return render(request, "portal/visualisations/trends.html", {"title": "Trends"})


@login_required
def top_ten(request):
    """Routes the user to the Top Ten visualisation page"""
    return render(request, "portal/visualisations/top_ten.html", {"title": "Top Ten"})


@login_required
def mapping(request):
    """Routes the user to the Mapping visualisation page"""
    return render(request, "portal/visualisations/mapping.html", {"title": "Mapping"})
