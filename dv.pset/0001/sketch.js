var x=200;
var y=200;
var z=0;
function setup(){
  createCanvas (windowWidth,windowHeight);
  background(255,0,0);
  stroke(0);
  }
function draw(){
background(255,0,0);
  ellipse(x,y,100,100);


  if (x==0) {
    z=0;
  } else if (x>windowWidth) {
    z=1;
  }

  if (x<=windowWidth && z==0) {
    x=x+10;
  } else if (x>0 && z==1) {
    x=x-10;
  }
}
