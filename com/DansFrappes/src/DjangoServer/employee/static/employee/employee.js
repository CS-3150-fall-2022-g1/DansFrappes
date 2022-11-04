function showEdit(uid) {
    var edForm = document.getElementById("editForm"+uid);
    edForm.style = "display: inline;";
    var editButton = document.getElementById("editbutton"+uid);
    editButton.style = "display: none;";
    var cancel = document.getElementById("cancelbutton"+uid);
    cancel.style = "display: inline;";
}
function hideEdit(uid) {
    var edForm = document.getElementById("editForm"+uid);
    edForm.style = "display: none;";
    var editButton = document.getElementById("editbutton"+uid);
    editButton.style = "display: inline;";
    var cancel = document.getElementById("cancelbutton"+uid);
    cancel.style = "display: none;";
}