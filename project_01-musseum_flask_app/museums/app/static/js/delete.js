

function delete_selection(){
    var elem=document.getElementById("museum");

    console.log(elem.options[elem.selectedIndex].value);
    $.ajax({
    url: "https://8080-cs-880609831488-default.cs-europe-west4-bhnf.cloudshell.dev/admin/"+elem.options[elem.selectedIndex].value,
    type: 'DELETE',
    });

}