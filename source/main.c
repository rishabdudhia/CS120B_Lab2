/*	Author: rdudh001
 *      Partner(s) Name: None
 *	Lab Section: 022
 *	Assignment: Lab #2  Exercise #2
 *	Exercise Description: [optional - include for your own benefit]
 *      Output available parking spots on Port C
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */

#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif	

int main(void) {
	DDRA = 0x00; PORTA = 0xFF; // Configure port A's 8 pins as inputs
	DDRC = 0xFF; PORTC = 0x00; // Configure port B's 8 pins as outputs, initialize to 0s
	unsigned char i; // will be used in for loop
	unsigned char currspot = 0x00; //looks at current spot in for loop
	unsigned char cntavail = 0x00; // will hold count of total available spots
	while(1) {
		for (i = 0; i < 4; ++i)
		{
		    currspot = PINA >> i;
		    currspot = currspot & 0x01;
		    if (currspot == 0)
		    {
			cntavail = cntavail + 0x01;
		    }
		}
		PORTC = cntavail;	
	}
	return 0;
}
