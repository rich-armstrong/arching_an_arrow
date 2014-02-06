//
//  input_utilities.c
//  richards_c_utilities
//
//  Created by Raichu on 5/1/13.
//  Copyright (c) 2013 Raichu. All rights reserved.
//

#include <stdio.h>
#include <string.h> // strlen
#include <ctype.h>	// isdigit
#include <stdlib.h>	// atoi

#include "input_utilities.h"
#include "boolean.h"

int get_int
( const char * prompt
)
{
    boolean good_value = true;
    
    int     return_value	= 0;
    char    buffer [ 1024 ];
    
    for ( unsigned int i = 0; i < ( sizeof ( buffer ) / sizeof ( buffer [ 0 ] ) ); i++ )
    {
        buffer [ i ] = 0;
    }
    
    do
    {
        printf ( "%s", prompt );
        
        gets ( buffer );
        
        for ( int i = 0; i < strlen ( buffer ); i++ )
        {
            if ( buffer [0] == '-' )
            {
                // skip the negative sign
            }
            else if ( ! isdigit ( buffer [ i ] ) )
            {
                fprintf ( stdout, "invalid entry\n" );
                good_value = false;
                
                break;
            }
            else
            {
                good_value = true;
            }
        }
    }
    while ( good_value == false );
    
    return_value = atoi ( buffer );
    
    return return_value;
}

int
get_int_range
( int	min_value
, int	max_value
)
{
    int		user_input = 0;
    char	prompt [ 1024 ];

    sprintf ( prompt, "Give me an int between %d and %d: ", min_value, max_value );

    while ( true )
    {
      	user_input = get_int ( prompt );
        
      	if ( ( user_input < min_value ) || ( user_input > max_value ) )
        {
            fprintf ( stdout, "Not within the required range.\n" );
            
            continue;
        }
        else
        {
            break;
        }
    }

    return user_input;
}

char *
get_string
( const char * prompt
)
{
    char *  return_value    = NULL;
    char    buffer [ 1 * 1024 ];

    bzero ( buffer, sizeof ( buffer ) );

    do
    {
        fprintf ( stdout, "%s", prompt );
        gets ( buffer );
    }
    while (strlen ( buffer ) == 0);

    return_value =  malloc ( 1 + strlen ( buffer ) );

    strcpy ( return_value, buffer );

    if ( ! return_value)
    {
        // can't alloc
    }

    return return_value;
}

boolean get_yes_no ( char * yes_no_question )
{
    boolean yes = false;

    char answer [ 256 ];

    char testing_answer;

    do
    {
        fprintf ( stdout, "%s", yes_no_question );
        
        gets ( answer );
        
        testing_answer = toupper ( answer [ 0 ] );
    }
    while (		( testing_answer != 'Y' )
           &&	( testing_answer != 'N' ) );


    if ( testing_answer == 'Y' )
    {
        yes = true;
    }

    return yes;
}



















