from django.shortcuts import render
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def get_session_with_retries():
    session = requests.Session()
    retry = Retry(
        total=5,
        read=5,
        connect=5,
        backoff_factor=0.3,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def starwars_home(request):
    return render(request, 'starwars_app/starwars_home.html')

def films_list(request):
    try:
        session = get_session_with_retries()
        response = session.get('https://swapi.dev/api/films/', timeout=10)
        response.raise_for_status()
        films_data = response.json()
        return render(request, 'starwars_app/films_list.html', {'films': films_data.get('results', [])})
    except requests.exceptions.ConnectionError:
        return render(request, 'starwars_app/error.html', {
            'error': 'Не удалось подключиться к серверу SWAPI. Проверьте интернет-соединение.'
        })
    except requests.exceptions.Timeout:
        return render(request, 'starwars_app/error.html', {
            'error': 'Превышено время ожидания ответа от сервера SWAPI.'
        })
    except requests.exceptions.RequestException as e:
        return render(request, 'starwars_app/error.html', {'error': f'Ошибка: {str(e)}'})

def film_detail(request, film_id):
    try:
        session = get_session_with_retries()
        response = session.get(f'https://swapi.dev/api/films/{film_id}/', timeout=10)
        response.raise_for_status()
        film = response.json()
        return render(request, 'starwars_app/film_detail.html', {'film': film})
    except requests.exceptions.ConnectionError:
        return render(request, 'starwars_app/error.html', {
            'error': 'Не удалось подключиться к серверу SWAPI. Проверьте интернет-соединение.'
        })
    except requests.exceptions.Timeout:
        return render(request, 'starwars_app/error.html', {
            'error': 'Превышено время ожидания ответа от сервера SWAPI.'
        })
    except requests.exceptions.RequestException as e:
        return render(request, 'starwars_app/error.html', {'error': f'Ошибка: {str(e)}'})

def people_list(request):
    try:
        session = get_session_with_retries()
        response = session.get('https://swapi.dev/api/people/', timeout=10)
        response.raise_for_status()
        people_data = response.json()
        return render(request, 'starwars_app/people_list.html', {'people': people_data.get('results', [])})
    except requests.exceptions.ConnectionError:
        return render(request, 'starwars_app/error.html', {
            'error': 'Не удалось подключиться к серверу SWAPI. Проверьте интернет-соединение.'
        })
    except requests.exceptions.Timeout:
        return render(request, 'starwars_app/error.html', {
            'error': 'Превышено время ожидания ответа от сервера SWAPI.'
        })
    except requests.exceptions.RequestException as e:
        return render(request, 'starwars_app/error.html', {'error': f'Ошибка: {str(e)}'})

def person_detail(request, person_id):
    try:
        session = get_session_with_retries()
        response = session.get(f'https://swapi.dev/api/people/{person_id}/', timeout=10)
        response.raise_for_status()
        person = response.json()
        return render(request, 'starwars_app/person_detail.html', {'person': person})
    except requests.exceptions.ConnectionError:
        return render(request, 'starwars_app/error.html', {
            'error': 'Не удалось подключиться к серверу SWAPI. Проверьте интернет-соединение.'
        })
    except requests.exceptions.Timeout:
        return render(request, 'starwars_app/error.html', {
            'error': 'Превышено время ожидания ответа от сервера SWAPI.'
        })
    except requests.exceptions.RequestException as e:
        return render(request, 'starwars_app/error.html', {'error': f'Ошибка: {str(e)}'})

def planets_list(request):
    try:
        session = get_session_with_retries()
        response = session.get('https://swapi.dev/api/planets/', timeout=10)
        response.raise_for_status()
        planets_data = response.json()
        return render(request, 'starwars_app/planets_list.html', {'planets': planets_data.get('results', [])})
    except requests.exceptions.ConnectionError:
        return render(request, 'starwars_app/error.html', {
            'error': 'Не удалось подключиться к серверу SWAPI. Проверьте интернет-соединение.'
        })
    except requests.exceptions.Timeout:
        return render(request, 'starwars_app/error.html', {
            'error': 'Превышено время ожидания ответа от сервера SWAPI.'
        })
    except requests.exceptions.RequestException as e:
        return render(request, 'starwars_app/error.html', {'error': f'Ошибка: {str(e)}'})

def planet_detail(request, planet_id):
    try:
        session = get_session_with_retries()
        response = session.get(f'https://swapi.dev/api/planets/{planet_id}/', timeout=10)
        response.raise_for_status()
        planet = response.json()
        return render(request, 'starwars_app/planet_detail.html', {'planet': planet})
    except requests.exceptions.ConnectionError:
        return render(request, 'starwars_app/error.html', {
            'error': 'Не удалось подключиться к серверу SWAPI. Проверьте интернет-соединение.'
        })
    except requests.exceptions.Timeout:
        return render(request, 'starwars_app/error.html', {
            'error': 'Превышено время ожидания ответа от сервера SWAPI.'
        })
    except requests.exceptions.RequestException as e:
        return render(request, 'starwars_app/error.html', {'error': f'Ошибка: {str(e)}'})

def starships_list(request):
    try:
        session = get_session_with_retries()
        response = session.get('https://swapi.dev/api/starships/', timeout=10)
        response.raise_for_status()
        starships_data = response.json()
        return render(request, 'starwars_app/starships_list.html', {'starships': starships_data.get('results', [])})
    except requests.exceptions.ConnectionError:
        return render(request, 'starwars_app/error.html', {
            'error': 'Не удалось подключиться к серверу SWAPI. Проверьте интернет-соединение.'
        })
    except requests.exceptions.Timeout:
        return render(request, 'starwars_app/error.html', {
            'error': 'Превышено время ожидания ответа от сервера SWAPI.'
        })
    except requests.exceptions.RequestException as e:
        return render(request, 'starwars_app/error.html', {'error': f'Ошибка: {str(e)}'})

def starship_detail(request, starship_id):
    try:
        session = get_session_with_retries()
        response = session.get(f'https://swapi.dev/api/starships/{starship_id}/', timeout=10)
        response.raise_for_status()
        starship = response.json()
        return render(request, 'starwars_app/starships_detail.html', {'starship': starship})
    except requests.exceptions.ConnectionError:
        return render(request, 'starwars_app/error.html', {
            'error': 'Не удалось подключиться к серверу SWAPI. Проверьте интернет-соединение.'
        })
    except requests.exceptions.Timeout:
        return render(request, 'starwars_app/error.html', {
            'error': 'Превышено время ожидания ответа от сервера SWAPI.'
        })
    except requests.exceptions.RequestException as e:
        return render(request, 'starwars_app/error.html', {'error': f'Ошибка: {str(e)}'})