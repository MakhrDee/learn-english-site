from proj_learn_eng.models import Vocabulary


def db_get_words_for_table():
    words = []
    for i, item in enumerate(Vocabulary.objects.all()):
        words.append([i+1, item.word, item.translate, item.meaning])
    return words


def db_write_word(new_word, new_translate, new_meaning):
    word = Vocabulary(word=new_word, translate=new_translate, meaning=new_meaning)
    word.save()


def db_delete_word(delete_word):
    #TODO: обработать ошибку при введении несуществующего слова
    del_word = Vocabulary.objects.filter(word=delete_word)
    del_word.delete()


