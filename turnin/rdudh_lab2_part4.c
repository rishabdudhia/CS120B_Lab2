/*	Author: rdudh001
 *      Partner(s) Name: None
 *	Lab Section: 022
 *	Assignment: Lab #2  Exercise #4
 *	Exercise Description: [optional - include for your own benefit]
 *      Max weight on kids amusement park ride
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */

#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif	

int main(void) {
	DDRA = 0x00; PORTA = 0xFF; // Configure port A's 8 pins as inputs
	DDRB = 0x00; PORTB = 0xFF; // Configure port B's 8 pins as inputs 
	DDRC = 0x00; PORTC = 0xFF; // Configure port C's 8 pins as inputs
	DDRD = 0xFF; PORTD = 0x00; // Configure port D's 8 pins as outputs, initialize to 0x00
	//unsigned char i; // will be used in for loop
	//unsigned char currspot = 0x00; //looks at current spot in for loop
	//unsigned char cntavail = 0x00; // will hold count of total available spots
	unsigned char weightA = 0x00;
	unsigned char weightB = 0x00;
	unsigned char weightC = 0x00;
	unsigned short totalWeight = 0x00;
	short balanced = 0x00;
	unsigned char finalD = 0x00;
	while(1) {
		weightA = PINA;
		weightB = PINB;
		weightC = PINC;
		totalWeight = weightA + weightB + weightC;
		balanced = weightA - weightC;
		if (balanced < 0)
		{
		    balanced = balanced * -1;
		}
		
		if (totalWeight > 140)
		{
		    finalD = finalD | 0x01;
		}
		if (balanced > 80)
		{
		    finalD = finalD | 0x02;
		}

		totalWeight = totalWeight >> 2;
		totalWeight = totalWeight << 2;

		finalD = totalWeight | finalD;
		PORTD = finalD;
		finalD = 0x00;
	}
	return 0;
}
