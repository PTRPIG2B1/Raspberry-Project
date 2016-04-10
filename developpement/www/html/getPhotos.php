/**
* Script pour récupérer le code HTML nécéssaire à l'affichage des photos
*
* Ce script ouvre le répertoire contenant les photos, et crée un tableau avec la totalité
* des noms des fichiers photos. Ca génère ensuite le code HTML nécéssaire pour chaque image
* entouré d'une balise <li>.
*
*/

<?php
$photoPath="/home/pi/RaspiWatch/photo";
$photoDirectory = opendir($photoPath);
while($filename = readdir($photoDirectory)) {
    $photoArray[] = $filename;
}
closedir($photoDirectory);
$nbPhoto = count($photoArray);

for($index=0; $index < $nbPhoto; $index++) {
    $name = $photoArray[$index]
    $extension = substr($name, -3);
    if ($extension == 'jpg'){
        echo '<li><a href="photo/'. $name.'"><img src="photo/'. $name .'" alt="'.$name.'" /><span>' . $name . '</span></a></li>';
    }
}
?>
