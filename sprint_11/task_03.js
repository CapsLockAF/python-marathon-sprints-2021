const maxInterv = (...numbers) => {
    return numbers.reduce((acc, num, i, arr) => {
        if (i < arr.length - 1){
            const difference = Math.abs(arr[i + 1] - num)
            return (difference > acc ) ? difference : acc
        }
        return acc
    }, 0)
}

