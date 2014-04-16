<html>
<body>
<h1> ADD USERS HERE!!!</h1>
<form id="myform" action="submit.php" method="post">
	RFID card address:<input type="text" name = "addr"> <br>
	user:<input type="text" name = "name">
	
	
	<input type="submit" value="Submit">
	<!--<button id="sub"> Submit </button>-->
</form>


<h1> Remove USERS HERE!!!</h1>
<form id="myform" action="remove.php" method="post">
	RFID card address:<input type="text" name = "addr"> <br>
	user:<input type="text" name = "name">
	
	
	<input type="submit" value="Submit">
	<!--<button id="sub"> Submit </button>-->
</form>

<h3>Click to view the log of who has come and gone</h3>
<a href="viewlog.php">View Log</a>

<h3>Click to clear the log</h3>
<a href="clearlog.php">Clear Log</a>



</body>
</html>