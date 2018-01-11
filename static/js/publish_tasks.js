function course_1(str)
{
  var xmlhttp;
  if (window.XMLHttpRequest)
  {
    // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
  }
  else
  {
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      document.getElementById("My_module").innerHTML=xmlhttp.responseText;
    }
  };
  xmlhttp.open("GET","/submit_course_info?q="+str,true);
  // xmlhttp.setRequestHeader('content-type','application/x-www-form-urlencoded');
  xmlhttp.send();
}

function course_2(str)
{
  var xmlhttp;
  if (window.XMLHttpRequest)
  {
    // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
  }
  else
  {
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      document.getElementById("Second_module").innerHTML=xmlhttp.responseText;
    }
  };
  xmlhttp.open("GET","/submit_module_info?q="+str,true);
  // xmlhttp.setRequestHeader('content-type','application/x-www-form-urlencoded');
  xmlhttp.send();
}

function course_3(str)
{
  var xmlhttp;
  if (window.XMLHttpRequest)
  {
    // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
  }
  else
  {
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      document.getElementById("content").innerHTML=xmlhttp.responseText;
    }
  };
  xmlhttp.open("GET","/submit_knowledgebase_info?q="+str,true);
  // xmlhttp.setRequestHeader('content-type','application/x-www-form-urlencoded');
  xmlhttp.send();
}