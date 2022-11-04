const ingredientList = document.getElementById("ingredient-list");
const ingredientSelector = document.getElementById("ingredient-selector");
const amountSelector = document.getElementById("amount-selector");
const milkSelector = document.getElementById("milk-selector")

const ingredients = {}

function addIngredient() {
    var name = ingredientSelector.value
    var amount = amountSelector.value

    ingredients[name] = amount
    drawIngredients()
}

function initIngredient(name, amount) {
    ingredients[name] = amount
}

function removeIngredient(ingredient) {
    delete ingredients[ingredient]
    drawIngredients()
}

function drawIngredients() {
    ingredientList.innerHTML=""
    for (const [ingredient, amount] of Object.entries(ingredients)) {
        ingredientList.appendChild(makeIngredientDisplay(ingredient))
    }
}

function makeIngredientDisplay(ingredient) {
    var template = document.createElement("div")
    template.classList.add("ingredient_row")
    
    var remove = document.createElement("button")
    remove.onclick = () => removeIngredient(ingredient)
    remove.textContent="x"
    template.appendChild(remove)

    var label = document.createElement("span")
    label.textContent = ingredient
    template.appendChild(label)

    var qty = document.createElement("input")
    qty.type="number"
    qty.min="1"
    qty.max="9"
    qty.value=ingredients[ingredient]
    template.appendChild(qty)

    return template
}

function addToCart(path) {
    fetch(path, {
        method: "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(ingredients)
    })
}