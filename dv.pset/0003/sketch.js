var m=180, n=0,r=20, x,y;

function setup(){
	createCanvas(300, 300);
	background(50,50,50);
	strokeWeight(1);
}

function draw(){

x= 150+r*cos(m);
y= 150+r*sin(m);
m=m+0.1;
ellipse(x, y, 5, 5);

}
