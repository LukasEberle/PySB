#In Germany we would say "Dieses Programm tut Pi raten!" and I think this is beautiful!
import random
import math


def main():
    print_controller(10)
    print_controller(100)
    print_controller(1000)
    print_controller(10000)
    print_controller(100000)
    print_controller(1000000)


def print_controller(num):
    print(f"Estimation with {num} points: {estimate_pi(num)}. The absolute mistake is {abs(estimate_pi(num) - math.pi)}!")


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
