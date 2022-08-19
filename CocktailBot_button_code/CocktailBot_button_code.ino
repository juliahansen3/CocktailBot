//from https://funprojects.blog/2018/02/18/arduino-talking-to-node-red-and-python/
/*
Test TCP client to send message
 */
#include <WiFiNINA.h>
#define button 7 //connected to pin 7
#include "arduino_secret.h"

char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int status = WL_IDLE_STATUS;     // the Wifi radio's status
const uint16_t port = 8888;          // port to use
const char * host = "192.168.1.102"; // address of host server
String msg;
// Use WiFiClient class to create TCP connections
WiFiClient client;

bool pressed =false;
int buttonval;

void setup() {
  Serial.begin(9600); // initialize serial communication
  pinMode(button, INPUT_PULLUP); //set up button
  buttonval= digitalRead(button); //store value of button
  while (!Serial);

  // attempt to connect to Wifi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to network: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }

  // you're connected now, so print out the data:
  Serial.println("You're connected to the network");
  
  Serial.println("----------------------------------------");
  //printData();
  Serial.println("----------------------------------------");
  

}

void loop() {
  int Valbutton=digitalRead(button); 
  if (!client.connect(host, port)) { //check for connection to socket
      Serial.println("connection failed");
      Serial.println("wait 5 sec...");
      delay(5000);
      return;
  }
  // Send message to TCP server
  else{
    if(Valbutton != buttonval){ //compare values to see if it changed
      if(Valbutton==LOW && pressed==false) {
        msg="Button was pressed";
        //pressed=true;
        client.print(msg);
        Serial.print("Sent : ");
        Serial.println(msg);
        client.stop();    
        }
      else {
        msg="Button not pressed";
        /*client.print(msg);
        Serial.print("Sent : ");
        Serial.println(msg);
        client.stop(); */
      }
   }
  }
  delay(100);

}
