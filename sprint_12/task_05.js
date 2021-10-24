function mapCreator(keys, values) {
    const myEntries = keys.reduce((acc, k, i) => {
        return typeof values[i] === 'string'? [...acc, [k, values[i]]] : acc
    }, [])
    return new Map(myEntries)
}

