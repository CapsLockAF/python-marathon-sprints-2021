const sumOfLen = (a="", ...strings) => {
    return [a, ...strings].reduce((a, b) => a + b).length
}
