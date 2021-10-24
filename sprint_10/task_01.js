function modifyArray(array) {
    [array[0], array[array.length - 1]] = ['Start', 'End']
    return array
 }