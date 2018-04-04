var x,y,t=0,u=45;

function setup(){
  createCanvas(300, 300);
  background(255,0,0);
  stroke(255);
  strokeWeight(5);
}

function draw(){
  translate(0,height);
ellipse(UX(),-UY(),5,5);
}

function UX(){
  x=(u*cos(PI/6)*t);
  return x;
}

function UY(){
  y=(u*sin(PI/3)*t - (9.8*t*t)/2);
  t+=0.1;
  return y;
}
