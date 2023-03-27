"""
[kmp - Knuth-Morris-Pratt Algorithm: Python implementation]
"""
from typing import List, AnyStr

def kmp_table(pattern:AnyStr)->List[int]:
    """[Generate the KMP table for pattern matching]

    Args:
        pattern (List[String]): Pattern used to find the KMP Table

    Returns:
        List[int]: The KMP Table generated
    """
    size = len(pattern)
    table = [0] * (size+1)

    position = 1
    candidate = 0

    table[0] = -1

    while position < size:
        if pattern[position] == pattern[candidate]:
            table[position] = table[candidate]
        else:
            table[position] = candidate
            while candidate >= 0 and pattern[position] != pattern[candidate]:
                candidate = table[candidate]
        position += 1
        candidate += 1
    table[position] = candidate

    return table

def kmp_search(text: AnyStr, pattern: AnyStr) -> List[int]:
    """[summary]

    Args:
        search (AnyStr): [description]
        pattern (AnyStr): [description]

    Returns:
        Tuple[List[int], int]: [description]
    """
    position_in_text, position_in_pattern = 0, 0
    table = kmp_table(pattern)

    size_text = len(text)
    size_pattern = len(pattern)
    positions = []

    while position_in_text < size_text:
        if pattern[position_in_pattern] == text[position_in_text]:
            position_in_text += 1
            position_in_pattern += 1
            if position_in_pattern == size_pattern:
                positions.append(position_in_text - position_in_pattern)
                position_in_pattern = table[position_in_pattern]
        else:
            position_in_pattern = table[position_in_pattern]
            if position_in_pattern < 0:
                position_in_text += 1
                position_in_pattern += 1
    return positions



print(kmp_table('batata'))
print(kmp_search('comer batata frita eh melhor que comer batata assada, mas batata assada eh melhor que nenhuma batata','batata'))
# print(kmp_table(['abcdeabfabc']))
# print(kmp_table(['aabcadaabe']))
# print(kmp_table(['aaaabaacd']))
