from datetime import datetime

call_schedule: dict[int, str] = {
    1: "08:30 &mdash; 09:50",
    2: "10:00 &mdash; 11:30",
    3: "11:40 &mdash; 13:10",
    4: "13:20 &mdash; 14:50",
    5: "15:00 &mdash; 16:20",
    6: "16:30 &mdash; 17:50",
    7: "18:00 &mdash; 19:20"
}

lunch_schedule: dict[int, str] = {
    1: "12:10 &mdash; 12:30",
    2: "12:10 &mdash; 12:30",
    3: "13:20 &mdash; 13:40",
    4: "15:30 &mdash; 15:50"
}

weekday_names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]


def get_timetable(
        start_lesson_numbers: str, lessons: str
) -> list[tuple[str, list[list[str]]]]:
    """
    Args:
        start_lesson_numbers: 1 3 0
        lessons:
            |-------------------------------|
            | Психология общения. 41        |
            |                               |
            | Физическая культура. Спортзал |
            |                               |
            | 0                             |
            |-------------------------------|
    """

    timetable = []

    start_lesson_numbers = list(map(int, start_lesson_numbers.split()))
    lessons = lessons.replace("\r", "").split("\n\n")

    day = datetime.today().day + 1
    month = datetime.today().month
    for weekday_number, weekday_data in enumerate(lessons):
        lesson_number = start_lesson_numbers[weekday_number]
        if not lesson_number:
            timetable.append((f"{day}.{month} &mdash; {weekday_names[weekday_number]}", []))

            day += 1

            continue

        data = []
        for lesson in weekday_data.split("\n"):
            lesson_name, lesson_room = lesson.split(". ")

            data.append([
                call_schedule[lesson_number], lesson_name, lesson_room
            ])

            lesson_number += 1

        timetable.append((
            (
                f"{day}.{month} &mdash; {weekday_names[weekday_number]} "
                f"({lunch_schedule[start_lesson_numbers[weekday_number]]})"
            ), data
        ))

        day += 1

    return timetable
