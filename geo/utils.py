
import math


def pythagoras(a, b):
    """
    두 변의 길이 a, b를 받아 빗변의 길이를 반환합니다.
    """
    c = math.sqrt(a**2 + b**2)
    return c


def circle(r):
    """
    반지름 r을 받아 원의 면적을 반환합니다.
    """
    area = math.pi * r**2
    return area
