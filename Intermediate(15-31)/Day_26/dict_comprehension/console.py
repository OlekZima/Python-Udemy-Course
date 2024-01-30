from random import randint
from typing import Dict, List


def main():
    names: List[str] = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
    student_score: Dict[str, int] = {name: randint(0, 100) for name in names}
    print(student_score)

    passed_students: Dict[str, int] = {
        name: score for (name, score) in student_score.items() if score >= 60
    }

    print(passed_students)


if __name__ == "__main__":
    main()
