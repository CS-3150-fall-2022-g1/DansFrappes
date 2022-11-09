function addToOrdering(name) {
    let element = document.getElementById("icount" + name);
    let count = Number.parseInt(element.textContent) +1;
    element.textContent = count;
    return count;
}

function subFromOrdering(name){
    let element = document.getElementById("icount" + name);
    let count = Number.parseInt(element.textContent); 
    if(count == 0){
        return count;
    } else{
        element.textContent = count - 1;
    }
    return count;
}