from proj_learn_eng.models import Lessons, Vocabulary


def db_get_words_for_table():
    words = []
    for i, item in enumerate(Vocabulary.objects.all()):
        words.append([i+1, item.word, item.translate, item.meaning])
    return words


def db_get_lessons_for_table():
    lessons = []
    for i, item in enumerate(Lessons.objects.all()):
        lessons.append([i+1, item.topic, item.description])
    return lessons


'''def db_write_term(new_term, new_definition):
term = Terms(term=new_term, definition=new_definition)
term_addition = TermAuthors(termid=term.termid, termsource=”user”)
term.save()
term_addition.save()
def db_get_terms_stats():
db_terms = len(TermAuthors.objects.filter(termsource=”db”))
user_terms = len(TermAuthors.objects.filter(termsource=”user”))
terms = Terms.objects.all()
defin_len = [len(term.definition) for term in terms]
stats = {
“terms_all”: db_terms + user_terms,
“terms_own”: db_terms,
“terms_added”: user_terms,
“words_avg”: sum(defin_len)/len(defin_len),
“words_max”: max(defin_len),
“words_min”: min(defin_len)
} return stats'''
