int ML1 = 5;
int ML2 = 4;
int MR1 = 13;
int MR2 = 12;
int EL = 3;   
int ER = 11; 


void setup() {
  pinMode(ER, OUTPUT); 
  pinMode(EL, OUTPUT); 
  pinMode(ML1, OUTPUT); 
  pinMode(ML2, OUTPUT); 
  pinMode(MR1, OUTPUT); 
  pinMode(MR2, OUTPUT); 


  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly  
  //this code just goes straight,
      digitalWrite(ML1, HIGH);
      digitalWrite(ML2, LOW);
      digitalWrite(MR1, HIGH);
      digitalWrite(MR2, LOW);        
      analogWrite(EL, 155);  
      analogWrite(ER, 255);

      //Serial.println(s);
  //analogWrite(EL, 80);
  //delay(1000);
  
}
