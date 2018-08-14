var m=180, n=0,r=20, x,y;
function setup(){
	createCanvas(500,500);
	background(250,250,250);
	strokeWeight(1);
	ellipse(250,250, 5, 5);
	frameRate(5);
}
function draw(){
//	clear();
stroke(0,255,0);
//green tiny circle
x= 250+r*sin(m);
y= 250+r*cos(m);
m=m+0.1;
ellipse(x, y, 5, 5);

x= 250+(180)*sin(m);
y= 250+(180)*cos(m);
m=m+0.1;
ellipse(x, y, 5, 5);

x= 250+(100)*sin(m);
y= 250+(100)*cos(m);
m=m+0.1;
ellipse(x, y, 5, 5);

x= 250+(140)*sin(m);
y= 250+(140)*cos(m);
m=m+0.1;
ellipse(x, y, 5, 5);

a= 250+(60)*sin(m);
b= 250+(60)*cos(m);
m=m+0.4;
ellipse(a, b, 5, 5);

//green tiny circle2
x= 250+(60)*sin(n);
y= 250+(60)*cos(n);
m=m+0.1;
ellipse(x, y, 5, 5);

//moon
stroke(255,255,255);
x= a+(20)*sin(n);
y= b+(20)*cos(n);
n=n+0.4;
ellipse(x, y, 5, 5);

}
