# Plotting Cumulative Distribution Functions (CDFs)

## `plot_single_cdf`

This function is used to plot a single Cumulative Distribution Function (CDF).

### Parameters:
- **points**: List of tuples representing points for the CDF (x, y).
- **color**: (Optional) Color of the lines. Default is 'blue'.

### Example Usage:
```python
points_single = [(-40000, 0.05), (50000, 0.65), (220000, 1), (250000, 1)]
plot_single_cdf(points_single, color='red')

 ```
## Output 
![ggadd1](https://github.com/Burakyvz/riskanalysis-cdf-plotter/assets/74691005/b003814d-ab4c-4c70-86f3-183fa40c7708)


### Example Usage for `plot_comparison_cdf`

This function is used to plot multiple Cumulative Distribution Functions (CDFs) for comparison.

#### Parameters:
- **points_list**: List of lists containing points for each CDF to compare.
- **labels**: (Optional) Labels for each CDF. If provided, should have the same length as points_list.
- **color1**: (Optional) Color of the lines for the first CDF. Default is 'blue'.
- **color2**: (Optional) Color of the lines for the second CDF. Default is 'green'.

#### Example Usage:
```python
points_compare = [[(0,0),(20000, 0.30), (200000, 0.75), (550000, 1), (600000, 1)],
                  [(-40000, 0.05), (50000, 0.65), (220000, 1), (250000, 1)]]
plot_comparison_cdf(points_compare, labels=['Strategy 1', 'Strategy 2'], color1='blue', color2='green')
```

## Output 
![ggadd2](https://github.com/Burakyvz/riskanalysis-cdf-plotter/assets/74691005/12626bc6-67f5-48b9-bc02-58403e6737c9)
