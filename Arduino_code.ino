const int analogPort[3] = {A0, A1, A2, A3};
// number of measures
const int n_max = 5;

void setup(){
  Serial.begin(9600);
  delay(2000);
}

void loop(){
  int n = 0;
  int airQ[4]{};

  while (n < n_max){
    for (int i = 0; i < 4; i++){
      airQ[i] = airQ[i] + analogRead(analogPort[i]);
    }
    delay(2000);
    n++;
  }
  for (int i = 0; i < 4; i++)
  {
    airQ[i] = airQ[i] / n_max;
    if (i != 3)
    {
      Serial.print(airQ[i]);
      Serial.print(',');
    }
    else
    {
      Serial.println(airQ[i]);
    }
  }
}