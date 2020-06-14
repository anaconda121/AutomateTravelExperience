<?php
	date_default_timezone_set('America/New York');
	require 'templates\forum\dbh.php';
	require 'templates\forum\comments.php';
?>

<main>
	<!DOCTYPE html>
	<html>
	  <head>		  
	  	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
		<link href="https://fonts.googleapis.com/css2?family=Comfortaa&display=swap" rel="stylesheet">
		<link href="https://use.fontawesome.com/releases/v5.13.0/css/all.css" rel="stylesheet">
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width">
	    <title>Forum</title>
	  </head>
	  <body>

		<section class="flex center banner">
			<header class="flex">
				<nav class="options">
					<a style = 'color: #FDBD01;' class="link" href="/home">All About US</a>
					<a style = 'color: #FDBD01;'  class="link" href="/algo">Airport Ticket Ratings</a>
					<a style = 'color: #FDBD01;'  class = "link" href = "/planner">Trip Planner</a>
					<a  style = 'color: #FDBD01;' class="link" href="/stats">COVID-Stats</a>
					<a style = 'color: #FDBD01;'  class="link" href="/asteroids">COVID-Asteroids</a>
					<a style = 'color: #FDBD01;'  class = "link" href = "/snake">COVID-Snake Game</a>
					<a style = 'color: #FDBD01;'  class = "link" href = "/logout"> Logout </a>
				</nav>
			</header>
		</section>

	 	<?php
			echo "<form method = 'POST' action = 'forum\comments.php'>
				<input type = 'hidden' name = 'id' value='anonymous'>
				<input type = 'hidden' name = 'date' value=".date('Y-m-d H:i:s').">
				<textarea name = 'message'></textarea>
				<button type = 'submit' name = 'message_submit'> Submit </button>
			</form>";
	  	?>
	  </body>
	</html>

	<style>
		body {
			background-color: rgb(42,42,42);
		}

		textarea {
			width: 40%;
			height: 15%;
			background-color: rgb(42,42,42);
			resize: none;
			position:absolute;
			top:30%;
			left:10%;
			color: #FDBD01;
		}

		button {
			width: 5%;
			height: 3%;
			position:absolute;
			top:30%;
			left:55%;
			background-color: rgb(42,42,42);
			color: #FDBD01;
			font-weight:400;
			cursor:pointer;
		}

		header {
			width: 100%;
			flex-direction: column;
		}

		header nav.options {
			padding: 1em;
			text-align: center;
		}

		header nav.options a {
			margin: 0.5em;
			font-size: 1.1em;
			color: black;
			cursor: pointer;
			text-decoration: none;
		}

		a.link {
			display: inline-block;
		}

		a.link::after {
			content: "";
			display: block;
			position: relative;
			left: 50%;
			transform: translateY(0.5em) translateX(-50%);
			width: 0;
			height: 2px;
			background: var(--secondary);
			transition: width 0.3s ease;
		}

		a.link:hover::after  {
			width: 100%;
		}

		section.banner {
			background: linear-gradient(to bottom, transparent, var(--primary), var(--primary)), url("main-bg.jpg") no-repeat;
			background-size: auto calc(100vw);
			background-attachment: fixed;
			min-height: 50vw;
			text-align: center;
			flex-direction: column;
		}

		section.banner h1 {
			word-break: break-word;
			font-size: 4em;
			margin: 20vh 0 0.5em 0;
			text-shadow: 0 0 0.5em var(--secondary);
			color: var(--secondary);
		}

		section.banner > div {
			max-width: 60%;
			flex-direction: column;
		}

		section.banner > div p {
			font-size: 1.1em;
			margin: 0 0 2em 0;
		}
	</style>
</main>