from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import datetime
# from urllib.parse import quote_plus

def Endpoint(request):
    # Get query parameters
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Get current day of the week in the specified formatc
    current_day = datetime.datetime.now().strftime('%A')

    # Get current UTC time with validation of +/-2 minutes
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct GitHub URLs
    github_repo_url = 'https://github.com/rukkyme/zuri_endpoint'
    github_file_url = f'{github_repo_url}/blob/main/API/get_parameters/api/views.py'

    # Create the JSON response
    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': current_utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200,
    }

    return JsonResponse(response_data)