<!DOCTYPE html>
<html>
	<head>
		<meta charset = "utf-8"/>
		<title>Menu RaspiWatch</title>
	</head>

	<body>
		<header>
			<h1>Menu RaspiWatch</h1>
		</header>

		<h2>Menu Principal</h2>
		<section>
			<form id="menu" action="cgi-bin/raspiwatch.cgi" method="GET" target="_blank">
				<legend> Que souhaitez-vous faire ? </legend>
				<fieldset>
				<input type = "submit" name = "on" value = "Démarrer">
				<input type = "submit" name = "off" value = "Arrêter">
				<input type = "submit" name = "photo" value = "Photo">
				</fieldset>
			</form>
		</section>
		
		<h2> Configuration </h2>
		<section>
			<form id="config" action="cgi-bin/raspiwatch.cgi" method="GET" target="_blank">
				<fieldset>
					<legend>Résolution</legend>
					<input type = "radio" name = "res" value = "1" checked>1900x1080<br>
					<input type = "radio" name = "res" value = "2">1280x720<br>
					<input type = "radio" name = "res" value = "3">640x480<br>
					
					<legend>Images par seconde</legend>
					<input type = "radio" name = "ips" value = "30" checked>30<br>
					<input type = "radio" name = "ips" value = "25">25<br>
					<input type = "radio" name = "ips" value = "20">20<br>
					<input type = "radio" name = "ips" value = "15">15<br>
					
					
					<legend>Seuil de détection</legend>
					<input type="range"  id = "seuil" name = "seuil" min="0" max="100" value="50" step = "5" oninput="document.getElementById('AfficheRange1').textContent=value" />
					<span id="AfficheRange1">50</span>%
					
					
					<legend>Luminosité</legend> 
					<input type="range"  id = "lum" name = "lum" min="0" max="100" value="50" step = "5" oninput="document.getElementById('AfficheRange2').textContent=value" />
					<span id="AfficheRange2">50</span>%
					
					<input type = "submit" name = "submit" value = "submit">
				</fieldset>
			</form>
		</section>
		
		<h2>Photos</h2>
		<section>

		<!-- Ce script php ouvre le dossier /home/pi/RaspiWatch/photo et lit le nom des fichiers, puis ajoute du HTML tel qu'on a 
			[ip]/photo/[nomphot].jpg 
		Cela marche parcequ'un Alias est crée dans la conf de apache tel que /photo pointe vers   /home/pi/RaspiWatch/photo, qui
		n'est pas accessible par html sinon. -->
		    <?php
			
			$path="/home/pi/RaspiWatch/photo";
		    // open this directory 
		    $myDirectory = opendir($path);

		    // get each entry
		    while($entryName = readdir($myDirectory)) {
			    $dirArray[] = $entryName;
		    }

		    // close directory
		    closedir($myDirectory);

		    //	count elements in array
		    $indexCount	= count($dirArray);

		    ?>
		
		    <ul>

			    <?php
			    // loop through the array of files and print them all in a list
			    for($index=0; $index < $indexCount; $index++) {
				    $extension = substr($dirArray[$index], -3);
				    if ($extension == 'jpg'){ // list only jpgs
					    echo '<li><img src="photo/'. $dirArray[$index] .'" alt="'.$dirArray[$index].'" /><span>' . $dirArray[$index] . '</span>';
				    }	
			    }
			    ?>

		    </ul>	
		</section>
		
		<footer>
		Footer ici
		</footer>

	</body>
</html>
