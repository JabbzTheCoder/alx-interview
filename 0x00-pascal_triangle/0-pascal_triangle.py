#!/usr/bin/python3


def pascal_triangle(n):
    
    pascal_triangle = []

    for i in range(n):
        row = []

        if i == 0:
            row.append(i+1)
        else:
            prev_row = pascal_triangle[len(pascal_triangle)-1]
            if len(prev_row) > 1:
                row = [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)]
            row.insert(0,1)
            row.append(1)
       
       
        pascal_triangle.append(row)
    return pascal_triangle
