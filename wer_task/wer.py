import json
import re
from pathlib import Path


WORD_PATTERN = re.compile(
    r"[^\W\d_]+(?:['’ʼ-][^\W\d_]+)*",
    re.UNICODE
)


def tokenize(text):
    """Поділяє текст на слова, зводячи їх до нижнього регістру."""
    return [word.casefold() for word in WORD_PATTERN.findall(text)]


def calculate_wer(reference_text, hypothesis_text):
    """Обчислює WER і кількість замін, видалень та вставок."""
    reference = tokenize(reference_text)
    hypothesis = tokenize(hypothesis_text)

    number_of_reference_words = len(reference)

    if number_of_reference_words == 0:
        raise ValueError("Текст-еталон має містити щонайменше одне слово.")

    rows = len(reference) + 1
    columns = len(hypothesis) + 1
    distance = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        distance[i][0] = i

    for j in range(columns):
        distance[0][j] = j

    for i in range(1, rows):
        for j in range(1, columns):
            if reference[i - 1] == hypothesis[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            distance[i][j] = min(
                distance[i - 1][j] + 1,
                distance[i][j - 1] + 1,
                distance[i - 1][j - 1] + substitution_cost
            )

    substitutions = 0
    deletions = 0
    insertions = 0
    i = len(reference)
    j = len(hypothesis)

    while i > 0 or j > 0:
        if (
            i > 0
            and j > 0
            and reference[i - 1] == hypothesis[j - 1]
            and distance[i][j] == distance[i - 1][j - 1]
        ):
            i -= 1
            j -= 1
        elif (
            i > 0
            and j > 0
            and distance[i][j] == distance[i - 1][j - 1] + 1
        ):
            substitutions += 1
            i -= 1
            j -= 1
        elif i > 0 and distance[i][j] == distance[i - 1][j] + 1:
            deletions += 1
            i -= 1
        else:
            insertions += 1
            j -= 1

    wer = (
        substitutions + deletions + insertions
    ) / number_of_reference_words

    return {
        "WER": wer,
        "S": substitutions,
        "D": deletions,
        "I": insertions,
        "N": number_of_reference_words
    }


def main():
    project_folder = Path(__file__).parent
    reference_path = project_folder / "texts" / "reference.txt"
    hypothesis_path = project_folder / "texts" / "hypothesis.txt"
    output_path = project_folder / "wer_results.json"

    try:
        reference_text = reference_path.read_text(encoding="utf-8")
        hypothesis_text = hypothesis_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Не вдалося прочитати текстовий файл: {error}")
        return

    try:
        metrics = calculate_wer(reference_text, hypothesis_text)
    except ValueError as error:
        print(f"Помилка обчислення WER: {error}")
        return

    output_path.write_text(
        json.dumps(metrics, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )

    print(f"Еталонний файл: {reference_path.name}")
    print(f"Файл для порівняння: {hypothesis_path.name}")
    print(f"WER: {metrics['WER']:.4f} ({metrics['WER'] * 100:.2f}%)")
    print(f"S — заміни: {metrics['S']}")
    print(f"D — видалення: {metrics['D']}")
    print(f"I — вставки: {metrics['I']}")
    print(f"N — слів в еталоні: {metrics['N']}")
    print(f"Результати збережено у {output_path.name}")


if __name__ == "__main__":
    main()