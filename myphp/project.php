<?php 

session_start();

if(isset($_SESSION['counter'])){
	
	$_SESSION['counter']+=1;
	
	
}else {
	
	$_SESSION['counter']=1;
	
	
	
}

$my_msg="this page is visited";
$_SESSION['counter'];


$my_msg="time during this session";

?>

<html>

<head>
	
	<title>starting a php session</title>
	
	</head>

<body>
	
	<?php echo ($my_msg);
?>	
	
	
	
	
	
	</body>




</html>
