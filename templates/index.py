<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>My BOT</title>
</head>
<body>
	<h1>My cool app!</h1>
	<form method="POST">
		<label>Question:</label>
		<!-- the double {} pulls the variable from our python script -->
	  	<input name=question type="text" value={{my_question}}><br><br>
	  	<input type="submit" value="Submit"><br><br>
	</form>
	<p>{{bot_response}}</p>
</body>
</html>