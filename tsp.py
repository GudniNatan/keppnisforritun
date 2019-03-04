from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

# Distance callback


def create_distance_callback(dist_matrix):
    # Create a callback to calculate distances between cities.

    def distance_callback(from_node, to_node):
        return int(dist_matrix[from_node][to_node])

    return distance_callback


def read():
    points = list()
    with open("iceland.txt") as file:
        n = int(file.readline())
        for line in file:
            x, y = map(float, line.split())
            x *= 100000
            y *= 100000
            points.append((int(x), int(y)))
    return points


def get_dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def compute_dist_mat(points):
    dist_mat = list()
    for p1 in points:
        p1_dist = list()
        for p2 in points:
            p1_dist.append(get_dist(p1, p2))
        dist_mat.append(p1_dist)
    return dist_mat


def main():
    points = read()
    dist_matrix = compute_dist_mat(points)
    tsp_size = len(dist_matrix)
    num_routes = 1
    depot = 0

    # Create routing model
    if tsp_size > 0:
        routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        # Create the distance callback.
        dist_callback = create_distance_callback(dist_matrix)
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        # Solve the problem.
        assignment = routing.SolveWithParameters(search_parameters)
        if assignment:
            # Solution distance.
            print("Total distance: " + str(assignment.ObjectiveValue()))
            # Display the solution.
            # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
            route_number = 0
            # Index of the variable for the starting node.
            index = routing.Start(route_number)
            route = ''
            while not routing.IsEnd(index):
                # Convert variable indices to node indices in the displayed route.
                route += str(routing.IndexToNode(index)) + ' '
                index = assignment.Value(routing.NextVar(index))
            route += str(routing.IndexToNode(index))
            print("Route:\n\n" + route)
        else:
            print('No solution found.')
    else:
        print('Specify an instance greater than 0.')


if __name__ == '__main__':
    main()
