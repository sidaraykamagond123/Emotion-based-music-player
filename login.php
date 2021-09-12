<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhai+2&family=Zen+Tokyo+Zoo&display=swap"
        rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhai+2&family=Bangers&family=Zen+Tokyo+Zoo&display=swap"
        rel="stylesheet">
    <title>Login Page</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: sans-serif;
            background: url("index.jpeg");
            background-size: 100%;

        }

        .login-box {
            width: 300px;
            border-radius: 12px;
            position: absolute;
            padding: 13px;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #0e0704;
            background-color: rgba(128, 128, 128, 0.52);

        }

        .login-box h1 {
            float: left;
            font-size: 70px;
            padding-left: 74px;
            font-family: 'Baloo Bhai 2', cursive;
        }

        .textbox {
            width: 100%;
            overflow: hidden;
            font-size: 20px;
            padding: 8px 0;
            margin: 8px 0;
            border-bottom: 1px solid black;
            font-family: 'Baloo Bhai 2', cursive;
        }

        .fa {
            width: px;
            float: left;
            text-align: center;

        }

        .textbox input {
            border: none;
            outline: none;
            background: none;
            font-size: 18px;
            float: left;
            margin: 0 10px;
        }

        .button {
            width: 58%;
            padding: 8px;
            color: #ffffff;
            background: none #030336;
            border: none;
            border-radius: 6px;
            font-size: 18px;
            cursor: pointer;
            margin: 12px 0;
        }
    </style>
</head>

<body>


    <form name="f1" action="validate.php" method="POST" onsubmit="return validation();">
        <div class="login-box">
            <h1>Login</h1>

            <div class="textbox">
                <i class="fa fa-user" aria-hidden="true"></i>
                <input type="email" placeholder="E-mail" id="adminname" name="adminname" value="" >
            </div>

            <div class="textbox">
                <i class="fa fa-lock" aria-hidden="true"></i>
                <input type="password" placeholder="Password" id="password" name="password" value="">
            </div>

            <input class="button" type="submit" name="login" value="Sign In">

        </div>
    </form>
    <script>  
            function validation()  
            {  
                var id=document.f1.adminname.value;  
                var ps=document.f1.password.value;  
                if(id.length=="" && ps.length=="") {  
                    alert("User Name and Password fields are empty");  
                    return false;  
                }  
                else  
                {  
                    if(id.length=="") {  
                        alert("User Name is empty");  
                        return false;  
                    }   
                    if (ps.length=="") {  
                    alert("Password field is empty");  
                    return false;  
                    }  
                }                             
            }  
        </script>
</body>

</html>