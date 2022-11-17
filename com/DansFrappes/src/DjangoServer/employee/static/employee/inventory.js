var prices = {};

function addPrices(data){
    Object.keys(data).forEach(name => {
        prices[name] = parseFloat(data[name]);
    })
}

function addToOrdering(name){
    let element = document.getElementById("icount" + name);
    let count = Number.parseInt(element.value) +1;
    element.value = count;

    makeReceipt(name);
}

function subFromOrdering(name){
    let element = document.getElementById("icount" + name);
    let count = Number.parseInt(element.value); 
    if(count == 0){
        return count;
    } else{
        element.value = count - 1;
    }

    makeReceipt(name);
}

function buy(balance, names){
    let bill = parseFloat(calcTotal());
    if(bill > balance){
        alert("WARNING: Insufficient Funds")
    }else{
        let nameList = names.split("^");
        let counts = {};
        nameList.forEach(name => {
            let element = document.getElementById("icount" + name);
            let count = Number.parseInt(element.value); 
            counts[name] = count;
        });

        let post = new XMLHttpRequest();
        post.open('POST', '/employee/buy/', true);
        post.setRequestHeader('Content-Type', 'application/json');  
        post.onreadystatechange = function () {
            if (post.readyState === 4) {
            window.location.replace("/employee/buy/");
            }};  
        post.send(JSON.stringify({'counts':counts,'bill':bill}));
    }
}

function cleanUp(id){
    let element = document.getElementById("icount" + id);
    let clean = "";
    for(let i = 0; i < element.value.length; i++){
        if(!isNaN(parseInt(element.value[i]))){
            clean += parseInt(element.value[i]);
        }
    }
    if(clean.length === 0){
        clean = "0";
    }

    let count = Number.parseInt(clean);
    element.value = count;

    makeReceipt(id);
}

function calcTotal(){
    let total = 0;
    Object.keys(prices).forEach(name => {
        base = parseFloat(prices[name]);
        let ingField = document.getElementById("icount" + name);
        let count = Number.parseInt(ingField.value); 

        total += (count * base)
    });

    return total.toFixed(2)
}

function makeReceipt(name){
    let ingField = document.getElementById("icount" + name);
    let count = Number.parseInt(ingField.value); 
    let price = (prices[name] * count).toFixed(2);
    
    let entry = document.getElementById("ordering" + name)
    let receipt = document.getElementById("receipt");
    if(!!entry){
        entry.textContent = name + '   $' + price;
    } else{
        entry = document.createElement("h3");
        entry.textContent = name + '   $' + price;
        entry.id = "ordering" + name;
        receipt.appendChild(entry);
    }
    
    if(count == 0){
        receipt.removeChild(entry);
    }

    let total = calcTotal();
    let finalCost = document.getElementById("total");
    finalCost.textContent = 'Total:   $' + total;
}