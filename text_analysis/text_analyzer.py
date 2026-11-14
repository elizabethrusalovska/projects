import re
from pathlib import Path


WORD_PATTERN = re.compile(r"[^\W\d_]+(?:['’ʼ-][^\W\d_]+)*", re.UNICODE)


def get_words(text):
    """Повертає список слів у нижньому регістрі."""
    return [word.casefold() for word in WORD_PATTERN.findall(text)]


def get_word_counts(text):
    """Створює словник: слово — кількість його появ."""
    counts = {}
    for word in get_words(text):
        counts[word] = counts.get(word, 0) + 1
    return counts


def word_frequency_percentages(text):
    """Повертає словник частотності слів у відсотках."""
    counts = get_word_counts(text)
    total = sum(counts.values())

    if total == 0:
        return {}

    return {
        word: round(count / total * 100, 2)
        for word, count in counts.items()
    }


def shortest_words(text):
    """Повертає список найкоротших унікальних слів."""
    words = get_word_counts(text)

    if not words:
        return []

    shortest_length = min(len(word) for word in words)
    return sorted(word for word in words if len(word) == shortest_length)


def longest_words(text):
    """Повертає список найдовших унікальних слів."""
    words = get_word_counts(text)

    if not words:
        return []

    longest_length = max(len(word) for word in words)
    return sorted(word for word in words if len(word) == longest_length)


def unique_word_count(text):
    """Рахує кількість унікальних слів."""
    return len(get_word_counts(text))


def total_word_count(text):
    """Рахує загальну кількість слів."""
    return sum(get_word_counts(text).values())


def get_letter_counts(text):
    """Створює словник: літера — кількість її появ."""
    counts = {}

    for character in text.casefold():
        if character.isalpha():
            counts[character] = counts.get(character, 0) + 1

    return counts


def letters_used(text):
    """Повертає список літер, які є в тексті."""
    return sorted(get_letter_counts(text))


def most_frequent_letters(text):
    """Повертає літеру або літери з найбільшою частотою."""
    counts = get_letter_counts(text)

    if not counts:
        return []

    highest_count = max(counts.values())
    return sorted(
        letter for letter, count in counts.items()
        if count == highest_count
    )


def main():
    text_file = Path(__file__).parent / "input" / "corpus.txt"

    try:
        text = text_file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Не вдалося прочитати файл: {error}")
        return

    percentages = word_frequency_percentages(text)

    print(f"Кількість слів: {total_word_count(text)}")
    print(f"Кількість унікальних слів: {unique_word_count(text)}")
    print(f"Найкоротші слова: {shortest_words(text)}")
    print(f"Найдовші слова: {longest_words(text)}")
    print(f"Використані літери: {letters_used(text)}")
    print(f"Найчастіша літера: {most_frequent_letters(text)}")

    print("\n20 найчастотніших слів у відсотках:")
    for word, percentage in sorted(
        percentages.items(),
        key=lambda item: item[1],
        reverse=True
    )[:20]:
        print(f"{word}: {percentage}%")


if __name__ == "__main__":
    main()