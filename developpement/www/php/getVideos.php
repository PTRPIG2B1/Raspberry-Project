<?php

/**
* Script pour récupérer le code HTML nécéssaire à l'affichage des vidéos avec miniature
*
* Ce script ouvre le répertoire contenant les vidéos, et crée un tableau avec la totalité
* des noms des fichiers vidéo. Ca génère ensuite le code HTML nécéssaire pour chaque miniature
* entouré d'une balise <li>.
*
*/

// On append tous les noms de fichier dans un tableau
$videoPath="/home/pi/RaspiWatch/video";
$videoDirectory = opendir($videoPath);
while($filename = readdir($videoDirectory)) {
    $videoArray[] = $filename;
}
closedir($videoDirectory);
$nbVideo = count($videoArray);

//Boucle principale, pour chaque fichier, si c'est une vidéo, alors on génère le code pour télécharger la vidéo (<a>) et la miniature (<img>)
for($index=0; $index < $nbVideo; $index++) {
    $vidName = $videoArray[$index];
    $miniName= substr($vidName,0, strlen($vidName)-4).'jpg';
    $extension = substr($vidName, -4);
    if ($extension == 'h264'){
        echo '<li><a href="video/'.$vidName.'"><img src="video/miniatures/'.$miniName.'" alt="'.$miniName.'" /><span>'. $vidName.'</span></a></li>';
    }
}
?>
