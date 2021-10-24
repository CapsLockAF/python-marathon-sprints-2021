const filterNums = (array, number=0, parameter='greater' ) => {
    const res = array.filter((x) => {
        switch (true) {
            case parameter == 'greater':
                return x > number
            case parameter == 'less':
                return x < number
            default:
                break;
        }
    })
    return res
};
