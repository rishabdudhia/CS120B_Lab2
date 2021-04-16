# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).

tests = [ {'description': 'PINA: 0x10, PINB: 0x17, PINC: 0x12  => PORTD: 0x38',
    'steps': [ {'inputs': [('PINA',0x10)], 'iterations': 5 },
	{'inputs': [('PINB', 0x17)], 'iterations': 5 },
	{'inputs': [('PINC', 0x12)], 'iterations': 5 }],
    'expected': [('PORTD',0x38)],
    },
    {'description': 'PINA: 0x35, PINB: 0x2C, PINC: 0x33 => PORTD: 0x95',
    'steps': [ {'inputs': [('PINA',0x35)], 'iterations': 5 },
	{'inputs': [('PINB', 0x2C)], 'iterations': 5 },
        {'inputs': [('PINC', 0x33)], 'iterations': 5 } ],
    'expected': [('PORTD',0x95)],
    },
    {'description': 'PINA: 0x5E, PINB: 0x20, PINC: 0x0C => PORTD: 0x8A',
    'steps': [ {'inputs': [('PINA',0x5E)], 'iterations': 5 },
        {'inputs': [('PINB', 0x20)], 'iterations': 5 },
        {'inputs': [('PINC', 0x0C)], 'iterations': 5 } ],
    'expected': [('PORTD',0x8A)],
    },
    {'description': 'PINA: 0x64, PINB: 0x1B, PINC: 0x0D => PORTD: 0x8E',
    'steps': [ {'inputs': [('PINA',0x64)], 'iterations': 5 },
        {'inputs': [('PINB', 0x1B)], 'iterations': 5 },
        {'inputs': [('PINC', 0x0D)], 'iterations': 5 } ],
    'expected': [('PORTD',0x8E)],
    },
    {'description': 'PINA: 0x00, PINB: 0x00, PINC: 0x00 => PORTD: 0x00',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 5 },
        {'inputs': [('PINB', 0x00)], 'iterations': 5 },
        {'inputs': [('PINC', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTD',0x00)],
    },
    {'description': 'PINA: 0xFF, PINB: 0x19, PINC: 0x0C => PORTD: 0x27',
    'steps': [ {'inputs': [('PINA',0xFF)], 'iterations': 5 },
        {'inputs': [('PINB', 0x19)], 'iterations': 5 },
        {'inputs': [('PINC', 0x0C)], 'iterations': 5 } ],
    'expected': [('PORTD',0x27)],
    },
    {'description': 'PINA: 0x2F, PINB: 0x31, PINC: 0x18 => PORTD: 0x78',
    'steps': [ {'inputs': [('PINA',0x2F)], 'iterations': 5 },
        {'inputs': [('PINB', 0x31)], 'iterations': 5 },
        {'inputs': [('PINC', 0x18)], 'iterations': 5 } ],
    'expected': [('PORTD',0x78)],
    },
    {'description': 'PINA: 0x10, PINB: 0x0A, PINC: 0x6C => PORTD: 0x86',
    'steps': [ {'inputs': [('PINA',0x10)], 'iterations': 5 },
        {'inputs': [('PINB', 0x0A)], 'iterations': 5 },
        {'inputs': [('PINC', 0x6C)], 'iterations': 5 } ],
    'expected': [('PORTD',0x86)],
    },
    ]

#watch = ['main::totalWeight','main::balance']


# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
