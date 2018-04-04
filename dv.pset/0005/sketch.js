var x=0;
var y=200;
var z=0;
var a=600;
var c=0;
function setup(){
  createCanvas (600,400);
  background(255,0,0);
  stroke(0);
  }
function draw(){
background(255,0,0);
  ellipse(x,y,10,10);
  if (x==0) {
    z=0;
} else if (x>600) {
    z=1;
  }

  if (x<=600 && z==0) {
    x=x+10;
  } else if (x>0 && z==1) {
    x=x-10;
  }

  ellipse(a,y,10,10);
  if (a==0) {
    c=0;
} else if (a>600) {
    c=1;
  }

  if (a<=600 && c==0) {
    a=a+10;
} else if (a>0 && c==1) {
    a=a-10;
  }
}
