import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plot_single_cdf(points, color='blue'):
    """
    Plot a single Cumulative Distribution Function (CDF).

    Parameters:
        points (list of tuples): List containing points for the CDF.
                                 Each tuple represents a point (x, y).
        color (str, optional): Color of the lines. Default is 'blue'.

    Returns:
        None
    """

    x_values = []
    y_values = []

    for i in range(len(points)):
        x, y = points[i]
        x_values.append(x)
        y_values.append(y)
        if i < len(points) - 1:
            next_x, next_y = points[i+1]
            if next_x == x:  # If x is constant, then the line is vertical
                linestyle = 'dashed'
                plt.plot([x, next_x], [y, next_y], linestyle=linestyle, color=color)
            else:  # If y is constant, then the line is horizontal
                linestyle = 'solid'
                plt.plot([x, next_x], [y, y], linestyle=linestyle, color=color)
                plt.plot([next_x, next_x], [y, next_y], linestyle='dashed', color=color)

    # Add labels for each point
    for point in points[:-1]:
        plt.text(point[0], point[1], f'({point[0]}, {point[1]})', verticalalignment='bottom')

    plt.xlabel('Outcome')
    plt.ylabel('Probability')
    plt.title('Cumulative Risk Profile')
    plt.grid(True)

    plt.show()

def plot_comparison_cdf(points_list, labels=None, color1='blue', color2='green'):
    """
    Plot multiple Cumulative Distribution Functions (CDFs) for comparison.

    Parameters:
        points_list (list of list of tuples): List containing points for each CDF to compare.
                                              Each sublist represents a CDF, and each tuple represents a point (x, y).
        labels (list of str, optional): Labels for each CDF. If provided, should have the same length as points_list.
        color1 (str, optional): Color of the lines for the first CDF. Default is 'blue'.
        color2 (str, optional): Color of the lines for the second CDF. Default is 'green'.

    Returns:
        None
    """

    if labels is None:
        labels = ['CDF {}'.format(i+1) for i in range(len(points_list))]
    elif len(labels) != len(points_list):
        raise ValueError("Number of labels should match the number of CDFs.")

    for i, points in enumerate(points_list):
        x_values = []
        y_values = []

        for j in range(len(points)):
            x, y = points[j]
            x_values.append(x)
            y_values.append(y)
            if j < len(points) - 1:
                next_x, next_y = points[j+1]
                if next_x == x:  # If x is constant, then the line is vertical
                    linestyle = 'dashed'
                    if i == 0:
                        plt.plot([x, next_x], [y, next_y], linestyle=linestyle, color=color1)
                    else:
                        plt.plot([x, next_x], [y, next_y], linestyle=linestyle, color=color2)
                else:  # If y is constant, then the line is horizontal
                    linestyle = 'solid'
                    if i == 0:
                        plt.plot([x, next_x], [y, y], linestyle=linestyle, color=color1)
                        plt.plot([next_x, next_x], [y, next_y], linestyle='dashed', color=color1)
                    else:
                        plt.plot([x, next_x], [y, y], linestyle=linestyle, color=color2)
                        plt.plot([next_x, next_x], [y, next_y], linestyle='dashed', color=color2)

        # Add labels for each point
        for point in points[:-1]:
            plt.text(point[0], point[1], f'({point[0]}, {point[1]})', verticalalignment='bottom')

    plt.xlabel('Outcome')
    plt.ylabel('Probability')
    plt.title('Combined CDFs')
    plt.grid(True)

    # Create legend entries using Line2D objects
    legend_entries = [Line2D([0], [0], color=color1, linestyle='solid'),
                      Line2D([0], [0], color=color2, linestyle='solid')]

    # Show legend with specified legend entries and labels
    plt.legend(legend_entries, labels)

    plt.show()


# Example usage:

# Single CDF with custom color
points_single = [(-40000, 0.05), (50000, 0.65), (220000, 1), (250000, 1)]
plot_single_cdf(points_single, color='red')

# Comparison CDFs with custom colors
points_compare = [[(0,0),(20000, 0.30), (200000, 0.75), (550000, 1), (600000, 1)],
                  [(-40000, 0.05), (50000, 0.65), (220000, 1), (600000, 1)]]
plot_comparison_cdf(points_compare, labels=['Strategy 1', 'Strategy 2'], color1='blue', color2='green')
