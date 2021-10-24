function longestLogin(loginList) {
    return loginList.reduce((a, b) => a.length <= b.length ? a = b : a)
}
