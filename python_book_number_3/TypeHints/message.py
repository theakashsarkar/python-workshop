
# def show_count(count: int, word:str) -> str: 
#     if count == 1:
#         return f'1 {word}'
#     count_str = str(count) if count else 'no'
#     return f'{count_str} {word}s'

# show_count(3, "mouse", "mice")

def show_count(count: int, singular: str, plural: str = '') -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}'

show_count(1, "mouse")