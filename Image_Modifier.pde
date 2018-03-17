PImage img;  // Declare a variable of type PImage

int box_l = 250, box_w = 15;
void setup() {
  size(365,400);
  // Make a new instance of a PImage by loading an image file
  img = loadImage("flower.jpg");
  background(100);
  fill(0);
  text("Height",310,20);
  text("Width",10,303);
  text("Red",10,323);
  text("Green",10,343);
  text("Blue",10,363);
  text("Alpha",10,383);
}
float h_y = 30 + box_l;
float w_x = 55 + box_l;
float r_x = 55 + box_l;
float b_x = 55 + box_l;
float g_x = 55 + box_l;
float a_x = 55 + box_l;

void draw() {
  fill(100);
  noStroke();
  rect(53, 285, box_l+10, 6*(box_w+10));
  rect(310, 28, box_w+20, box_l+20);
  
  // Sliders
  stroke(0);
  fill(255);
  rect(325, 30, box_w, box_l);
  rect(55, 290, box_l, box_w);
  rect(55, 310, box_l, box_w);
  rect(55, 330, box_l, box_w);
  rect(55, 350, box_l, box_w);
  rect(55, 370, box_l, box_w);
  
  fill(255);
  if(mousePressed) {
    if(mouseX >= 325 && mouseX <= 325+box_w && mouseY >= 30 && mouseY <= 30+box_l) {
      h_y = mouseY;
    }
    if(mouseX >= 55 && mouseX <= 55+box_l) {
      if(mouseY >= 290 && mouseY <= 290+box_w) {
        w_x = mouseX;
      } else if(mouseY >= 310 && mouseY <= 310+box_w) {
        r_x = mouseX;
      } else if(mouseY >= 330 && mouseY <= 330+box_w) {
        g_x = mouseX;
      } else if(mouseY >= 350 && mouseY <= 350+box_w) {
        b_x = mouseX;
      } else if(mouseY >= 370 && mouseY <= 370+box_w) {
        a_x = mouseX;
      }
    }
  }
  //pointers
  fill(255);
  rect(323, h_y-2, box_w+4, 4);
  rect(w_x-2, 288, 4, box_w+4);
  rect(r_x-2, 308, 4, box_w+4);
  rect(g_x-2, 328, 4, box_w+4);
  rect(b_x-2, 348, 4, box_w+4);
  rect(a_x-2, 368, 4, box_w+4);
  
  fill(100);
  stroke(0);
  rect(55,30,250,250); //Image box
  colorMode(RGB,250);
  tint((r_x-55), (g_x-55), (b_x-55), (a_x-55));
  image(img,55,30,(w_x-55),(h_y-30));
  colorMode(RGB,255);
}