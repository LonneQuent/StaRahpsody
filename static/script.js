
// Fonction pour mettre à jour le fond en fonction de l'univers
function updateBackground() {
    // Récupérer la valeur de l'univers
    var univers = "{{univers}}";

    // Mettre à jour le fond en fonction de la valeur de l'univers
    document.body.style.backgroundImage = getBackgroundImage(univers);
}

// Fonction pour obtenir l'image de fond en fonction de l'univers
function getBackgroundImage(univers) {
    switch (univers) {
        case "Star Wars":
            return 'url("S-W.jpg")'; 
        case "Harry Potter":
            return 'url("H-P.jpg")';
        case "Seigneur des anneaux":
            return 'url("S-A.jpg")';
    }
}

// Appeler la fonction au chargement de la page
window.onload = updateBackground;
