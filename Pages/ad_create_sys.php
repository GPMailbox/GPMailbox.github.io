<?php
$servername = "localhost";
$username = "votre_utilisateur";
$password = "votre_mot_de_passe";
$dbname = "votre_base_de_donnees";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("La connexion à la base de données a échoué : " . $conn->connect_error);
}

$titre = $_POST['title'];
$description = $_POST['description'];
$prix = $_POST['price'];
$ville = $_POST['city'];
$categorie = $_POST['category'];

$images = [];

$sql = "INSERT INTO annonces (titre, description, prix, ville, categorie, images) VALUES (?, ?, ?, ?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ssdsss", $titre, $description, $prix, $ville, $categorie, implode(",", $images));

if ($stmt->execute()) {
    echo "Annonce ajoutée avec succès.";
} else {
    echo "Erreur lors de l'ajout de l'annonce : " . $conn->error;
}

$stmt->close();
$conn->close();
?>
