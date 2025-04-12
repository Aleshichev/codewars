# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text, ending):
        return True if text.endswith(ending) else False

print(solution('abc', 'bc'))


def solution(string, ending):
    return ending in string[-len(ending):]
print(solution('abc', 'bc'))
