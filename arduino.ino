char pyin;
int cw;
int i;
char b;
int cw2;
int senswal;

void setup() {
  Serial.begin(9600);
}

void loop() {
 //enter user code here. Whenever you think a command is needed from the python, use pyduino() function
 pyduino();
}


void pyduino(){
  
  if(Serial.available()){
    
    pyin = Serial.read();
    
    //analyzing the intput to determine function
    cw = (int)pyin;
    
    //Serial.println(cw);
    if(cw & 64){
      darw(cw);
  }
    else if(cw & 32){
      pm(cw);
   }
}
}

void darw(int cw){
  if( cw & 32){
    
      if(cw & 16){
        delay(2);
        if(Serial.available()){
           b = Serial.read();
        cw2 = b;
        if(cw2 & 15)
        digitalWrite(cw & 15,HIGH);
        else 
        digitalWrite(cw & 15,LOW);
        }
      }
      else{
        senswal = digitalRead(cw & 15);
        Serial.print(senswal);
      }
  }
  else
  {
    if( cw & 16){
   int pin =(int) cw & 15;
   delay(2);
   if(Serial.available()){
     b=Serial.read();
     int val= (int) (b & 255);
     analogWrite(pin,val);
     Serial.print(pin);
     Serial.print(val);  
   }
  }
  else
  {
    senswal = analogRead(cw & 15);
    Serial.println(senswal, DEC);
  }
  }
}

int pm(int cw){
  if(cw & 16){
    pinMode(cw & 15, OUTPUT);
    //Serial.println("pm output");
    return 1;
  }
  else {
    pinMode(cw & 15, INPUT);
    //Serial.println("pm input");
    return 1;
  }
}


