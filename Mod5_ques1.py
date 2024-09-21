import random


def approximate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1

    pi_approximation = 4 * points_inside_circle / num_points
    return pi_approximation
def main():
    try:
        num_points = int(input("Enter the number of random points to generate: "))
        if num_points <= 0:
            print("The number of points must be a positive integer.")
            return
        pi_value = approximate_pi(num_points)
        print(f"Approximation of pi using {num_points} random points: {pi_value}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
main()
