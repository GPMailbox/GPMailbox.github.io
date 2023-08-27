function removeAccents(input) {
    return input.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  }
  
  document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search");
    const suggestionBox = document.getElementById("suggestions");
    
      const suggestions = ["Téléphone",
      "Ordinateur",
      "Réfrigérateur",
      "Aspirateur",
      "Lave-linge",
      "Téléviseur",
      "Cafetière",
      "Bouilloire",
      "Micro-ondes",
      "Tablette",
      "Console de jeu",
      "Casque audio",
      "Chaussures",
      "Sac à dos",
      "Montre",
      "Appareil photo",
      "Parfum",
      "Maquillage",
      "Vêtement",
      "Bijou",
      "Canapé",
      "Chaise",
      "Table",
      "Lit",
      "Matelas",
      "Lampe",
      "Rideau",
      "Tapis",
      "Miroir",
      "Casserole",
      "Poêle",
      "Vaisselle",
      "Verre",
      "Assiette",
      "Couvert",
      "Nappe",
      "Ustensile de cuisine",
      "Serviette",
      "Shampoing",
      "Gel douche",
      "Dentifrice",
      "Brosse à dents",
      "Serviette de bain",
      "Tondeuse",
      "Rasoir",
      "Brosse à cheveux",
      "Sèche-cheveux",
      "Balai",
      "Seau",
      "Éponge",
      "Papier toilette",
      "Lessive",
      "Savon",
      "Détergent",
      "Désodorisant",
      "Serpillière",
      "Poubelle",
      "Fleur",
      "Plante d'intérieur",
      "Arrosoir",
      "Pelle de jardin",
      "Graines",
      "Engrais",
    
    ]
  
    
      searchInput.addEventListener("input", function () {
        const inputText = searchInput.value;
        const words = inputText.split(" ");
        const lastWord = words[words.length - 1].toLowerCase();
    
        suggestionBox.innerHTML = "";
    
        if (lastWord !== "") {
          const normalizedLastWord = removeAccents(lastWord);
    
          const matchingSuggestions = suggestions.filter(suggestion =>
            removeAccents(suggestion.toLowerCase()).startsWith(normalizedLastWord)
          );
    
          matchingSuggestions.forEach(suggestion => {
            const suggestionElement = document.createElement("div");
            suggestionElement.classList.add("suggestion");
            suggestionElement.textContent = suggestion;
            suggestionElement.addEventListener("click", function () {
              words[words.length - 1] = suggestion;
              searchInput.value = words.join(" ");
              suggestionBox.style.display = "none";
            });
            suggestionBox.appendChild(suggestionElement);
          });
    
          if (matchingSuggestions.length > 0) {
            suggestionBox.style.display = "block";
          } else {
            suggestionBox.style.display = "none";
          }
        } else {
          suggestionBox.style.display = "none";
        }
      });
    
      document.addEventListener("click", function(event) {
        if (!event.target.closest(".searchbar-container")) {
          suggestionBox.style.display = "none";
        }
      });
    });