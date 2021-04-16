/*	Author: rdudh001
 *      Partner(s) Name: None
 *	Lab Section: 022
 *	Assignment: Lab #2  Exercise #1
 *	Exercise Description: [optional - include for your own benefit]
 *      Garage open at night
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */

#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif	

int main(void) {
	DDRA = 0x00; PORTA = 0xFF; // Configure port A's 8 pins as inputs
	DDRB = 0xFF; PORTB = 0x00; // Configure port B's 8 pins as outputs, initialize to 0s
	unsigned char pa0 = 0x00; // Temporary variable to hold the value of B
	unsigned char pa1 = 0x00; // Temporary variable to hold the value of A
	while(1) {
		// 1) Read input
		pa0 = PINA & 0x01; //check if door is open
		pa1 = PINA & 0x02; // check if light is sensed
		// 2) Perform computation
		if (pa0 && !pa1)
		{
		    PORTB = 0x01;
		}
		else
		{
		    PORTB = 0x00;
		}
		// 3) Write output
		// PORTB = tmpB;	
	}
	return 0;
}
