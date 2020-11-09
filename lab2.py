def fuzzy_compare_string(s1: str, s2: str) -> float:
    count = 0
    for i in range(len(s1)):
        count += s2.count(s1[i:i+3])
    return count/max(len(s1), len(s2))

def fuzzy_compare_int(n1: int, n2: int) -> float:
    DELTA = 3
    if abs(n1 - n2) > DELTA:
        return 0.0
    return 1 - abs(n1 - n2) / DELTA 


class Ball:
    def __init__(self, size: int, color: str):
        self.size = size
        self.color = color

    def __repr__(self):
        return f"Ball({self.size}, {self.color})"

    def fuzzy_compare(self, ball):
        size_result = fuzzy_compare_int(self.size, ball.size)
        color_result = fuzzy_compare_string(self.color, ball.color)
        return  size_result * color_result


if __name__ == "__main__":
    balls = {
        "basketball": Ball(10, "orange"),
        "football": Ball(9, "black-white"),
        "tennis": Ball(2, "green"),
    }

    search_ball = Ball(8, "Orange")

    most_relevant_ball = sorted(balls.values(), key=search_ball.fuzzy_compare)[-1]
    print(most_relevant_ball)


