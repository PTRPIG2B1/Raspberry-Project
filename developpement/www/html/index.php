<!DOCTYPE html>
<html>
	<head>
		<meta charset = "UTF-8">
		<title>RaspiWatch</title>
		<link rel="stylesheet" type="test/css" href="css/style.css">
	</head>

	<body>
		<header>
			<img id = "logo" src = "images/logoRaspiWatch.png" alt="Logo  de RaspiWatch">
			<h1>RaspiWATCH</h1>
		</header>


		<nav>
			<div id = "menu">
				<ul id = "onglets">
					<li id = "onglet0" class = "active" onclick ="changeOnglet(0)"> Configuration </li>
					<li id = "onglet1" onclick ="changeOnglet(1)"> Photos </li>
					<li id = "onglet2" onclick ="changeOnglet(2)"> Vidéos </li>
				</ul>
			</div>
		</nav>

		<section>
			<form action="cgi-bin/raspiwatch.cgi" method="GET" target="_blank">
				<legend>Que souhaitez-vous faire ?</legend>
				<fieldset>
				<input type = "submit" name = "on" value = "Démarrer">
				<input type = "submit" name = "off" value = "Arrêter">
				<input type = "submit" name = "photo" value = "Photo">
				<input type = "submit" name = "video" value = "Vidéo">
				</fieldset>
			</form>
		</section>

		
		<section id = "contenuOnglet0">
			<h2> Configuration </h2>
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
					<input type="range"  id = "luminosite" name = "luminosite" min="0" max="100" value="50" step = "5" oninput="document.getElementById('AfficheRange2').textContent=value" />
					<span id="AfficheRange2">50</span>%
					
					<input type = "submit" name = "submit" value = "Valider">
				</fieldset>
			</form>
		</section>
		
		<section id = "contenuOnglet1">
		    <h2>Photos</h2>
		    <ul id="photos">
		        <!-- Le script php suivant génère du code HTML pour tous les images qu'il faut afficher-->
		        <?php include 'php/getPhotos.php';?>
		    </ul>	
		</section>

		<section id = "contenuOnglet2">
			<h2>Vidéos</h2>	
		    <ul id="videos">
		        <!-- Le script php suivant génère du code HTML pour tous les vidéos et miniatures qu'il faut afficher-->
		        <?php include 'php/getVideos.php';?>
		    </ul>
		</section>
		
		<footer>
		Site en construction.
		</footer>


		<script type="text/javascript">
		      var nombreOnglets = 3;
		      function changeOnglet(numero)
		      {
			// On commence par tout masquer
			for (var i = 0; i < nombreOnglets; i++){
				document.getElementById("contenuOnglet" + i).style.display = "none";
				document.getElementById("onglet" + i).className = '';
			
			}
			// Puis on affiche celui qui a été sélectionné
			document.getElementById("contenuOnglet" + numero).style.display = "block";
			document.getElementById("onglet" + numero).className = 'active';
		      }
		</script>
	</body>
</html>
