


function quizCount(){
if(sessionStorage.length==0){
s=59
m=0

}
else {
var c=  sessionStorage.getItem("name"); 
var d=  sessionStorage.getItem("mame"); 
s=parseInt(c,10);
m=parseInt(d,10);
}



console.log("this is qiz count 	");

document.getElementById('timer').value=m+":"+s+" remaining";





s=s-1


q=setTimeout("quizCount()", 1000)
document.getElementById('timer').value=m+":"+s+" remaining";

if (s<1)
{ m=m-1; s=59;}
sessionStorage.setItem("name", s);
sessionStorage.setItem("mame", m);
if (m<0)
{
quizStop();
}
console.log(s);
document.getElementById('oa').value=m;
document.getElementById('ob').value=s;


}

function quizStop()
{
clearTimeout(q)
document.getElementById('timer').value="Your Time Was Finished"
document.getElementById('flags').value=1
 document.getElementById('next').click();
}



