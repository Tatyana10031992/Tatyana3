from django.shortcuts import render, get_object_or_404


LYRICS_BY_LANG = {
    "en": [
        "We are the champions, my friends",
        "And we'll keep on fighting till the end"
    ],
    "fr": [
        "Nous sommes les champions, mes amis",
        "Et nous continuerons à nous battre jusqu'au bout"
    ],
    "de": [
        "Wir sind die Champions, meine Freunde",
        "Und wir werden weiterkämpfen bis zum Ende"
    ],
    "es": [
        "Somos los campeones, mis amigos",
        "Y seguiremos luchando hasta el final"
    ]
}

LANG_INFO = {
    "en": {"artist": "Queen", "title": "We Are The Champions", "name": "English"},
    "fr": {"artist": "Queen", "title": "We Are The Champions", "name": "Français"},
    "de": {"artist": "Queen", "title": "We Are The Champions", "name": "Deutsch"},
    "es": {"artist": "Queen", "title": "We Are The Champions", "name": "Español"},
}

def song_lyrics(request, lang="en"):
    if lang not in LYRICS_BY_LANG:
        return get_object_or_404(Exception) 

    context = {
        "lines": LYRICS_BY_LANG[lang],
        "artist": LANG_INFO[lang]["artist"],
        "title": LANG_INFO[lang]["title"],
        "lang_name": LANG_INFO[lang]["name"],
    }
    return render(request, "lyrics/song.html", context)
