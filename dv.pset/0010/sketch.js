var PI=22/7;
var a=PI/2;
var f=5;
var x,y;
function setup(){
	createCanvas(300, 300);
	background(255,0,0);
	strokeWeight(1);
	x=0;
	//t=1;
	//a=150;
	//f=50;

}

function draw(){
x++;
y=100+sin(((a)*(PI/6))*50);
a++;
ellipse(x, y, 1, 1);

}
