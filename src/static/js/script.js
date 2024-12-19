// Función para mostrar el mensaje del pop-up
const showPopup = (message, type) => {
    let popup = document.createElement('div');
    popup.textContent = message;
    popup.style.position = 'fixed';
    popup.style.top = '25%';
    popup.style.left = '50%';
    popup.style.transform = 'translate(-50%, -50%)';
    popup.style.padding = '20px';
    popup.style.backgroundColor = (type === 'success') ? 'green' : 'red';
    popup.style.color = 'white';
    popup.style.fontSize = '16px';
    popup.style.borderRadius = '5px';
    popup.style.zIndex = '1000';
    document.body.appendChild(popup);

    // Desaparecer el popup después de 3 segundos
    setTimeout(() => {
        popup.style.display = 'none';
    }, 1500);
}

/* Escucho cuando todo el dom fue cargado */
document.addEventListener("DOMContentLoaded", () => {
    
    const formNewGame = document.querySelector("#form-new-game")
    
    const txtfiltro = document.querySelector("#filtro")
    const btn = document.querySelector("#btn-show-table")

    //Botones Delete y Update
    const btnsDelete = document.querySelectorAll(".btnDelete")
    const btnsUpdate = document.querySelectorAll(".btnUpdate")

    //Boton confirmacion de modificacion
    const btnConfirmUpdate = document.querySelector("#btnConfirmUpdate")
    const btnNewGame = document.querySelector("#btnNewGame")

    //Input para buscar juego
    const inputSearch = document.querySelector("#inputSearch")

    //Logica para detectar los cambios del input en tiempo real
    //y ocultar filas de la tabla que contengan el valor del input
    inputSearch.addEventListener("input", (e) => {
        const input = inputSearch.value.toLowerCase()
        const tbl = document.querySelector("#table-games")
        const rows = document.querySelectorAll("tbody tr")
        rows.forEach(row => {
            let name = row.querySelector("td[data-name]").getAttribute("data-name").toLowerCase()
            row.style.display = name.includes(input) ? "" : "none"    
        })
        
    })


    //Logica para eliminar elemento de la base de datos
    btnsDelete.forEach( btn => {
        
        btn.addEventListener("click", () => {
            if(confirm("¿Desea eliminar este item?")){
                let id = btn.getAttribute("data-id")
                fetch(`/games/${id}`, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(data => {
                    if(data.success){
                        btn.closest("tr").remove()
                        showPopup(data.message, "success")
                    }else{
                        showPopup(data.message, "error")
                    }
                })
                .catch(err => {
                    showPopup("Hubo un error al eliminar el item", "error")
                })

            }
    
        })
    })

})

 //Confirmar actualizacion de juego
 function updateGame(){
    const formUpdateGame = document.querySelector("#form-update-game")
    const formData = new FormData(formUpdateGame)
    const id = document.querySelector("#id").value
    
    if(validateForm(formData)){
        
        fetch(`/games/update/${id}`, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if(data.success){
                showPopup(data.message, "success")
                window.location.href = "/games"
            }else{
                showPopup(data.message, "error")
            }
        })
        .catch(err => {
            showPopup("Hubo un error al actualizar el juego", "error")
        })
    }else{
        alert("Datos ingresados inválidos")
    }

}


//Funcion para insertar juego nuevo
function insertNewGame() {
    const formNewGame = document.querySelector("#form-new-game")
    const formData = new FormData(formNewGame)
    
    //válido que los datos ingresados sean correctos
    if (validateForm(formData)){
        fetch('/games/create', {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success){
                showPopup(data.message, "success")
                setTimeout(() => {
                    window.location.href = "/games"
                }, 2000)
            }else{
                showPopup(data.message, "error")
            }
        })
        .catch(error => {
            showPopup("Hubo un error en la solicitud", "error")
        })
    }else{
        alert("Datos ingresados inválidos")
    }
}

//Funcion para validar campos de formulario
function validateForm(form){
    const regex = /^[A-Za-z0-9\s\-_\.]{3,100}$/ //Expresion regular para permitir letras, numeros y simbolos ".-_"
    //campos del formulario
    const name = form.get("name") 
    const country = form.get("country")
    const minPlayers = form.get("min_players") > 0 
    const maxPlayers = form.get("max_players") > 0 
    const ageLimit = form.get("age_limit") > 0 
    const cost = form.get("cost") > 0
    console.log(minPlayers, maxPlayers, ageLimit, cost)


    return regex.test(name) && minPlayers && maxPlayers && ageLimit && cost && regex.test(country)

}