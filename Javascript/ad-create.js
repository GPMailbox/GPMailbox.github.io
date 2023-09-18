
const categories = [
    "Meubles", "Vêtements", "Électronique", "Sports et loisirs", "Livres", "Automobile", "Instruments", "Cuisine & Alim.", "Art", "Outils", "Santé & Beauté", "Jeux vidéos", "Bébés & enfants", "Appareils photos", "Équipement audio", "Animaux"
    ];
  
    const categorySelect = document.getElementById('categorySelect');
  
    categories.forEach(category => {
    const option = document.createElement('option');
    option.value = category;
    option.textContent = category;
    categorySelect.appendChild(option);
    });
  
    const cities = [
      "Les Abymes", "Anse-Bertrand", "Baie-Mahault", "Baillif", "Basse-Terre", "Bouillante", "Capesterre-Belle-Eau", "Capesterre-de-Marie-Galante", "Deshaies", "Gourbeyre", "Goyave", "Grand-Bourg", "Lamentin", "Morne-à-l'Eau", "Petit-Bourg", "Petit-Canal", "Pointe-à-Pitre", "Pointe-Noire", "Port-Louis", "Saint-Claude", "Saint-François", "Saint-Louis", "Sainte-Anne", "Sainte-Rose", "Terre-de-Bas", "Terre-de-Haut", "Trois-Rivières", "Vieux-Fort", "Vieux-Habitants"
    ];
  
    const citySelect = document.getElementById('citySelect');
  
    cities.forEach(city => {
      const option = document.createElement('option');
      option.value = city;
      option.textContent = city;
      citySelect.appendChild(option);
    });
  
    const imageUpload = document.getElementById("imageUpload");
  const previewContainer = document.getElementById("previewContainer");
  const imageModal = document.getElementById("imageModal");
  const modalImage = document.querySelector(".modal-image");
  const closeModal = document.querySelector(".close-modal");
  const modalPrev = document.querySelector(".modal-prev");
  const modalNext = document.querySelector(".modal-next");
  const selectedImages = [];
  let currentImageIndex = 0;
  
  imageUpload.addEventListener("change", function () {
      previewContainer.innerHTML = "";
      selectedImages.length = 0;
  
      Array.from(imageUpload.files).slice(0, 10).forEach((selectedImage) => {
          const reader = new FileReader();
          reader.onload = function () {
              const previewImage = document.createElement("div");
              previewImage.classList.add("preview-image");
  
              const imageElement = document.createElement("img");
              imageElement.src = reader.result;
              imageElement.classList.add("preview-image-img");
              previewImage.appendChild(imageElement);
  
              const deleteIcon = document.createElement("i");
              deleteIcon.classList.add("fas", "fa-times", "delete-icon");
              previewImage.appendChild(deleteIcon);
  
              previewContainer.appendChild(previewImage);
  
              deleteIcon.addEventListener("click", function () {
                  previewContainer.removeChild(previewImage);
                  selectedImages.splice(selectedImages.indexOf(selectedImage), 1);
                  updateNavigationArrows();
              });
  
              selectedImages.push(imageElement);
              updateNavigationArrows();
          };
          reader.readAsDataURL(selectedImage);
      });
  });
  
  function openModalWithImage(imageSrc) {
      modalImage.src = imageSrc;
      imageModal.style.display = "block";
      updateNavigationArrows();
  }
  
  function updateNavigationArrows() {
      modalPrev.style.display = currentImageIndex === 0 ? "none" : "block";
      modalNext.style.display = currentImageIndex === selectedImages.length - 1 ? "none" : "block";
  }
  
  function handleNavigationClick(direction) {
      if (direction === "prev") {
          currentImageIndex = (currentImageIndex - 1 + selectedImages.length) % selectedImages.length;
      } else if (direction === "next") {
          currentImageIndex = (currentImageIndex + 1) % selectedImages.length;
      }
  
      modalImage.src = selectedImages[currentImageIndex].src;
      updateNavigationArrows();
  }
  
  previewContainer.addEventListener("click", function (event) {
      if (event.target.classList.contains("preview-image-img")) {
          const clickedImageSrc = event.target.src;
          currentImageIndex = Array.from(previewContainer.children).indexOf(event.target.parentNode);
          openModalWithImage(clickedImageSrc);
      }
  });
  
  closeModal.addEventListener("click", function () {
      imageModal.style.display = "none";
  });
  
  imageModal.addEventListener("click", function (event) {
      if (event.target === imageModal) {
          imageModal.style.display = "none";
      }
  });
  
  modalPrev.addEventListener("click", function () {
      handleNavigationClick("prev");
  });
  
  modalNext.addEventListener("click", function () {
      handleNavigationClick("next");
  });
  
  const priceInput = document.getElementById("priceInput");
  
  priceInput.addEventListener("input", function () {
  this.value = this.value.replace(/[^\d,.]/g, ""); 
  
  if (this.value.includes(",")) {
    this.value = this.value.replace(".", ","); 
    const parts = this.value.split(",");
    if (parts.length > 1) {
      this.value = parts[0] + "," + parts[1].substring(0, 2);
    }
  }
  
  if (this.value.includes(",")) {
    const parts = this.value.split(",");
    if (parts.length > 1) {
      this.value = parts[0] + "," + parts[1].substring(0, 2);
    }
  }
  
  if (!this.value.endsWith("€")) {
    this.value = this.value.replace(/€/g, "") + "€";
  }
  });
  
  priceInput.addEventListener("focus", function () {
  this.value = this.value.replace("€", "");
  });
  
  priceInput.addEventListener("keydown", function (event) {
  if (event.key === "Backspace") {
    this.value = this.value.slice(0, -1);
    event.preventDefault();
  }
  });
  
  document.querySelector("#create-ad-form").addEventListener("submit", function (event) {
  if (selectedImages.length === 0) {
    event.preventDefault();
    alert("Veuillez importer au moins une image.");
  }
  
  const categorySelect = document.querySelector("select[name='category']");
  if (categorySelect.selectedIndex === 0) {
  event.preventDefault();
  alert("Veuillez sélectionner une catégorie de produit.");
  }
  
  const qualitySelect = document.querySelector("select[name='quality']");
  if (qualitySelect.selectedIndex === 0) {
    event.preventDefault();
    alert("Veuillez indiquer la qualité du produit.");
  }
  
  const citySelect = document.querySelector("select[name='city']");
  if (citySelect.selectedIndex === 0) {
    event.preventDefault();
    alert("Veuillez sélectionner une ville.");
  }
  });