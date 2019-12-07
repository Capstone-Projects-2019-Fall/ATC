int ML1 = 5;
int ML2 = 4;
int MR1 = 13;
int MR2 = 12;
int EL = 3;   
int ER = 11; 
int r = 1;

void setup() {
  pinMode(ER, OUTPUT); 
  pinMode(EL, OUTPUT); 
  pinMode(ML1, OUTPUT); 
  pinMode(ML2, OUTPUT); 
  pinMode(MR1, OUTPUT); 
  pinMode(MR2, OUTPUT); 


  Serial.begin(9600);
}

void loop()
{
  if(Serial.available())
  {
    r = r * (Serial.read() - '0');
    if(r == 4) // go left
    {
      digitalWrite(ML1, LOW);
      digitalWrite(ML2, HIGH);
      digitalWrite(MR1, HIGH);
      digitalWrite(MR2, LOW);
      analogWrite(EL, 255);
      analogWrite(ER, 255);
    }
    else if(r == 5) // go right
    {
      digitalWrite(ML1, HIGH);
      digitalWrite(ML2, LOW);
      digitalWrite(MR1, LOW);
      digitalWrite(MR2, HIGH);
      analogWrite(EL, 255);
      analogWrite(ER, 255);
    }
    else if(r == 6) // go forward
    {
      digitalWrite(ML1, HIGH);
      digitalWrite(ML2, LOW);
      digitalWrite(MR1, HIGH);
      digitalWrite(MR2, LOW);
      analogWrite(EL, 255);
      analogWrite(ER, 255);
    }
    else if(r == 7) // go backwards
    {
      digitalWrite(ML1, LOW);
      digitalWrite(ML2, HIGH);
      digitalWrite(MR1, LOW);
      digitalWrite(MR2, HIGH);
      analogWrite(EL, 255);
      analogWrite(ER, 255);
    }
    else if(r == 0) // stop 
    {
      digitalWrite(ML1, LOW);
      digitalWrite(ML2, LOW);
      digitalWrite(MR1, LOW);
      digitalWrite(MR2, LOW);
    }
    r = 1;
  }
}
