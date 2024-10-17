import requests 
from django.shortcuts import render, redirect
from django.conf import settings
from spotipy import SpotifyOAuth 

# Create your views here.

def your_view_function(request): 
    sp_oauth = SpotifyOAuth(
        client_id = settings.SPOTIFY_CLIENT_ID, 
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope="user-library-read playlist-modify-private"
    )
    # 인증 URL 생성 
    auth_url = sp_oauth.get_authorize_url() 
    # 인증 페이지로 redirection 
    return redirect(auth_url)


def search_song(request): 
    # 세션에서 엑세스 토큰 가져오기 
    token_info = request.session.get('token_info')
    access_token = token_info['access_token'] if token_info else None 

    if access_token is None: 
        return redirect('accounts:login') # 로그인 페이지로 리다이렉션 
 
    query = request.GET.get('q')
    url = 'https://api.spotify.com/v1/search'
    headers = { 
        'Authorization' : f'Bearer {access_token}'
    }
    params = {
        'q' : query, 
        'type' : 'track', 
        'limit' : 10 
    }
    response = requests.get(url, headers=headers , params=params)
    results = response.json() 
    context = {
        'results' : results
    }
    return render(request, 'spotify/search_results.html', context)

