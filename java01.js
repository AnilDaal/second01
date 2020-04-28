ai = {
    nuber: 0,
    age: 20,
    form:2,
}
 
form = function(todo,lk){
    todo.age = lk + todo.age
    return ai.age;
    
}
console.log(form(ai,5));


