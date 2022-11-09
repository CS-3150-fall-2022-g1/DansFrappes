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

async function buy(names){
    let nameList = names.split("^");
    let counts = {};
    nameList.forEach(name => {
        let element = document.getElementById("icount" + name);
        let count = Number.parseInt(element.textContent); 
        counts[name] = count;
    });

    let post = new XMLHttpRequest();
    post.open('POST', '/employee/buy/', true);
    post.setRequestHeader('Content-Type', 'application/json');    
    post.send(JSON.stringify(counts));
    window.location.replace("/employee/buy/");
}