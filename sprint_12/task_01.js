function getMin(arr) {
    return [].sort.apply(arr, (a, b) => a - b)[0]
}
