# 平方的平方
def get_an_generator(x: int):
    current_result = x
    while True:
        current_result = current_result ** 2
        yield current_result


def main():
    generator_2 = get_an_generator(2)
    generator_3 = get_an_generator(3)

    for time in range(3):
        a, b = next(generator_2), next(generator_3)
        print('第%s次, %s + %s = %s' % (time + 1, a, b, a + b))


if __name__ == '__main__':
    main()
