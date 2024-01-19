<?php
if (isset($_POST['saga'])) {
    $selectedSaga = $_POST['saga'];

    if ($selectedSaga == "Star_Wars") :
?>
        <select name="perso_1" id="perso_1">
            <option value="desactive_3" disabled>Sélectionner un personnage </option>
            <option value="Jar_Jar_Binks">Jar Jar Binks</option>
            <option value="Yoda">Yoda</option>
            <option value="Vador">Vador</option>
        </select>
<?php elseif ($selectedSaga == "Harry_Potter") : ?>
        <select name="perso_2" id="perso_2">
            <option value="desactive_2" disabled>Sélectionner un personnage </option>
            <option value="Gryffondor">Gryffondor</option>
            <option value="Poufsouffle">Poufsouffle</option>
            <option value="Serdaigle">Serdaigle</option>
            <option value="Serpentard">Serpentard</option>
        </select>
<?php elseif ($selectedSaga == "Seigneur_des_anneaux") : ?>
        <select name="perso_3" id="perso_3">
            <option value="desactive_2" disabled>Sélectionner un personnage </option>
            <option value="Azog">Azog</option>
            <option value="Legolas">Legolas</option>
            <option value="Gimli">Gimli</option>
        </select>
<?php endif;
}
?>
