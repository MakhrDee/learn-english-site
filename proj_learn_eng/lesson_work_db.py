from proj_learn_eng.models import Lessons


def db_get_lessons_for_table():
    lessons = []
    for i, item in enumerate(Lessons.objects.all()):
        lessons.append([i+1, item.topic, item.description])
    return lessons


def db_write_lesson(new_topic, new_description):
    lesson = Lessons(topic=new_topic, description=new_description)
    lesson.save()