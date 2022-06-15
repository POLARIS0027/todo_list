from django.shortcuts import render
from django.views.generic import FormView
from cal.forms import BookingForm
from google.oauth2 import service_account
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from googleapiclient.discovery import build

# Create your views here.


    
#setting for google API
    
SCOPES =["https://www.googleapis.com/auth/calendar"]

service_account_email = "golfcal-service-account@inspiring-grove-353415.iam.gserviceaccount.com"    
credentials = service_account.Credentials.from_service_account_file('credential.json')
scoped_credentials = credentials.with_scopes(SCOPES)
calendarId = "bl62dktmt3l69hjmt25feev9ks@group.calendar.google.com"
    
#working part

def build_service(request):
    service = build("calendar", "v3", credentials=scoped_credentials)
    return service

class HomeView(FormView):
    form_class = BookingForm
    template_name = 'cal/home.html'
    
    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        eventTitle = form.cleaned_data.get("eventTitle")
        start_date_data = form.cleaned_data.get("startDateTime")
        end_date_data = form.cleaned_data.get("endDateTime")
        discription = form.cleaned_data.get('description')
        
        if start_date_data > end_date_data:
            messages.add_message(self.request, messages.INFO, '시작일이 종료일보다 늦을순 없음')
            return HttpResponseRedirect(reverse("cal:home"))
        
        service = build_service(self.request)
        
        event = (
            service.events().insert(
            calendarId=calendarId,
            body={
                "summary": eventTitle,
                "start": {"dateTime": start_date_data.isoformat()},
                "end": {"dateTime": end_date_data.isoformat()},
                "discription": discription,
            },
        ).execute()
        )
        
        return super().form_valid(form)
    
    def get_success_url(self):
        
        messages.add_message(self.request, messages.INFO, '예약 제출 완료!!')
        
        return reverse('cal:home')