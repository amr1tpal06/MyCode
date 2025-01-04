const person= {
    name: 'amrit',
    surname:'sandhu',
    age:18,
    pets: function (n) {
        console.log('amrit has ', n ,' pets')
    }
}

person.job='software';
person['age']=19;
array= Object.values(person);
newarray= Object.entries(person);
console.log(person.pets(9));

for (let x of array){
    console.log(x);
}

const names = new Set (['amrit', 'jeevan', 'avneet'])
names.add('veer');
names.has('amrit')
console.log(names)

//maps have key value pairs 

//classes

function myClass (name, surname, age){
    this.name = name;
    this.surname=surname 
    this.age=age;
}

myClass.prototype.school='dggs';

const amrit = new myClass ('amrit', 'sandhu', 18);
console.log(amrit);


//everything +  arrow functions 
//objects, dom, ts and querying 
//angular 