// Función para mostrar el mensaje del pop-up
const showPopup = (message, type) => {
    let popup = document.createElement('div');
    popup.textContent = message;
    popup.style.position = 'fixed';
    popup.style.top = '50%';
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
    }, 3000);
}


/* Escucho cuando todo el dom fue cargado */
window.addEventListener("DOMContentLoaded", () => {
    
    /* Funcion para enviar los datos del formulario para insertar nuevo juego */
    const formGame = document.querySelector("#form-game")
    const tbl = document.querySelector("#table-games")
    const txtfiltro = document.querySelector("#filtro")
    // const filas = tbl.getElementsByTagName('tr') 
    const btn = document.querySelector("#btn-show-table")
    formGame.addEventListener("submit", (e) => {
        event.preventDefault()
        const formData = new FormData(formGame)

        fetch('/games', {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success){
                showPopup(data.message, "success")
                console.log("success")
            }else{
                showPopup(data.message, "error")
                console.log("error")
            }

            //Reseteo el contenido del formulario
            formGame.reset()
        })
        .catch(error => {
            showPopup("Hubo un error en la solicitud", "error")
        })

    })
})






// btn.addEventListener("click", () => {
//     let str = txtfiltro.value
//     if (str != ""){
//         // Iterar sobre todas las filas de la tabla
//         for (let i = 1; i < filas.length; i++) {  // Empezamos desde 1 para evitar el encabezado
//             let fila = filas[i];
//             const celdas = fila.getElementsByTagName('td')
//             let nombre = celdas[0].textContent
    
//             if(!nombre.toLowerCase().includes(str.toLowerCase())){
//                 fila.style.display = "none"
//             }
//         }
//     }

// })