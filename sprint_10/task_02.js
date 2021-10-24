function combineArray(arr1, arr2) {
    return [...arr1, ...arr2].filter(x => typeof x == "number")
}