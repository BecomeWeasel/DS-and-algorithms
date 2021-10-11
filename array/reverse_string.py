def reverse(string):
    if not string:
        return ""
    result = []
    for i in range(len(string) - 1, -1, -1):
        result.append(string[i])

    return ''.join(result)


def reverse_with_recursive(string):
    if len(string):
        return reverse_with_recursive(string[1:]) + string[0]
    else:
        return string


print(reverse_with_recursive("hi this is reversed"))
print(reverse("hi this is reversed"))
print(reverse(""))