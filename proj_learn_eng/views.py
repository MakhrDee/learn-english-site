from django.shortcuts import render
from django.core.cache import cache
from . import vocab_work
from . import vocab_work_db
import random


def index(request):
    return render(request, "index.html")


def vocabulary(request):
    words = vocab_work_db.db_get_words_for_table()
    return render(request, "vocab.html", context={"words": words})


def lessons_list(request):
    lessons = vocab_work_db.db_get_lessons_for_table()
    return render(request, "lessons_list.html", context={"lessons": lessons})


def terms_list_new(request, slug):
    terms = vocab_work.get_terms_for_table()
    if slug == 'random':
        random_term = list()
        random_term.append(random.choice(terms))
        return render(request, "vocab.html", context={"terms": random_term, "slug": slug})
    else:
        return render(request, "vocab.html", context={"terms": terms})


def add_word(request):
    return render(request, "word_add.html")


def send_word(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            vocab_work.write_word(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_word(request)


def show_stats(request):
    stats = vocab_work.get_terms_stats()
    return render(request, "stats.html", stats)


def add_lesson(request):
    return render(request, "lesson_add.html")
