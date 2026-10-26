import math

WORDS = ["НЕ", "ХВАЛИ", "ДЕНЬ", "ДО", "ВЕЧОРА", "А", "ХЛІБ", "ДО", "ВЕЧЕРІ"]

ALPHABET = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19,
    'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}

M_DIV = 13
M_MULT = 16
A_CONST = (math.sqrt(5) - 1) / 2  # Knuth's constant ≈ 0.6180339


def get_k(word):
    """Calculates the numeric key K as the sum of letter positions."""
    return sum(ALPHABET.get(char, 0) for char in word)


def hash_div(k, m=M_DIV):
    """Division method: h(k) = k mod m"""
    return k % m


def hash_mult(k, m=M_MULT):
    """Multiplication method: h(k) = floor(m * (k * A mod 1))"""
    return int(m * ((k * A_CONST) % 1))


def build_open_hash_table(words, method='div'):
    """Builds an open hash table using separate chaining."""
    m = M_DIV if method == 'div' else M_MULT
    hash_func = hash_div if method == 'div' else hash_mult

    hash_table = [[] for _ in range(m)]

    # Insert words into the corresponding chain
    for word in words:
        k = get_k(word)
        idx = hash_func(k, m)
        hash_table[idx].append(word)

    return hash_table


def build_closed_hash_table(words, method='div'):
    """Builds a closed hash table using open addressing."""
    m = M_DIV if method == 'div' else M_MULT
    hash_func = hash_div if method == 'div' else hash_mult

    hash_table = [None] * m

    for word in words:
        k = get_k(word)
        start_idx = hash_func(k, m)

        # Linear probing to resolve collisions
        for i in range(m):
            idx = (start_idx + i) % m
            if hash_table[idx] is None:
                hash_table[idx] = word
                break
        else:
            print(f"Error: Hash table is full. Cannot insert '{word}'.")

    return hash_table


def display_open_table(table, method_name):
    print(f"\n--- Open Hash Table (Chaining), Method: {method_name}, M={len(table)} ---")
    for i, chain in enumerate(table):
        print(f"Index {i:02d}: {chain}")


def display_closed_table(table, method_name):
    print(f"\n--- Closed Hash Table (Open Addressing), Method: {method_name}, M={len(table)} ---")
    print("Index | Word")
    print("------|------")
    for i, item in enumerate(table):
        val = item if item is not None else "(NULL)"
        print(f"{i:02d}    | {val}")


if __name__ == "__main__":
    print("Words and their numeric keys (K):")
    for w in WORDS:
        print(f"{w}: {get_k(w)}")

    # Task 1: Open Hashing
    open_div = build_open_hash_table(WORDS, 'div')
    display_open_table(open_div, 'Division')

    open_mult = build_open_hash_table(WORDS, 'mult')
    display_open_table(open_mult, 'Multiplication')

    # Task 2: Closed Hashing
    closed_div = build_closed_hash_table(WORDS, 'div')
    display_closed_table(closed_div, 'Division')

    closed_mult = build_closed_hash_table(WORDS, 'mult')
    display_closed_table(closed_mult, 'Multiplication')