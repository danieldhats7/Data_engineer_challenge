from cfg import URL
from so_questions import Stackoverflow_questions
import click


def actividad_2(questions):
    answered_count, unanswered_count = questions.answered_count()
    print(f"Respuestas contestadas: {answered_count}")
    print(f"Respuestas no contestadas: {unanswered_count} \n")


def actividad_3(questions):
    q_views_min = questions.question_views_min()
    print(f"Pregunta con menor numero de vistas: {q_views_min} \n")


def actividad_4(questions):
    old, current = questions.question_old_current()
    print(f"Pregunta mas vieja: {old}")
    print("=" * 50)
    print(f"Pregunta mas actual: {current} \n")


def actividad_5(questions):
    q_owner_highest_reputation = questions.question_owner_highest_reputation()
    print(f"Pregunta del owner con mayor reputacion: {q_owner_highest_reputation} \n")


def actividad_6(questions):
    actividad_2(questions)
    actividad_3(questions)
    actividad_4(questions)
    actividad_5(questions)


@click.command()
@click.option(
    "--activity",
    default="6",
    type=click.Choice(["2", "3", "4", "5", "6"]),
    help="Activity to run",
)
def run(activity):
    actividades = {
        "2": actividad_2,
        "3": actividad_3,
        "4": actividad_4,
        "5": actividad_5,
        "6": actividad_6,
    }
    questions = Stackoverflow_questions(URL)
    actividades[activity](questions)


if __name__ == "__main__":
    run()
