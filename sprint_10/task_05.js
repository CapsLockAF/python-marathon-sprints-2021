function checkAdult(age){
    try {
        switch (true) {
            case typeof age == 'undefined':
                throw new Error("Please, enter your age")

            case typeof age != "number":
                throw new Error("Please, enter number")
                
            case !Number.isInteger(age):
                throw new Error("Please, enter Integer number")
                
            case age < 0:
                throw new Error("Please, enter positive number")
                
            case age < 18:
                throw new Error("Access denied - you are too young!")
                
            default:
                console.log("Access allowed")
                break;
        }
        
    } catch (e) {
        console.log(`${e.name} ${e.message}`)
    } finally {
        console.log("Age verification complete")
    }
}