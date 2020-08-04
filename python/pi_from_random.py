import random
import math


def main():
    x = estimate_pi(10)
    print(f"Estimation with 10 points: {x}. The absolute mistake is {abs(x - math.pi)}!")
    x = estimate_pi(100)
    print(f"Estimation with 100 points: {x}. The absolute mistake is {abs(x - math.pi)}!")
    x = estimate_pi(1000)
    print(f"Estimation with 1000 points: {x}. The absolute mistake is {abs(x - math.pi)}!")
    x = estimate_pi(10000)
    print(f"Estimation with 10000 points: {x}. The absolute mistake is {abs(x - math.pi)}!")
    x = estimate_pi(100000)
    print(f"Estimation with 100000 points: {x}. The absolute mistake is {abs(x - math.pi)}!")
    x = estimate_pi(1000000)
    print(f"Estimation with 1000000 points: {x}. The absolute mistake is {abs(x - math.pi)}!")


def estimate_pi(num):
    points_in_circle = 0
    point_list = get_random_points(num)
    for p in point_list:
        if est_distance_from_center(p) < 1:
            points_in_circle += 1
    return 4 * points_in_circle/len(point_list)


def get_random_points(num):
    list_of_points = []
    for i in range(num):
        p = (random.uniform(0,1), random.uniform(0,1))
        list_of_points.append(p)
    return list_of_points


def est_distance_from_center(tupel):
    return tupel[0]**2 + tupel[1]**2


if __name__ == '__main__':
    main()
