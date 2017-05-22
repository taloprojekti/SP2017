#include <OneWire.h>
#include <DallasTemperature.h>

/*-----( Declare Constants and Pin Numbers )-----*/
#define ONE_WIRE_BUS_PIN 2

OneWire oneWire(ONE_WIRE_BUS_PIN);

DallasTemperature sensors(&oneWire);

DeviceAddress Probe01 = { 0x28, 0x06, 0x0C, 0x81, 0x07, 0x00, 0x00, 0xA1 }; 
DeviceAddress Probe02 = { 0x28, 0xFF, 0x79, 0xA4, 0x60, 0x14, 0x04, 0x62 };

void setup()  
{
  // start serial port to show results
  Serial.begin(9600);
 // Serial.print("Initializing Temperature Control Library Version ");
  //Serial.println(DALLASTEMPLIBVERSION);
  
  // Initialize the Temperature measurement library
  sensors.begin();
  
  // set the resolution to 10 bit (Can be 9 to 12 bits .. lower is faster)
  sensors.setResolution(Probe01, 10);
  sensors.setResolution(Probe02, 10);
}

void loop()  
{ 

  delay(1000);
  sensors.requestTemperatures();
    
  //float temp1 = sensors.getTempC(Probe01);
 // float temp2 = sensors.getTempC(Probe02);

  Serial.println(sensors.getTempC(Probe01));
  Serial.println(sensors.getTempC(Probe02));

}