from proj_learn_eng.models import Vocabulary
from proj_learn_eng.models import Lessons


def db_get_vocab_stats():
    admin_words = len(Vocabulary.objects.filter(added="admin"))
    user_words = len(Vocabulary.objects.filter(added="user"))
    all_words = Vocabulary.objects.all()
    words_len = [len(word.word) for word in all_words]
    w_meaning_len = [len(word.meaning) for word in all_words]
    admin_lessons = len(Lessons.objects.filter(added="admin"))
    user_lessons = len(Lessons.objects.filter(added="user"))
    all_lessons = Lessons.objects.all()
    les_descrip_len = [len(lesson.description) for lesson in all_lessons]
    stats = {
        "all_words": admin_words + user_words,
        "admin_words": admin_words,
        "user_words": user_words,
        "words_max": max(words_len),
        "w_max_meaning_len": max(w_meaning_len),
        "all_lessons": admin_lessons + user_lessons,
        "admin_lessons": admin_lessons,
        "user_lessons": user_lessons,
        "les_min_descrip_len": min(les_descrip_len)
    }
    return stats
