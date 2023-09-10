// Obtener elementos de los botones
var retrocederBtn = document.querySelector(".btn1");
var continuarBtn = document.querySelector(".btn2");

// Crear una matriz de elementos de sección
var sections = document.querySelectorAll('.my_dashboard_review');

// Índice de la sección actual
var currentSectionIndex = 0;

// Función para mostrar la sección actual y ocultar las demás
function showSection(index) {
    for (var i = 0; i < sections.length; i++) {
        if (i === index) {
            sections[i].style.display = "block";
        } else {
            sections[i].style.display = "none";
        }
    }
}

// Asociar función al botón "Retroceder"
function previous_page() {
    console.log("retroceder");
    if (currentSectionIndex > 0) {
        currentSectionIndex--;
        showSection(currentSectionIndex);
    }

}


// Asociar función al botón "Continuar"
function next_page() {
    console.log("avanzar");
    if (currentSectionIndex < sections.length - 1) {
        currentSectionIndex++;
        showSection(currentSectionIndex);
    }
}

// Mostrar la primera sección inicialmente
showSection(currentSectionIndex);



