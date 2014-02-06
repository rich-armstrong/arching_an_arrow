//
//  input_utilities.h
//  richards_c_utilities
//
//  Created by Raichu on 5/1/13.
//  Copyright (c) 2013 Raichu. All rights reserved.
//

#ifndef richards_c_utilities_input_utilities_h
#define richards_c_utilities_input_utilities_h

#include "boolean.h"

int 	get_int				( const	char *	prompt					);
int		get_int_range	( 			int		min_value
                    ,		 		int		max_value					);
char *	get_string	( const char *	prompt					);
boolean	get_yes_no	( 			char *	yes_no_question	);

#endif	/* richards_c_utilities_input_utilities_h */

