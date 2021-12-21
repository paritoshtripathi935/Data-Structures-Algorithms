def hourglassSum(arr):
    total_sums = []

    for i in range(1, len(arr) - 1):
        c_row = arr[i]
        for j in range(1, len(c_row) - 1):
            total_sums += [arr[i][j] + arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i + 1][j - 1] +
                           arr[i + 1][j] + arr[i + 1][j + 1]]
    return max(total_sums)
