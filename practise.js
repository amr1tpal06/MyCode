console.log("Amrit is here");
//exercises 
let x =2;
x=5;
console.log(x)
const y=9;
//let and const has block scope - only valid within {}
//const - cannot reassign it

//const for arrays, objects, functions and regexpr

const car= {
    type:"ford",
    color:"blue",
}

car.color="pink";
car.type="audi";
car.owner= "Amrit"

//cant make car = to something else /reassign it

//car= {
//    type:"audi",
//    color:"blue"
//} //error 

// division is /
// make = and do something, just add = to operator
// == equal to, === equal to and equal type, add ! for not

//LOGICAL OPERATORS - && (and) II(or) !(not)

//TYPE CHECK typeof, instanceof 

//Types- String, Number, Booelean, Null, Undefined, Object, Bigint 

let z= 12e2; 
console.log(z)

let num= BigInt(9343274362547653276452376);
//Bigint for nums that are too big 


//OBJECTS
const mycar= {
    type: "audi",
    color:"pink",
    manual: true,
}
mycar.owner="amrit"
mycar.type="ford"

//ARRAYS 
const names = ['amrit','keira','avneet']
console.log(names)

console.log(typeof(mycar))
console.log(mycar instanceof Object);

function addnumbers(num1, num2) {
    return num1+num2;
}

let number = addnumbers(2,9);
console.log(number);

const person = {
    name: 'amrit',
    age:'18',
    job:'software engineer',
    birthdaymonth:'march',
    yob:2006,
    pets: function (num1,num2) {
        return 'Amrit has ' + (num1+num2)+ ' pets';
    },
}

let o= person.pets(4,5);
console.log(o);

delete person.yob;
person["age"]= 19; //person.age=19;
console.log(person);

//nested objects 

const person2 = {
    name:'Avneet',
    age:16,
    job:'student',
    month:'september',
    subjects: {
        maths: 9,
        art: 9,
    }
}
console.log(person2.subjects.maths);



//OBJECTS 
const user = {
    name:'amrit',
    age:18,
    year:'year 14',
}
user.rating= 5;
user.age=19;
user['age']=20;
const array= Object.entries(user);
const newarray= Object.values(user); //make iterable 
console.log(array);
console.log(newarray);
JSON.stringify(user); //converts to string 
delete user.name; 

//OBJECT CONSTRUCTOR - function 
function somebody(name,age, job){
    this.name = name;
    this.age=age;
    this.job=job 
    this.person=true;
}
const Amrit = new somebody ('amrit', 18, 'software');
console.log('This is about Amrit-', Amrit);

const Avneet = new somebody ('avneet', 16, 'student');

somebody.prototype.siblings =2;

somebody.prototype.something= function () { 
    console.log(2+2);
}


