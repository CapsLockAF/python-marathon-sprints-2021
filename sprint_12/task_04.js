class Student {
    
    constructor(fullName, direction) {
      this._fullName = fullName;
      this._direction = direction;
    }
    
    showFullName(){
        return this._fullName
    }

    nameIncludes(data){
        return !!~this.showFullName().search(data)
    }


    static studentBuilder(fullName="Ihor Kohut", direction="qc") {
        return new this(fullName, direction) 
    }

    get direction(){
        return this._direction
    }

    set direction(d){
        this._direction = d
    }
}

const stud1 = new Student('Ivan Petrenko', 'web');
const stud2 = new Student('Sergiy Koval', 'python')
const stud3 = Student.studentBuilder("Ihor Kohut", "qc")

